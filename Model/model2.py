import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# nltk.download('stopwords')
# nltk.download('punkt')


# Load your Q&A dataset from a text file
def load_dataset(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q, 'answer': a} for q, a in qna_pairs if q and a]

    if not dataset:
        raise ValueError("Dataset is empty or not properly formatted.")

    return dataset


# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    # Keep alphanumeric tokens and remove stopwords
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]

    if not tokens:
        return ""  # Return empty string if nothing is left after preprocessing

    return ' '.join(tokens)


# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]

    if not any(corpus):  # Check if the corpus is empty after preprocessing
        raise ValueError("The preprocessed corpus is empty. Ensure your dataset has valid questions.")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X


# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)

    if not question:
        return "I couldn't understand your question."

    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()

    return dataset[best_match_index]['answer']


# Main function
def mind(text):
    try:
        dataset_path = r'D:\Myjarvis\pythonProject1\Data\qna.txt'  # Replace with your dataset path
        dataset = load_dataset(dataset_path)

        vectorizer, X = train_tfidf_vectorizer(dataset)

        # Get the answer for the user-provided question
        answer = get_answer(text, vectorizer, X, dataset)
        return answer
    except FileNotFoundError as fnf_error:
        return f"Error: {fnf_error}"
    except ValueError as ve:
        return f"Error: {ve}"


# Test with a sample question

