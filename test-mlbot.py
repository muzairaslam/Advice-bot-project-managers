import openai

API_KEY = "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"

openai.api_key = API_KEY

response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "You are an expert project manager with twenty years of experience. Answer the following questions in a concise way or in bullet points"}, # project manager role definition
    {"role": "user", "content": "Plan a project for a time frame of 20 days in event management"}, # question from our application
  ]
)

# get the answer
answer = response.choices[0].message.content # Get the text of the first choice

print(answer)
