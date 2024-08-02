from speech_recognition import *
def main():
    r=Recognizer()
    with Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say Something. ")

        audio=r.listen(source)

        try:
            print("You have said: \n "+r.recognize_google(audio))

        except Exception as e:
            print("Error: "+str(e))


if __name__=="__main__":
    main()


