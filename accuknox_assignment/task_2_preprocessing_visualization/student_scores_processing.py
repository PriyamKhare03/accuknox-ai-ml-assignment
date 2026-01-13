#Task 2
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def fetch_student_score(url=None):
  response = requests.get(url)
  data = response.json()
  return data

# ASSUMPTION
# Normally data should come form the API but in this case i dont find any PLI for student score.
# I created the custom dataset(messy) for this then process it and visualize it.

raw_student_data = [
    {"name": " Alice ", "score": "85"},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": "92"},
    {"name": "David", "score": -10},
    {"name": "Eva", "score": "73"},
    {"name": "Frank", "score": None},
    {"name": "Grace ", "score": "95"},
    {"name": "Hannah", "score": 81},
    {"name": "Ian", "score": "77"},
    {"name": "Jane", "score": 84},
    {"name": "Kyle", "score": "invalid"},
    {"name": "Laura", "score": 91},
    {"name": "Mike", "score": "75"},
    {"name": "Nina", "score": 83},
    {"name": "Oscar", "score": 187},
    {"name": "Paula", "score": "94"},
    {"name": "Quinn", "score": 80},
    {"name": "Rachel", "score": "79"},
    {"name": "Sam", "score": 86},
    {"name": "Tina", "score": "90"},
    {"name": "Uma", "score": 72},
    {"name": "Victor", "score": "68"},
    {"name": "Wendy", "score": None},
    {"name": "Xavier", "score": "82"},
    {"name": "Yara", "score": 89},
    {"name": "Zack", "score": "74"},
    {"name": "Amy", "score": 93},
    {"name": "Brian", "score": "70"},
    {"name": "Cathy", "score": "85"},
    {"name": "Derek", "score": 88}
]


def preprocess_student_data(raw_data):
    cleaned_data = []

    for student in raw_data:
        name = student.get("name", "").strip()
        score = student.get("score")

        try:
            score = int(score)
        except (TypeError, ValueError):
            continue

        if 0 <= score <= 100:
            cleaned_data.append({
                "name": name,
                "score": score
            })

    return cleaned_data


def calculate_average(scores):
    total = sum(student["score"] for student in scores)
    return total / len(scores)


def visualize_scores(scores):
    names = [s["name"] for s in scores]
    values = [s["score"] for s in scores]

    plt.figure(figsize=(14, 7))
    plt.bar(names, values)
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Student Test Scores (After Preprocessing)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    #fetch student score from API is comment out
    #raw_student_data = fetch_student_scores()

    raw_data = raw_student_data
    cleaned_data = preprocess_student_data(raw_data)

    avg = calculate_average(cleaned_data)
    print(f"Average Score (Cleaned Data): {avg}")

    visualize_scores(cleaned_data)
