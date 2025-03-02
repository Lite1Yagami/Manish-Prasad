from flask import Flask, render_template, request
import os

print("Templates directory path:", os.path.join(os.getcwd(), "templates"))

def recommend_exercise(age, bmi, medical_history, fitness_goal, daily_routine, diet):
    """Recommend exercises based on health data."""
    recommendations = []

    # Recommendations based on BMI
    if bmi < 18.5:
        recommendations.append("Light Yoga")
        recommendations.append("Low-impact Aerobics")
    elif 18.5 <= bmi < 25:
        recommendations.append("Moderate Cardio")
        recommendations.append("Strength Training")
    elif 25 <= bmi < 30:
        recommendations.append("Brisk Walking")
        recommendations.append("Cycling")
    else:  # BMI >= 30
        recommendations.append("Water Aerobics")
        recommendations.append("Seated Exercises")

    # Adjustments based on medical history
    if medical_history == "Hypertension":
        recommendations = [rec for rec in recommendations if rec != "High-Intensity Cardio"]
        recommendations.append("Stretching")
    elif medical_history == "Diabetes":
        recommendations.append("Strength Training")
        recommendations.append("Cardio")
    elif medical_history == "Joint Pain":
        recommendations = [rec for rec in recommendations if rec not in ["Running", "Jumping Jacks"]]
        recommendations.append("Swimming")
    elif medical_history == "Heart Disease":
        recommendations = ["Walking", "Low-impact Aerobics", "Yoga"]

    # Adjustments based on fitness goals
    if fitness_goal == "Weight Loss":
        recommendations.append("HIIT")
        recommendations.append("Cycling")
    elif fitness_goal == "Muscle Gain":
        recommendations.append("Weight Lifting")
        recommendations.append("Resistance Training")
    elif fitness_goal == "Endurance Building":
        recommendations.append("Running")
        recommendations.append("Rowing")
    elif fitness_goal == "Flexibility Improvement":
        recommendations.append("Pilates")
        recommendations.append("Yoga")
    
    # Consider daily routine
    if daily_routine == "Sedentary":
        recommendations.append("Walking")
        recommendations.append("Stretching")
    elif daily_routine == "Moderately Active":
        recommendations.append("Jogging")
        recommendations.append("Cycling")
    elif daily_routine == "Highly Active":
        recommendations.append("Strength Training")
        recommendations.append("HIIT")
    
    # Consider diet type
    if diet == "High-Protein":
        recommendations.append("Weight Lifting")
    elif diet == "Vegetarian":
        recommendations.append("Yoga")
    elif diet == "Keto":
        recommendations.append("HIIT")
    elif diet == "Balanced":
        recommendations.append("Moderate Cardio")
    
    # Remove duplicates and return
    return list(set(recommendations))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user inputs from the form
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        medical_history = request.form["medical_history"]
        fitness_goal = request.form["fitness_goal"]
        daily_routine = request.form["daily_routine"]
        diet = request.form["diet"]

        # Get recommendations
        recommendations = recommend_exercise(age, bmi, medical_history, fitness_goal, daily_routine, diet)

        # Render result page with recommendations
        return render_template("result.html", recommendations=recommendations)

    # Render input form page
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
