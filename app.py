from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.secret_key = "128-046-767"

responses = []
questions = survey.questions


# default landing page for user
@app.route("/")
def start_page():
    survey_title = survey.title
    survey_instructions = survey.instructions
    return render_template(
        "home.html", survey_title=survey_title, survey_instructions=survey_instructions
    )


@app.route("/questions/<question_num>")
def show_question(question_num):
    # restart form if bad url is passed
    try:
        question_num = int(question_num)
    except ValueError:
        flash("Bad Human. Please start the survey from the beginning.")
        return redirect(url_for("start_page"))

    if question_num != len(responses) + 1:
        flash("Bad Human. Do not jump around the survey.")
        return redirect(url_for("show_question", question_num=len(responses) + 1))

    if question_num < len(questions) + 1:
        question = questions[question_num - 1]
        question_text = question.question
        choices = question.choices
        # print(f"Question: {question_text}, Choices: {choices}")
        # print(f"Question #{question_num}")
        return render_template(
            "questions.html",
            question_num=question_num,
            question_text=question_text,
            choices=choices,
        )
    # redirect to thank you if num responses = length of questions
    else:
        flash("Thank you for completing the survey!")
        return redirect(url_for("thank_you"))


@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    question_num = int(request.form.get("question_num"))
    selected_answer = request.form.get("selected_answer")
    # Process the submitted answer as needed
    responses.append(selected_answer)
    print(responses)

    # Update server status based on question number
    if question_num == len(questions):
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


@app.route("/thankyou")
def thank_you():
    survey_title = survey.title
    return render_template("thank.html", survey_title=survey_title)


if __name__ == "__main__":
    app.run(debug=True)
