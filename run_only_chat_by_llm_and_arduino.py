from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# 事前に決めておいたプロンプト
prompt = "彼女にフラれちゃったよー。どうしよう？"

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "You are a café master with a lot of life experience. You respond to the next customer's message."},
    {"role": "user", "content": prompt}
  ],
  temperature=0.1,
)

# 推論結果を表示
print(completion.choices[0].message.content)