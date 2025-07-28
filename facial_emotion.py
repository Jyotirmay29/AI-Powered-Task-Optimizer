
from deepface import DeepFace
import cv2

def detect_facial_emotion():
    cap = cv2.VideoCapture(0)
    print("Capturing image from webcam...")
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture image.")
        return None

    result = DeepFace.analyze(frame, actions=['emotion'])
    emotion = result[0]['dominant_emotion']
    print("Detected Emotion (Face):", emotion)
    return emotion

if __name__ == "__main__":
    detect_facial_emotion()
