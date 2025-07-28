
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def detect_text_emotion(text):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)

    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    user_input = input("Enter employee's message: ")
    mood = detect_text_emotion(user_input)
    print("Detected Mood (Text):", mood)
