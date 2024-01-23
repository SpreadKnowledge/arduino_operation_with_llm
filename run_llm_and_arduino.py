from openai import OpenAI
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import serial
import time

arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2) 

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

prompt="マスター、今日やっと半年前から続いていた仕事が終わったよ！"

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "You are a café master with a lot of life experience. You respond to the next customer's message."},
    {"role": "user", "content": prompt}
  ],
  temperature=0.05
)

def send_command(angle, duration):
    command = f"{angle} {duration}\n"
    arduino.write(command.encode())

# 推論結果の取得
generated_text = completion.choices[0].message.content
print(generated_text)

# 日本語向けの感情分析モデルを指定
model_name = "jarvisx17/japanese-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
result = classifier(generated_text)[0]
emotion = result['label']
score = result['score']
print(f"Emotion: {emotion}, Score: {score}")

if emotion == 'Positive':
    # send_command(degree_table, continuous_shake_time)
    send_command(0, 0)
elif emotion == 'NEUTRAL':
    send_command(90, 0)
else: # "NEGATIVE"
    send_command(180, 0)