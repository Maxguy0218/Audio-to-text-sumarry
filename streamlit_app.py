#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install streamlit


# In[5]:


pip install pydub


# In[2]:


pip install bert-extractive-summarizer


# In[3]:


import streamlit as st
import os
import speech_recognition as sr
from pydub import AudioSegment


# In[4]:


from summarizer import Summarizer


# In[5]:


def convert_to_wav(audio_path):
    sound = AudioSegment.from_file(audio_path)
    wav_path = os.path.splitext(audio_path)[0] + ".wav"
    sound.export(wav_path, format="wav")
    return wav_path


# In[6]:


def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text


# In[7]:


def generate_summary(text):
    model = Summarizer()
    summary = model(text)
    return summary


# In[8]:


def main():
    st.title("Audio to Text Summarizer")

    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        audio_path = os.path.join("audio_files", uploaded_file.name)
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())
        
        if audio_path.lower().endswith(".mp3"):
            wav_path = convert_to_wav(audio_path)
        else:
            wav_path = audio_path
        
        audio_text = audio_to_text(wav_path)
        summary = generate_summary(audio_text)

        st.subheader("Transcribed Text:")
        st.write(audio_text)

        st.subheader("Summary:")
        st.write(summary)

if __name__ == "__main__":
    main()


# In[ ]:




