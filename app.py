from os import path
from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import keras
import numpy as np
import librosa

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])





   

  

    

    

    






def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:


             path = 'SER_model.h5'
             loaded_model = keras.models.load_model(path)


             data, sampling_rate = librosa.load(file)
             mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
             x = np.expand_dims(mfccs, axis=1)
             x = np.expand_dims(x, axis=0)
             predictions = loaded_model.predict_classes(x)


             label_conversion = {'0': 'neutral',
                            '1': 'calm',
                            '2': 'happy',
                            '3': 'sad',
                            '4': 'angry',
                            '5': 'fearful',
                            '6': 'disgust',
                            '7': 'surprised'}

             for key, value in label_conversion.items():
                if int(key) == predictions:
                     label = value

             emotion=label
           
             transcript = emotion.upper()

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
