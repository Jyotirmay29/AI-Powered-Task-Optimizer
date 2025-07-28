# Auto-install required packages if missing
import os
import subprocess
import sys

def install_if_missing(package, import_name=None):
    try:
        __import__(import_name or package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure all needed packages are installed
for pkg in [("deepface",), ("opencv-python", "cv2"), ("nltk",), ("scikit-learn",), ("sounddevice",), ("librosa",)]:
    install_if_missing(*pkg)


import tkinter as tk
from tkinter import messagebox
from deepface import DeepFace
import cv2
import sounddevice as sd
import numpy as np
import librosa
import scipy.io.wavfile as wav
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def detect_text_emotion(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def detect_facial_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return "Camera error"
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']

def record_voice(filename="voice_sample.wav", duration=5, fs=44100):
    print("Recording...")
    voice = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    wav.write(filename, fs, (voice * 32767).astype(np.int16))
    print("Recording saved as", filename)
    return filename

def extract_features(filename):
    y, sr = librosa.load(filename)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

def classify_emotion_from_voice(features):
    if features[0] < -50:
        return "sad"
    elif features[0] > 50:
        return "happy"
    else:
        return "neutral"

def recommend_task(emotion):
    tasks = {
        "happy": ["Collaborate with team", "Work on creative tasks"],
        "sad": ["Do light documentation", "Take a short break"],
        "angry": ["Avoid meetings", "Focus on solo tasks"],
        "neutral": ["Proceed with regular assignments"],
        "surprise": ["Note reactions and evaluate"],
        "fear": ["Avoid high-pressure tasks"],
        "disgust": ["Pause or shift task context"],
        "positive": ["Team collaboration", "Start new projects"],
        "negative": ["Light workload", "Wellness break"]
    }
    return tasks.get(emotion.lower(), ["Continue normal routine"])

def analyze_text():
    text = text_entry.get()
    emotion = detect_text_emotion(text)
    tasks = recommend_task(emotion)
    messagebox.showinfo("Text Mood", f"Detected Mood: {emotion}\nRecommended Tasks:\n- " + "\n- ".join(tasks))

def analyze_face():
    emotion = detect_facial_emotion()
    tasks = recommend_task(emotion)
    messagebox.showinfo("Facial Emotion", f"Detected Emotion: {emotion}\nRecommended Tasks:\n- " + "\n- ".join(tasks))

def analyze_voice():
    filename = record_voice()
    features = extract_features(filename)
    emotion = classify_emotion_from_voice(features)
    tasks = recommend_task(emotion)
    messagebox.showinfo("Voice Emotion", f"Detected Emotion: {emotion}\nRecommended Tasks:\n- " + "\n- ".join(tasks))


app = tk.Tk()
app.title("Zidio AI-Powered Task Optimizer")
app.geometry("400x300")

tk.Label(app, text="Enter Employee Message:", font=('Arial', 12)).pack(pady=10)
text_entry = tk.Entry(app, width=50)
text_entry.pack()

tk.Button(app, text="Analyze Text Mood", command=analyze_text).pack(pady=10)
tk.Button(app, text="Analyze Facial Emotion", command=analyze_face).pack(pady=10)
tk.Button(app, text="Analyze Voice Emotion", command=analyze_voice).pack(pady=10)

app.mainloop()
