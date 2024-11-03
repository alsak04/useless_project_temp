from flask import Flask, render_template
import psutil
import random
from time import sleep

app = Flask(__name__)

# Define a list of moods based on system metrics
MOODS = {
    "cpu": {
        "low": ["Chill", "Relaxed", "Sleepy", "Bored","Keenness","Ethu Mood Pwoli Mood"],
        "medium": ["Focused", "Neutral", "Working","Intense","Alert"],
        "high": ["Excited", "Overwhelmed", "Stressed","Distress"]
    },
    "memory": {
        "low": ["Calm", "Unburdened"],
        "medium": ["Content", "Normal"],
        "high": ["Stretched", "Anxious", "Hogged-Up"]
    },
    "temperature": {
        "low": ["Cool", "Fresh"],
        "medium": ["Warm", "Toasty"],
        "high": ["Sweaty", "Burning Up", "On Fire"]
    }
}

def get_mood():
    # Get system metrics
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    # Use random temperatures for demonstration, or access real temperatures if supported
    temperature = random.uniform(30, 80)

    # Determine CPU mood
    if cpu < 30:
        cpu_mood = random.choice(MOODS["cpu"]["low"])
    elif cpu < 70:
        cpu_mood = random.choice(MOODS["cpu"]["medium"])
    else:
        cpu_mood = random.choice(MOODS["cpu"]["high"])

    # Determine Memory mood
    if memory < 30:
        memory_mood = random.choice(MOODS["memory"]["low"])
    elif memory < 70:
        memory_mood = random.choice(MOODS["memory"]["medium"])
    else:
        memory_mood = random.choice(MOODS["memory"]["high"])

    # Determine Temperature mood
    if temperature < 40:
        temp_mood = random.choice(MOODS["temperature"]["low"])
    elif temperature < 60:
        temp_mood = random.choice(MOODS["temperature"]["medium"])
    else:
        temp_mood = random.choice(MOODS["temperature"]["high"])

    # Generate combined mood status
    mood_data = {
        "cpu_mood": cpu_mood,
        "memory_mood": memory_mood,
        "temp_mood": temp_mood
    }
    return mood_data

@app.route('/')
def home():
    mood = get_mood()
    return render_template('mood.html', mood=mood)

if __name__ == '__main__':
    app.run(debug=True)
