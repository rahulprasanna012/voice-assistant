import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def llm2(text):
    # Load GPT-J (6B) or GPT-Neo (1.3B or 2.7B)
    model_name = "EleutherAI/gpt-j-6B"  # or "EleutherAI/gpt-neo-2.7B" for GPT-Neo
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Encode the input text
    inputs = tokenizer(text, return_tensors="pt")

    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            inputs['input_ids'],
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            pad_token_id=tokenizer.eos_token_id
        )

    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Format and customize response
    response = response.replace("YouChat", "Jarvis")
    response = response.replace("large language model", "AI Assistant")
    response = response.replace("from You.com.", "Created by Prasanna")

    return response


# Test the function
print(llm2("What is AI?"))
