from g4f.client import Client

def llm2(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": 'Innovatively trains Jarvis Ai Assistant, adept at recognizing nuanced responses, including sarcasm. Implements continuous learning for dynamic interactions. Ensures Jarvis maintains respectful assistance, addressing users as "sir." Expert in refining language nuances, fostering an evolving and adaptable AI for superior user engagement',"content": f"{text}"}]
    )

    x = response.choices[0].message.content
    x = x.replace("YouChat","jarvis")
    x = x.replace("large language model","Ai Assistant")
    x = x.replace("from You.com.","Created by Prasanna")
    return x

print(llm2("Python code for factorial"))