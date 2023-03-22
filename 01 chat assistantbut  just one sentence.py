import openai

openai.api_key = "your api key here"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "type you question here!! "}])
print(completion.choices[0].message.content) # type: ignore
