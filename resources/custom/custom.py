from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import javalang
import argparse


def read_java_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
# Extract AST nodes
def extract_ast_nodes(code):
    tokens = list(javalang.tokenizer.tokenize(code))
    parser = javalang.parser.Parser(tokens)
    tree = parser.parse()
    ast_nodes = [node.__class__.__name__ for path, node in tree if isinstance(node, javalang.tree.Node)]
    return ' '.join(ast_nodes) if ast_nodes else ''


if __name__ == '__main__':
    """
    Example of execution:
    python resources/custom/custom.py -p versions/version_1/00af3420_5449d33c/00af3420.java versions/version_1/00af3420_5449d33c/5449d33c.java
    """
    parser = argparse.ArgumentParser(description='Process two Java files.')
    parser.add_argument('-p', '--paths', nargs=2, required=True, help='Paths to the two Java files')
    args = parser.parse_args()

    file1, file2 = args.paths

    code1 = read_java_file(file1)
    code2 = read_java_file(file2)

    ast_nodes1 = extract_ast_nodes(code1)
    ast_nodes2 = extract_ast_nodes(code2)

    if ast_nodes1 and ast_nodes2:
        # Combine AST nodes into a single list for TF-IDF
        ast_corpus = [ast_nodes1, ast_nodes2]

        # Apply TF-IDF to vectorize AST nodes
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(ast_corpus)

        # Compute cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        print(f"Cosine Similarity between the two Java files: {similarity:.4f}")

        if similarity > 0.8:  # Threshold for plagiarism detection
            print("The files are likely plagiarized.")
        else:
            print("The files are unlikely to be plagiarized.")
    else:
        print("One or both files could not be parsed into AST nodes.")