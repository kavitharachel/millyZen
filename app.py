
import os
import openai
import gradio as gr

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_health_advice(symptoms):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a safe and helpful AI health assistant. You do not diagnose or treat, just provide general educational info."},
                {"role": "user", "content": f"I have the following symptoms: {symptoms}. What could be possible causes or home remedies?"}
            ],
            temperature=0.5
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(fn=get_health_advice, inputs="text", outputs="text", title="Healthcare Chatbot")
demo.launch(share=True)
