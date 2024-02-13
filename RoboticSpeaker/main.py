import pyttsx3 as pytxt

if __name__ == '__main__':
    print("welcome to Robotic Speaker 1.1 created by Sharad Patel")
    engine = pytxt.init()
    while True:
     speech = input("Enter whatever you want system to speak: ")

     if speech.lower() == 'exit':
         break

     engine.say(speech)
     engine.runAndWait()
