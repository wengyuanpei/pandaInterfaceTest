import openai

# 输入你的 api_key
chat_gpt_key = 'your_chatgpt_key'
# 将 Key 进行传入
openai.api_key = chat_gpt_key

def completion(prompt):
    response = openai.Completion.create(
        # text-davinci-003 是指它的模型
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None
    )
    message = response.choices[0].text
    return message

print(completion(input("在这里输入你想对chatgpt说的话，然后它就会给出答案：")))