import speech_recognition as sr 
AUDIO_FILE=("audioSample.wav")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contain"+r.recognize_google(audio))
except:
    print("google speech recognization could not understand audio")
