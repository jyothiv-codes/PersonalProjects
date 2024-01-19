import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="YOUR-OPENAI-KEY"
)
response=""



with st.form("get_recommendation"):
   
   st.write("What would you like to watch today?")
   search = st.text_input('', '')
   submitted = st.form_submit_button("Submit")
   if submitted:
      
       
       response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[
        {
          "role": "system",
          "content": "You will be provided with a sentence, and you have to recommend movies accordingly. If the sentence is not related to movie recommendation, just say Sorry! I am designed to only give movie recommendations"
        },
        {
          "role": "user",
          "content": search
        }
      ],
      temperature=0.2,
      max_tokens=1000,
      top_p=1
    )
       st.write(response.choices[0].message.content)
        
        
       
  
