from flask import Flask, render_template, request
import stories

app = Flask(__name__)


@app.route("/")
def home_page():
    '''Home Page with dynamically created form'''

    return render_template(
        "home.html",
        storybook=stories.storybook)


@app.route("/forms", methods=["post"])
def forms_page():
    """ Form to fill out for chosen story"""
    choice = int(request.form["chooser"])
    return render_template(
        "forms.html",
        s_words=stories.storybook[choice].prompts,
        choice=choice)


@app.route("/story", methods=["post"])
def story_page():
    '''Output of the Madlib'''
    choice = int(request.form["choice"])
    answers = request.form
    return render_template(
        "story.html",
        story_gen=stories.storybook[choice].generate(answers))
