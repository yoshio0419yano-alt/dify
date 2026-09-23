from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="取得したAPIキー")
res = client.chat.completions.create(
    model="openrouter/free",
    messages=[{"role": "user",
               "content": "自己紹介してください"}])
print(res.choices[0].message.content)
