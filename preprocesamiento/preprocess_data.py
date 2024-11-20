import os
import pandas as pd
import javalang
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Function to read a Java file
def read_java_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to extract AST nodes
def extract_ast_nodes(code):
    tokens = list(javalang.tokenizer.tokenize(code))
    parser = javalang.parser.Parser(tokens)
    tree = parser.parse()
    ast_nodes = [node.__class__.__name__ for path, node in tree if isinstance(node, javalang.tree.Node)]
    return ' '.join(ast_nodes) if ast_nodes else ''

# Preprocess all pairs and save a single pkl file
def preprocess_and_save_single_pkl(base_dir, labels_file, output_file):
    data = []
    labels = pd.read_csv(labels_file)
    
    for index, row in labels.iterrows():
        sub1, sub2, label = row['sub1'], row['sub2'], row['verdict']
        folder_name = f"{sub1}_{sub2}"
        pair_folder = os.path.join(base_dir, folder_name)
        file1_path = os.path.join(pair_folder, f"{sub1}.java")
        file2_path = os.path.join(pair_folder, f"{sub2}.java")

        if os.path.exists(file1_path) and os.path.exists(file2_path):
            code1 = read_java_file(file1_path)
            code2 = read_java_file(file2_path)
            try:
                ast_nodes1 = extract_ast_nodes(code1)
            except Exception as e:
                print(f"Error extracting AST nodes in file {file1_path} : {e}")
            try:
                ast_nodes2 = extract_ast_nodes(code2)
            except Exception as e:
                print(f"Error extracting AST nodes in file {file2_path} : {e}")

            if ast_nodes1 and ast_nodes2:
                combined_ast_nodes = ast_nodes1 + ' ' + ast_nodes2
                data.append({'code': combined_ast_nodes, 'label': label, 
                             'ast_nodes1': ast_nodes1, 'ast_nodes2': ast_nodes2})

    # TF-IDF vectorization
    df = pd.DataFrame(data)
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)
    df['vectorized_code'] = list(tfidf_vectorizer.fit_transform(df['code']).toarray())
    
    # Save everything in a single .pkl file
    joblib.dump({'data': df, 'vectorizer': tfidf_vectorizer}, output_file)
    print(f"Data saved in {output_file}")

if __name__ == "__main__":
    base_dir = '../dataset_raw/conplag_version_2/versions/version_2'  # Base folder containing subfolders for pairs
    labels_file = '../dataset_raw/conplag_version_2/versions/labels.csv'  # Path to the CSV file
    output_file = '../dataset_final/all_data.pkl'  # Single pkl file to store all data
    
    preprocess_and_save_single_pkl(base_dir, labels_file, output_file)
