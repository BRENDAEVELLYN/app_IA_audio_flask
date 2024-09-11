from gtts import gTTS
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    audio_path = None
    if request.method == 'POST':
        texto = request.form['texto']
        idioma = 'pt'
        tts = gTTS(text=texto,lang=idioma)
        audio_path='static/audio_exemplo.mp3'
        tts.save(audio_path)
    return render_template('index.html',audio_path=audio_path)


app.run()