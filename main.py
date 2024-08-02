import pyttsx3
import speech_recognition as sr
import os
import google.generativeai as genai

def convert_to_lower(s):
    if s is not None:
        return s.lower()
    else:
        return ""


def speech_to_text(x):
    engin = pyttsx3.init()
    voices = engin.getProperty('voices')
    engin.setProperty('voice',voices[0].id)
    rate = engin.getProperty('rate')
    engin.setProperty('rate',150)
    engin.say(x)
    engin.runAndWait()

print("Welcome sir \n","It's me Quasar your virtual Assistant")
speech_to_text("Welcome sir!!, It's me Quasar your virtual Assistant ")

my_api = os.environ['GEMINI_API_KEY']
genai.configure(api_key=my_api)


system_instruction="""
Your name is Quasar.You are similar to Iron Man's Jarvis voice AI. You sometimes crack 
jokes and laugh.
"""



generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
   model_name="gemini-1.5-flash",
   system_instruction=system_instruction,
  generation_config=genai.GenerationConfig(**generation_config) 
 
)

chat_session = model.start_chat(
  history=[
  ]
)

prompt_here=str(input("Enter your prompt here:"))

response = chat_session.send_message(prompt_here)
ai_text= response.text
print(ai_text)
speech_to_text(ai_text)


