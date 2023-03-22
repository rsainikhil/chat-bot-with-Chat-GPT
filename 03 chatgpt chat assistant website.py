import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": ""}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Chat gpt")

demo.launch(share=True)