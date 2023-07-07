import streamlit as st
from pygame import mixer

mixer.init()

music = st.file_uploader("Chose a song")

try:
    mixer.music.load(music)
except Exception:
    st.write("Please! Chose a song")

if st.button("play"):
    mixer.music.play()

if st.button("stop"):
    mixer.music.stop()

if st.button("Pause"):
    mixer.music.pause()

if st.button("Resume"):
    mixer.music.unpause()
