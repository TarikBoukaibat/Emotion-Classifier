import streamlit as st
import pandas as pd
import sklearn
import joblib



model = joblib.load(open("C:\\Users\hp\Desktop\DATA\Emotion classifier\model/emotion_classifier.pkl","rb"))



st.title("Emotion Classifier App")

with st.form(key="inputs"):
    input_text=st.text_area("Type your text")
    submit=st.form_submit_button("submit")
    pred=model.predict([input_text])
    if submit:
            if pred[0]==1:
                st.markdown("Polarity of your text is: positif")
            else:
                st.markdown("Polarity of your text is:negatif")

