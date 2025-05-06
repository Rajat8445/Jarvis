from openai import OpenAI

client = OpenAI(
    api_key="LnKhsBJ4OvT7h-w5wIBggqmrCTMeLSHsak_JIMKk_5cWOt9aajoe2zRtyYYpC0jTlAS3cC13oyT3BlbkFJdMUtzpjH3p6KcIwjZSKgF3cbq-f32zfgRx08GpIyOep8JvF6iixzJ0o_KBNwvr4-8gLHLHPv8A"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "You are a virtual assistant named jarvis skilled in "
        "general tasks like Alexa and Google Cloud "},
        {"role": "user", "content": "what is coding?"},
    ]
)

print(completion.choices[0].message.content)