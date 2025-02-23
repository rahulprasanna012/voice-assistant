import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Download NLTK resources if not already downloaded
# nltk.download('stopwords')
# nltk.download('punkt')


# Load Q&A dataset from a text file
def load_dataset(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':', 1) for line in lines if ':' in line]  # Split only at the first ':'
        dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs if q.strip() and a.strip()]

    if not dataset:
        raise ValueError("Dataset is empty or incorrectly formatted. Ensure 'question:answer' format.")

    # print(f"✅ Loaded {len(dataset)} Q&A pairs.")  # Debugging statement
    return dataset


# Preprocess the text (tokenization, stopwords removal, stemming)
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())

    # Keep only alphanumeric words, remove stopwords
    filtered_tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]

    return ' '.join(filtered_tokens) if filtered_tokens else text  # Return original text if all words are removed


# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]

    if not any(corpus):  # Ensure there's valid text
        raise ValueError("The preprocessed corpus is empty. Check your dataset content.")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)

    # print("✅ TF-IDF vectorizer trained successfully.")  # Debugging statement
    return vectorizer, X


# Retrieve the most relevant answer using cosine similarity
def get_answer(question, vectorizer, X, dataset):
    processed_question = preprocess_text(question)

    if not processed_question:
        return "I couldn't understand your question."

    question_vec = vectorizer.transform([processed_question])
    similarities = cosine_similarity(question_vec, X)

    # print(f"🔍 Similarity scores: {similarities.flatten()}")  # Debugging statement

    best_match_index = similarities.argmax()

    # If similarity score is too low, return a default response
    if similarities[0, best_match_index] < 0.2:  # Adjust threshold if needed
        return "I'm not sure, can you rephrase the question?"

    return dataset[best_match_index]['answer']


# Main function to process a user query
def mind(text):
    try:
        dataset_path = r'D:\final-year-project-2025\Data\new_data.txt'  # Update with your actual dataset path
        dataset = load_dataset(dataset_path)

        vectorizer, X = train_tfidf_vectorizer(dataset)

        # Debugging: Check input and preprocessed text
        # print(f"📝 User question: {text}")
        processed_text = preprocess_text(text)
        # print(f"🔍 Preprocessed: {processed_text}")

        answer = get_answer(text, vectorizer, X, dataset)
        return answer
    except FileNotFoundError as fnf_error:
        return f"❌ Error: {fnf_error}"
    except ValueError as ve:
        return f"❌ Error: {ve}"


