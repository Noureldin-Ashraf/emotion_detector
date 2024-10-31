''' Initiate a Flask app for the Emotion Detector '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' Send the text to the emotion detector package and show the response '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!. "

    return f'''For the given statement, the system response is 'anger': {anger},
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.
        The dominant emotion is {dominant_emotion}.'''

@app.route("/")
def render_index_page():
    ''' Render the Index Page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)