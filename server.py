from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") 

@app.route("/emotionDetector")
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    
    parts = [
        f"'{key}': {value}"
        for key, value in response.items()
        if key != "dominant_emotion"
    ]
    
    if len(parts) > 1:
        response_text = ", ".join(parts[:-1]) + " and " + parts[-1]
    else:
        response_text = parts[0]

    message = (
        f"For the given statement, the system response is {response_text}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

    return message    
  
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)