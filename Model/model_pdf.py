import fitz  # PyMuPDF for PDF text extraction
from sentence_transformers import SentenceTransformer, util

# Load a lightweight Hugging Face model for semantic search
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


# Extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = " ".join([page.get_text("text") for page in doc])
    return text if text.strip() else None


# Convert sentences into embeddings
def get_sentence_embeddings(sentences):
    return model.encode(sentences, convert_to_tensor=True)


# Find the most relevant answer using cosine similarity
def get_best_answer(question, sentences, embeddings):
    question_embedding = model.encode(question, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(question_embedding, embeddings)[0]
    best_match_index = scores.argmax().item()

    return sentences[best_match_index] if scores[best_match_index] > 0.4 else "I couldn't find a relevant answer."


# Main function
def ask_pdf(pdf_path, question):
    pdf_text = extract_text_from_pdf(pdf_path)
    if not pdf_text:
        return "❌ Error: Failed to extract text from PDF."

    sentences = pdf_text.split(". ")  # Split text into sentences
    embeddings = get_sentence_embeddings(sentences)

    return get_best_answer(question, sentences, embeddings)


# Example Usage
pdf_file = "D:/final-year-project-2025/Data/sample.pdf"
user_question = "emoji"
response = ask_pdf(pdf_file, user_question)
print(f"🤖 AI Response: {response}")
