import sys
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure NLTK resources are downloaded
# nltk.download('punkt_tab')
# nltk.download('punkt')

def chunk_text(text, chunk_size):
    words = nltk.word_tokenize(text)
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def calculate_similarity(chunks1, chunks2):
    vectorizer = TfidfVectorizer()
    vectors1 = vectorizer.fit_transform(chunks1)
    vectors2 = vectorizer.transform(chunks2)
    return cosine_similarity(vectors1, vectors2)

if __name__ == '__main__':
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    # Load files
    data1 = None
    with open(filename1, 'r') as file:
        data1 = file.read()

    data2 = None
    with open(filename2, 'r') as file:
        data2 = file.read()

    # Define chunk size
    chunk_size = 1000  # Adjust based on desired chunk length

    # Chunk the text
    chunks1 = chunk_text(data1, chunk_size)
    chunks2 = chunk_text(data2, chunk_size)

    # Ensure equal chunk length by truncating the longer list
    min_length = min(len(chunks1), len(chunks2))
    chunks1, chunks2 = chunks1[:min_length], chunks2[:min_length]

    # Calculate similarity
    similarity_matrix = calculate_similarity(chunks1, chunks2)

    # Print average similarity
    avg_similarity = similarity_matrix.trace() / min_length
    print(f"Average similarity between the files: {avg_similarity:.2f}")
