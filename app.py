import os
from google.genai import Client
import gradio as gr
from dotenv import load_dotenv
from utils.LoadSystemPrompt import load_prompt


load_dotenv()

client = Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    print(model.name)

def generate_cli(user_instruction):
    system_prompt = load_prompt(2)
    
    full_prompt = f"{system_prompt}\n\nUser request: {user_instruction}"
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=full_prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🛠️ CLI Agent - Level 1")
    
    with gr.Column():
        instruction = gr.Textbox(
            label="הוראה אנושית", 
            placeholder="למשל: תציג את כל התהליכים שתופסים הכי הרבה RAM"
        )
        output = gr.Textbox(label="פקודה לייצור", interactive=False)
        submit = gr.Button("ייצר פקודה", variant="primary")

    submit.click(fn=generate_cli, inputs=instruction, outputs=output)

if __name__ == "__main__":
    demo.launch()