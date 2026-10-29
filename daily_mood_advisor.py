#ASKING USER FOR NAME, MOOD & ENERGY
name = input("What is your name?")
mood = input("How are you feeling today? (happy/sad/energetic/tired/relaxed):")
energy = int(input("On a scale of 1 to 10, what is your energy level?"))

#ALERT STATEMENT
if energy < 4:
    print("ALERT, energy is extremely low")


#DO SMTH PRODUCTIVE OR TAKE DAY SLOWLY
if energy >= 7:
     print("Energy is high, do something productive!")

else:
    print("Take the day slowly")


#ADVICE FOR DIFFERENT MOODS
if mood == "happy":
    advice = "Keep that positive attitude going!"

elif mood == "sad":
    advice = "Hope things get better soon."

elif mood == "energetic":
    advice = "Make the most of your energy!"

elif mood == "tired":
    advice = "Take a break and get some rest!"

elif mood == "relaxed":
    advice =  "Enjoy some peace and quiet!"

else:
    advice = "Take things one step at a time."


#CURRENT DATE AND TIME
import datetime
timestamp = datetime.datetime.now()

#FINAL REPORT
print("FINAL REPORT")
print("NAME:",name)
print("ENERGY LEVEL:",energy)
print("MOOD:",mood)
print("ADVICE:",advice)
print("CURRENT DATE AND TIME:",timestamp)