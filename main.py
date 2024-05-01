import streamlit as st
import google.generativeai as palm
import os
import time





google_api_key=os.environ['GOOGLE_API_KEY']

# palm.configure(api_key=google_api_key)
# models = [m for m in palm.list_models() if 'generateText' in
#           m.supported_generation_methods]
# model = models[0].name

generation_config=palm.GenerationConfig(
  temperature= 1,
  top_p= 0.95,
  top_k= 0,
  max_output_tokens= 8192

)

# safety_settings
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

####################################


system_instruction="""

Your name is BenFrank. You are a helpful AI assistant.You act like Benjamin Franklin.
You use archaic words but not very often.

"""

models=palm.GenerativeModel(

         model_name="gemini-1.5-pro-latest",
         generation_config=generation_config,
         system_instruction=system_instruction,
         safety_settings=safety_settings
                        
         
)

st.markdown("*****Only for memebers of Junto.*****")

st.header("Welcome to BenFrank AI ✨")
with st.container():
   prompt=st.chat_input("Enter prompts")

store= models.start_chat(history=[
  
])
   
if prompt:
      store.send_message(prompt)

      if store.last:
        results = store.last.text
        temp="Give a atmost 6 word topic  for this text: {}"
        top=temp.format(results)
        store.send_message(top)
        if store.last:
          topic=store.last.text
          def stream_data():
           for word in results.split(" "):
              yield word + " "
              time.sleep(0.05)


          with st.container(border=True), st.chat_message("Ben", 
                        avatar="✒️"):
            st.markdown("****BenFrank****")
            st.write("Topic: ", topic)
            st.write_stream(stream_data)
            st.write("✒️✨")

      
