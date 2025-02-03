import streamlit as st
import requests

st.title("📰 Fake News Detector")

st.write("**📰 Breaking News or Misinformation? Instantly Detect Fake News with AI-Powered Verification! 🚀**")

news_text = st.text_area("Enter News Text:", "")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some text for prediction.")
    else:
        
        response = requests.post("http://127.0.0.1:5000/predict", json={"text": news_text})
        prediction = response.json()["prediction"]
        
        
        if prediction == 1:
            st.error("🚨 This news is likely FAKE!")
        else:
            st.success("✅ This news is REAL.")

st.write("**Unveiling the Truth: Instantly Detect and Combat Misinformation with Our Advanced AI-Powered Fake News Detection System**  \n"
         "**Built with Flask and Streamlit for Seamless Performance!**")
