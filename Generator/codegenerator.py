def code():
    import tkinter as tk
    from tkinter import scrolledtext
    from g4f.client import Client


    def llm_generate_code(prompt):
        """
        Function to interact with an LLM (like GPT-3) to generate Python code based on a prompt.
        """
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": 'user', "content": f"Generate Python code for: {prompt}"}]
        )

        generated_code = response.choices[0].message.content
        return generated_code


    def generate_code():
        """
        Function to generate Python code based on user input.
        """
        prompt = input_text.get("1.0", tk.END).strip()

        if prompt:
            output_label.config(text="Generating code...", fg="blue")
            root.update()

            generated_code = llm_generate_code(prompt)
            code_output.delete("1.0", tk.END)
            code_output.insert(tk.END, generated_code)

            output_label.config(text="Code generated successfully!", fg="green")
        else:
            output_label.config(text="Please enter a valid description!", fg="red")


    # GUI setup using Tkinter
    root = tk.Tk()
    root.title("Python Code Generator")
    root.geometry("800x600")
    root.configure(bg="#282c34")

    # Input Label and Textbox
    input_label = tk.Label(root, text="Enter your code description:", fg="white", bg="#282c34", font=("Helvetica", 12))
    input_label.pack()

    input_text = scrolledtext.ScrolledText(root, width=80, height=10, wrap=tk.WORD, bg="#D3D3D3", fg="#282c34")
    input_text.pack()

    # Generate Button
    generate_button = tk.Button(root, text="Generate Code", command=generate_code, bg="#61dafb", fg="white",
                                font=("Helvetica", 12))
    generate_button.pack()

    # Output Label
    output_label = tk.Label(root, text="", fg="blue", bg="#282c34", font=("Helvetica", 12, "italic"))
    output_label.pack()

    # Generated Code Output Box
    code_output_label = tk.Label(root, text="Generated Python Code:", fg="white", bg="#282c34",
                                 font=("Helvetica", 12, "bold"))
    code_output_label.pack()

    code_output = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, bg="#D3D3D3", fg="#282c34")
    code_output.pack()

    # Run the GUI
    root.mainloop()
