import os
import pandas as pd
import javalang
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def read_java_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ''

def extract_ast_nodes(code):
    try:
        tokens = list(javalang.tokenizer.tokenize(code))
        parser = javalang.parser.Parser(tokens)
        tree = parser.parse()
        ast_nodes = [node.__class__.__name__ for path, node in tree if isinstance(node, javalang.tree.Node)]
        return ' '.join(ast_nodes) if ast_nodes else ''
    except Exception as e:
        print(f"Error parsing code: {e}")
        return ''

def preprocess_from_folders(data_dir, labels_csv):
    labels_df = pd.read_csv(labels_csv)
    data = []
    labels = []

    for _, row in labels_df.iterrows():
        subfolder = f"{row['sub1']}_{row['sub2']}"  # Folder named after file pairs
        subfolder_path = os.path.join(data_dir, subfolder)

        file1_path = os.path.join(subfolder_path, f"{row['sub1']}.java")
        file2_path = os.path.join(subfolder_path, f"{row['sub2']}.java")

        code1 = read_java_file(file1_path)
        code2 = read_java_file(file2_path)

        if code1.strip() and code2.strip():
            ast1 = extract_ast_nodes(code1)
            ast2 = extract_ast_nodes(code2)

            if ast1 and ast2:
                combined_ast = ast1 + ' ' + ast2
                data.append(combined_ast)
                labels.append(row['verdict'])
            else:
                print(f"Skipping folder {subfolder} due to empty AST.")
        else:
            print(f"Skipping folder {subfolder} due to missing code files.")

    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(data)
    return X, labels, vectorizer

def train_random_forest_with_smote(X, y, model_path, vectorizer_path, test_data_path):
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    joblib.dump((X_test_raw, y_test), test_data_path)
    print(f"Original test data saved to {test_data_path}")

    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_raw, y_train)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train_resampled, y_train_resampled)

    joblib.dump(clf, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    print(f"Model saved to {model_path}")
    print(f"Vectorizer saved to {vectorizer_path}")

if __name__ == "__main__":
    data_directory = r'versions\version_2'
    labels_csv = r'versions\labels.csv'
    model_output_path = r'RF_SMOTE\random_forest_model.pkl'
    vectorizer_output_path = r'RF_SMOTE\tfidf_vectorizer.pkl'
    test_data_path = r'RF_SMOTE\test_data.pkl'

    # Preprocess the data
    X, y, vectorizer = preprocess_from_folders(data_directory, labels_csv)

    train_random_forest_with_smote(X, y, model_output_path, vectorizer_output_path, test_data_path)
