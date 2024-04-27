# import pprint
# import google.generativeai as palm
# import os
# import time

# google_api_key=os.environ['GOOGLE_API_KEY']
# palm.configure(api_key=google_api_key)
# models = [m for m in palm.list_models() if 'generateText' in
#           m.supported_generation_methods]
# model = models[0].name
# print(model)
# prompt = input("Prompt:")
# print("Generating",end="")
# for i in range(5):
#   time.sleep(0.5)
#   print(".",end="")
  
# print("")
# print("")

# time.sleep(1)

# if "your name" in prompt:
#       print("My name is BenFrank.")
# else:
#       completion = palm.generate_text(
#       model=model,
#       prompt=prompt,
#       temperature=0.1,
#     # The maximum length of the response
#       max_output_tokens=800,
#         )
#       print("Ans:",completion.result)

# print("")
# print("")

# print("Exiting", end="")
# for j in range(5):
#   time.sleep(1.5)
#   print(".",end="")

# print("")
# print("Exited successfully")


import streamlit as st
import google.generativeai as palm
import os
import time
import numpy as np
import pandas as pd

google_api_key=os.environ['GOOGLE_API_KEY']
palm.configure(api_key=google_api_key)
models = [m for m in palm.list_models() if 'generateText' in
          m.supported_generation_methods]
model = models[0].name

st.write("Only for memebers of Junto")

st.header("Welcome to BenFrank AI ✨")
with st.container():
   prompt=st.chat_input("Enter prompts")
   
if prompt:
  if "your name" in prompt:
    st.write("My name is BenFrank.")
  else:
   completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0.5,
       # The maximum length of the response
       max_output_tokens=800,
           )
   results= completion.result
   def stream_data():
      for word in results.split(" "):
         yield word + " "
         time.sleep(0.02)



   with st.chat_message("Ben"):
       st.write("BenFrank")
       st.write_stream(stream_data)