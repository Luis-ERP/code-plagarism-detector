import os
import joblib
import pandas as pd
import javalang
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

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
    return X, labels

def train_random_forest(X, y, model_path):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    joblib.dump((X_test, y_test), preprocessed_data_path)
    print(f"Preprocessed test data saved to {preprocessed_data_path}")

    joblib.dump(clf, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    data_directory = r'versions\version_2'
    labels_csv = r'versions\labels.csv'
    model_output_path = r'RF\random_forest_model.pkl'
    vectorizer_output_path = r'RF\tfidf_vectorizer.pkl'
    preprocessed_data_path = r'RF\test_data.pkl'

    # Preprocess and train
    X, y = preprocess_from_folders(data_directory, labels_csv)

    train_random_forest(X, y, model_output_path)
