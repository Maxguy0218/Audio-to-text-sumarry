#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import streamlit as st


# In[2]:


st.title("Text Summarizer")


# In[3]:


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HEADERS = {"Authorization": "Bearer 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"}


# In[4]:


data = st.text_area("Enter your text here:")


# In[7]:


max_length = st.slider("Select maximum summary length", min_value=10, max_value=800, value=100)


# In[8]:


if st.button("Summarize"):
    payload = {
        "inputs": data,
        "parameters": {"min_length": max_length // 4, "max_length": max_length},
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        output = response.json()[0]
        st.subheader("Summary:")
        st.write(output["summary_text"])
    else:
        st.error("An error occurred during summarization. Please try again.")


# In[ ]:




