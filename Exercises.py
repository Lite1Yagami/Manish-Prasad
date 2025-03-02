from flask import Flask, render_template, request

app = Flask(__name__)

# A set to store unique recommended exercises
unique_exercises = set()

@app.route("/", methods=["GET", "POST"])
def index():
    global unique_exercises

    if request.method == "POST":
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        medical_history = request.form["medical_history"]
        fitness_goal = request.form["fitness_goal"]

        # Example exercise recommendation logic
        recommendations = []
        if fitness_goal == "Weight Loss":
            recommendations.append("Running")
            recommendations.append("Cycling")
        elif fitness_goal == "Muscle Gain":
            recommendations.append("Weightlifting")
            recommendations.append("Resistance Training")
        elif fitness_goal == "Flexibility Improvement":
            recommendations.append("Yoga")
            recommendations.append("Pilates")
        elif fitness_goal == "Endurance Building":
            recommendations.append("Swimming")
            recommendations.append("HIIT")
        else:  # General Fitness
            recommendations.append("Walking")
            recommendations.append("Bodyweight Exercises")

        # Store recommendations in the set
        unique_exercises.update(recommendations)

        return render_template("result.html", recommendations=recommendations)

    return render_template("index.html")

@app.route("/exercise-types", methods=["GET"])
def exercise_types():
    """Endpoint to list all unique exercise types."""
    return {"unique_exercises": list(unique_exercises)}

if __name__ == "__main__":
    app.run(debug=True)
