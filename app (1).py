from flask import Flask
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

#calling loading api key
load_dotenv()

#configure api call 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")

df=pd.read_csv("qa_data (1).csv")
#text to content
content_text=""
for _,row in df.iterrows():
    content_text+=f"Q:{row['question']}\nA:{row['answer']}\n\n"

def ask_gemini(query):
    prompt = f"""
You are a Q&A assistant.

Answer ONLY using the context below.
If the answer is not presentr,say: No relevant Q&A found.

Content:
{content_text}

Question:{query}

"""
    response=model.generate_content(prompt)
    return response.text.strip()
print("Q & A Chat Bot ")
print("Enter exit get terminate")

while True:
    user_input=input("You :")
    if user_input.lower()=="exit":
        print("Goodbye")
        break
    answer=ask_gemini(user_input)
    print(f"{answer}\n") 