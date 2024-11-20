import os
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import javalang
import shutil

# Function to read a Java file
def read_java_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ''

# Function to extract AST nodes from Java code
def extract_ast_nodes(code):
    try:
        tokens = list(javalang.tokenizer.tokenize(code))
        parser = javalang.parser.Parser(tokens)
        tree = parser.parse()
        ast_nodes = [node.__class__.__name__ for path, node in tree if isinstance(node, javalang.tree.Node)]
        return ' '.join(ast_nodes) if ast_nodes else ''
    except Exception as e:
        print(f"Error extracting AST nodes: {e}")
        return ''

# Function to classify new Java code
def classify_new_code(new_code_path, pkl_file, plagiarized_folder, not_plagiarized_folder):
    # Load the dataset and vectorizer
    data = joblib.load(pkl_file)
    df = data['data']
    tfidf_vectorizer = data['vectorizer']

    # Process the new code
    new_code = read_java_file(new_code_path)
    new_ast_nodes = extract_ast_nodes(new_code)
    if not new_ast_nodes:
        print("No AST nodes extracted from the new code. Cannot classify.")
        return

    new_vector = tfidf_vectorizer.transform([new_ast_nodes]).toarray()

    # Compare similarity with all stored pairs
    similarity_scores = cosine_similarity(new_vector, list(df['vectorized_code']))
    most_similar_index = similarity_scores.argmax()
    most_similar_score = similarity_scores[0, most_similar_index]

    # Threshold to decide plagiarism
    threshold = 0.8  # Adjust based on dataset performance
    if most_similar_score >= threshold:
        print(f"Code is plagiarized. Similarity: {most_similar_score:.4f}")
        shutil.move(new_code_path, os.path.join(plagiarized_folder, os.path.basename(new_code_path)))
    else:
        print(f"Code is not plagiarized. Similarity: {most_similar_score:.4f}")
        shutil.move(new_code_path, os.path.join(not_plagiarized_folder, os.path.basename(new_code_path)))

# Main execution
if __name__ == "__main__":
    new_code_path = r'../dataset_final/java_files'  # Path to new Java file
    pkl_file = '../dataset_final/all_data.pkl'  # Path to the combined pkl file
    plagiarized_folder = 'plagiarized'  # Folder to move plagiarized files
    not_plagiarized_folder = 'not_plagiarized'  # Folder for non-plagiarized files
    
    os.makedirs(plagiarized_folder, exist_ok=True)
    os.makedirs(not_plagiarized_folder, exist_ok=True)

    classify_new_code(new_code_path, pkl_file, plagiarized_folder, not_plagiarized_folder)
