from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

from Base.Ear import listen
from Function.utils import speak_async

tokenizer = AutoTokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")
model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/grammar_error_correcter_v1")

def correct_grammar_with_huggingface(text):
    input_text = "gec: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)
    outputs = model.generate(input_ids, max_length=128, num_beams=5, early_stopping=True)
    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected

def learn_english():
    speak_async("Please speak a sentence you want me to correct.")
    sentence = listen()
    if sentence:
        corrected = correct_grammar_with_huggingface(sentence)
        if sentence.strip().lower() == corrected.strip().lower():
            speak_async("Your sentence is already correct!")
        else:
            speak_async("I found some mistakes. The correct sentence is:")
            speak_async(corrected)

        print(f"Original: {sentence}")
        print(f"Corrected: {corrected}")
    else:
        speak_async("I didn't catch anything. Please try again.")

learn_english()