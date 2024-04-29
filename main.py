import streamlit as st
import google.generativeai as palm
import os
import time


google_api_key=os.environ['GOOGLE_API_KEY']
palm.configure(api_key=google_api_key)
models = [m for m in palm.list_models() if 'generateText' in
          m.supported_generation_methods]
model = models[0].name

st.markdown("*****Only for memebers of Junto.*****")

st.header("Welcome to BenFrank AI ✨")
with st.container():
   prompt=st.chat_input("Enter prompts")
   
if prompt:
  
  transformer = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0.5,
       # The maximum length of the response
       max_output_tokens=800,
           )
 

  results= transformer.result
  temp="Give a topic for this text: {}"
  prompt_summ=temp.format(results)
  

  summary = palm.generate_text(
    model=model,
    prompt=prompt_summ,
    temperature=0.5,
     # The maximum length of the response
     max_output_tokens=800,
         )
  topic=summary.result
  def stream_data():
      for word in results.split(" "):
         yield word + " "
         time.sleep(0.05)


  with st.container(border=True), st.chat_message("Ben", avatar="✒️"):
      st.markdown("****BenFrank****")
      st.write("Topic: ", topic)
      st.write_stream(stream_data)
      st.write("I hope this helped you.😊✨")
