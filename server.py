"""Serve the emotion detection course web application."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

APP = Flask(__name__)


@APP.route("/")
def index():
    """Render the supplied course interface."""
    return render_template("index.html")


@APP.route("/emotionDetector")
def detect_emotion():
    """Analyze the submitted text and format the detected emotion scores."""
    result = emotion_detector(request.args.get("textToAnalyze", ""))
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
