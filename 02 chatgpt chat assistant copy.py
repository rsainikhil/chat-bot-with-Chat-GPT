import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"] # type: ignore
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")