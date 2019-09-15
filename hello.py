# Program 1
# import speech_recognition as sr
# print(sr.__version__)
# r = sr.Recognizer()
# harvard = sr.AudioFile('harvard.wav')
# with harvard as source:
#     audio = r.record(source)

# print(r.recognize_google(audio,show_all=True))


# Program 2
# import speech_recognition as sr
# print(sr.__version__)
# r = sr.Recognizer()
# mic = sr.Microphone()
# # harvard = sr.AudioFile('harvard.wav')
# while True:
#     with mic as source:
#         r.adjust_for_ambient_noise(source)
#         print("Speak Something")
#         audio = r.listen(source)

#     # print(r.recognize_google(audio))
#     if r.recognize_google(audio) == "commander":
#         with mic as source:
#             r.adjust_for_ambient_noise(source)
#             print("What can I do for you?")
#             audio = r.listen(source)
#         print("You just said " + r.recognize_google(audio) + ". I will try to google it")

# Program 3
import pyttsx3
engine = pyttsx3.init()
engine.say('Good morning.')
engine.runAndWait()


# Program 4
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()
while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Speak Something")
        audio = r.listen(source)

    if r.recognize_google(audio) == "commander":
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("What can I do for you?")
            audio = r.listen(source)
        engine.say("You just said " + r.recognize_google(audio) + ". I will try to google it")
        engine.runAndWait()