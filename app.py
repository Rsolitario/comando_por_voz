# pip install pipwin
# pipwin refresh
# pip install SpeechRecognition
# pip install --upgrade speechRecognition
# pip install pyaudio
import webbrowser
import speech_recognition as sr


def verify_microphone():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
            index, name))
verify_microphone()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Asistente en espera")
    audio = r.listen(source=source)

    try:
        text = r.recognize_google(
            audio)
        print(
            'has dicho: {}'.format(text))
    except:
        print(
            "no he podido entender")