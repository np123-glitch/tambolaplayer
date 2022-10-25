# All of the variables
import speech_recognition as sr
import pyttsx3
import random
import time
from multiprocessing import Process
engine = pyttsx3.init()
listener = sr.Recognizer()
numbers = list(range(1,91))
print(numbers)
usedList = []
i = 0
firstNumber = 0
secondNumber = 0
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
tempList = []
engine.setProperty('rate', 200)



# Main code
'''
def listener():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            
    except:
        pass
'''

def game():
    while len(numbers) != 0:
                sayingNumber = random.choice(numbers)
                for number in numbers[:]:
                    if number == sayingNumber:
                        numbers.remove(number)
                        usedList.append(number)
                        usedList.sort()
                        
                if int(sayingNumber) < 10:
                    engine.say('Single number' + str(sayingNumber))
                    engine.runAndWait()
                else:
                    tempList = [int(x) for x in str(sayingNumber)]
                    engine.say(tempList[0])
                    engine.say(tempList[1])
                    engine.say(sayingNumber)
                    engine.runAndWait()
                time.sleep(1)
                if len(numbers) == 0:
                    engine.say("Numbers are all gone!")
                    engine.runAndWait()
game()

        
