# Sentiment Analysis for Text Documents

This project is a sentiment analysis application built with Python and Streamlit. It uses the Natural Language Toolkit (NLTK) to analyze the sentiment of text documents.

## Features

- Upload a text document for analysis
- Preview the uploaded document
- Analyze the sentiment of the document
- Display the sentiment score on a meter
- Label the sentiment as Very Positive, Positive, Neutral, Negative, or Very Negative

## How to Run

1. Clone this repository.
2. Install the required Python packages:
`pip install streamlit nltk`
3. Run the application:
`streamlit run app1.py`
## Code Overview

The main functions in the code are:

- `main`: The main function that runs the Streamlit application.
- `analyze_sentiment`: This function takes a text string as input and returns a sentiment score using NLTK's SentimentIntensityAnalyzer.
- `get_sentiment_label`: This function takes a sentiment score as input and returns a label (Very Positive, Positive, Neutral, Negative, Very Negative) based on the score.
- `display_sentiment_meter`: This function takes a sentiment score as input and displays a sentiment meter using Streamlit's slider component.

| Sentiment Score Range | Sentiment Label |
|-----------------------|-----------------|
| `> 75`                | Very Positive   |
| `35 - 75`             | Positive        |
| `-75 to < 0`          | Very Negative   |
| `-35 to -75`          | Negative        |
| `-35 to 35`           | Neutral         |

## Contributions

Contributions to this project are welcome. Please open an issue or submit a pull request on [GitHub](https://github.com).
