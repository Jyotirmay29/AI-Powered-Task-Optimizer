
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

if __name__ == "__main__":
    mood = input("Enter detected mood or emotion: ")
    suggestions = recommend_task(mood)
    print("Recommended Tasks:", suggestions)
