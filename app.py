from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.secret_key = "128-046-767"

responses = []
questions = survey.questions


# default landing page for user
@app.route("/")
def start_page():
    return render_template(
        "home.html", survey_title=survey.title, survey_instructions=survey.instructions
    )


@app.route("/begin_survey")
def begin_survey():
    return redirect(url_for("show_question", question_num=1))


@app.route("/questions/<question_num>")
def show_question(question_num):
    # restart form if bad url is passed
    try:
        question_num = int(question_num)
    except ValueError:
        flash(
            "Bad Human. Please start the survey from the beginning.", category="error"
        )
        return redirect(url_for("start_page"))

    # check if user jumps a question
    if question_num != len(responses) + 1:
        print("triggered")
        flash("Bad Human. Do not jump around the survey.", category="warning")
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
        flash("Thank you for completing the survey!", category="success")
        return redirect(url_for("thank_you"))


@app.route("/submit_answer/<int:question_num>", methods=["POST"])
def submit_answer(question_num):
    selected_answer = request.form.get("option")
    responses.append(selected_answer)
    print(responses, question_num)

    # Update server status based on question number
    if question_num == len(questions):
        flash("Thank you for completing the survey!", category="success")
        return redirect(url_for("thank_you"))
    else:
        next_question_num = question_num + 1
        return redirect(url_for("show_question", question_num=next_question_num))


@app.route("/thankyou")
def thank_you():
    survey_title = survey.title
    return render_template("thank.html", survey_title=survey_title)


if __name__ == "__main__":
    app.run(debug=True)
