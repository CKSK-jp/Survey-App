from flask import Flask, jsonify, redirect, render_template, request, url_for

from surveys import satisfaction_survey

app = Flask(__name__)

responses = []


# default landing page for user
@app.route("/")
def story_selection():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    return render_template(
        "home.html", survey_title=survey_title, survey_instructions=survey_instructions
    )


@app.route("/questions/<question_num>")
def show_question(question_num):
    question_num = int(question_num)
    questions = satisfaction_survey.questions

    if question_num < len(questions):
        question = questions[question_num]
        question_text = question.question
        choices = question.choices
        print(f"Question: {question_text}, Choices: {choices}")
        print(f"Question #{question_num}")
        return render_template(
            "questions.html",
            question_num=question_num,
            question_text=question_text,
            choices=choices,
        )
    else:
        return render_template("error.html", message="Invalid question number")


@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    question_num = int(request.form.get("question_num"))
    selected_answer = request.form.get("selected_answer")
    # Process the submitted answer as needed
    responses.append(selected_answer)
    print(responses)

    # Redirect to the next question or a thank-you page
    if question_num >= len(satisfaction_survey.questions):
        return jsonify(
            {
                "status": "survey_completed",
                "message": "Thank you for completing the survey!",
            }
        )
    else:
        return jsonify(
            {"status": "success", "message": "Answer submitted successfully."}
        )


if __name__ == "__main__":
    app.run(debug=True)
