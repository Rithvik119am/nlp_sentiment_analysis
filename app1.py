import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer

def main():
    st.title("Sentiment Analysis for Text Documents")
    uploaded_file = st.file_uploader("Upload a text document", type=['txt'])
    if uploaded_file is not None:
        file_contents = uploaded_file.read().decode("utf-8")
        st.markdown("### Document Preview")
        st.write(file_contents)
        
        if st.button("Analyze Sentiment"):
            sentiment_score = analyze_sentiment(file_contents)
            st.table({
                        'Sentiment Score Range': ['75-100', '35 - 75', '-35 to 35', '-35 to -75', '-75 to -100'],
                        'Sentiment Label': ['Very Positive', 'Positive', 'Neutral', 'Negative','Very Negative' ]
                        }
                    )
            st.markdown("### The Sentiment Meter")
            display_sentiment_meter(sentiment_score)
            sentiment_label = get_sentiment_label(sentiment_score)
            st.write(f"## The sentiment of the text is: {sentiment_label}")

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def get_sentiment_label(sentiment_score):
    if sentiment_score['compound'] > 0.75:
        return "Very Positive"
    elif sentiment_score['compound'] > 0.35:
        return "Positive"
    elif sentiment_score['compound'] < -0.75:
        return "Very Negative"
    elif sentiment_score['compound'] < -0.35:
        return "Negative"
    else:
        return "Neutral"

def display_sentiment_meter(sentiment_score):
    if sentiment_score['compound'] > 0.35:
        st.slider("", -100, 100,int(sentiment_score['compound']*100))
    elif sentiment_score['compound'] > 0.75:
        st.slider("", -100, 100, int(sentiment_score['compound']*100))
    elif sentiment_score['compound'] < -0.75:
        st.slider("", -100, 100, int(sentiment_score['compound']*100))
    elif sentiment_score['compound'] < -0.35:
        st.slider("", -100, 100, int(sentiment_score['compound']*100))
    else:
        if sentiment_score['neg'] >sentiment_score['pos']:
            st.slider("", -100, 100, int(-sentiment_score['compound']*25))
        else:
            st.slider("", -100, 100, int(sentiment_score['compound']*25))
if __name__ == "__main__":
    main()
