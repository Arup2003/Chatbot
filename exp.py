#!/usr/bin/python3
import speech_recognition as sr 
import webbrowser, datetime, os
import wikipedia, random, playsound, pyttsx3

#=================================================================================================================================#
#------------------------------                  CHANGED VOICE TO WINDOES SAPI-5)                        -----------------------------#
#=================================================================================================================================#

#This variable is for remembering when someone asks to remember somethig
rem = "nothing"
#This variable means that the program has not run  yet
start_switch = "off"
#This will open the files and make them a list and then close them
question = open("text.txt", "r")
answers = open("textans.txt", "r")
ans = answers.readlines()
data = question.readlines()
question.close()
answers.close()
print(question)
print(answers)

#This defines the trigger speech, and reply
def startup(statement):
	global start
	start = takeCommand().lower()
	if start == "hello rabbit":
		if statement == "off":
			audio.say("Hey there! How may I help you?")
			audio.runAndWait()
			global start_switch
			start_switch = "on"
		else:
			audio.say("Hello")
			audio.runAndWait()

#This is the learning section where the AI will learn 
def learn():
	audio.say("Sorry, I am still learning")
	audio.say("Please help me improve.")
	audio.say("Do you want to help me?")
	audio.runAndWait()
	pop = takeCommand().lower()
	if pop == "yes" or pop == "sure":
		audio.say("Is it question?")
		audio.runAndWait()
		final = takeCommand().lower()
		if final == "yes" or final =='yep' :
			audio.say("What is the answer to your question?")
			audio.runAndWait()
			new_answer = takeCommand().lower()
			if new_answer == "":
				pass
			else:
				question = open("text.txt", "a")
				answers = open("textans.txt", "a")
				question.write(query1)
				answers.write(new_answer+"\n")
				question.close()
				answers.close()
				ans.append(new_answer)
				data.append(query2)
				audio.say("I have added" + new_answer + "as the answer")
				audio.runAndWait()

		else:
			audio.say("Okay alright")
			audio.runAndWait()
			pass
	else:
		audio.say("okay alright")
		audio.runAndWait()
		pass

#This is the listening function
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "Please say that again?"
    return query

#The first while loop is for trigger phrase, the second while loop is for running
Exit = True
while Exit == True:
	audio = pyttsx3.init()
	audio.setProperty('rate',140)
	startup(start_switch)

	#This is for exiting in the start menu
	if start == "exit" or start == "bye" or start == "bye bye" or start == "see you later":
		audio.say("Bye then! See you later!")
		audio.runAndWait()
		Exit = False
		
	#From here running starts
	while start == "hello rabbit":
		#This will not make this while loop repeat if not specified
		repeat = "no"
		
		#This is the main input of the audio
		query = takeCommand().lower()   #lower() is used to keep all your queries in lowercase.

#*************************************************************************************************************************************************************************************************************************************************************************************************************************************************#
		#These are the lists which keep internal questions
		
		Time = ['what time is it', 'what time is it now', 'time','what is the time', 'whats the time', 'tell me the time', 'i need to know the time', 'i wish to know the time']
		Date = ['what date is it', 'what is todays date', 'what is the date', 'what is the date as of today', 'how is the date', 'tell me the date', 'tell me todays date','i wish to know the date', 'i want to know the date', 'i want to know todays date']
		Day = ['what day is it', 'what is the day', 'is it monday', 'is it tuesday', 'is it wednesday', 'is it thursday','is it friday', 'is it saturday', 'is it sunday', 'is it a weekend', 'what is todays day', 'what weekday is it', 'tell me what day is it', 'tell me the day', 'tell me todays day','what is todays day']

#*************************************************************************************************************************************************************************************************************************************************************************************************************************************************#
		
		#query1 is used when reading files and query2 is for normal usage
		query1 = str(query+"\n")
		query2 = str(query)
		
		#This will check is question file if the question exists
		if query1 in data:
			number = data.index(query1)
			audio.say(ans[number])
			audio.runAndWait()

		#Exiting
		elif query2 == "exit" or query2 == "bye bye" or query2 == "see you later" or query2 == "bye":
			audio.say("Bye... See you later")
			audio.runAndWait()
			Exit = False
		
		#This is for the answer to say what Rabbit was asked to remember
		elif query2 == "what did i ask you to remember":
			if rem == "nothing":
				audio.say("You did not ask me to remember anything")
				audio.runAndWait()
			else:
				audio.say("You asked me to remember that..." + rem)
				audio.runAndWait()

		#This will tell the time
		elif query2 in Time:
			current_time = datetime.datetime.now()
			if current_time.hour > 12:
				hour = current_time.hour - 12
				last = "P" + "M"
			else:
				hour = current_time.hour
				last = "A" + "M"
			time = str(hour) + " " + str(current_time.minute) + last
			audio.say(time)
			audio.runAndWait()

		#This will tell the day 
		elif query2 in Day:
			today_day = datetime.datetime.now()
			day = today_day.strftime("%A")
			audio.say("Today is...")
			audio.say(day)
			audio.runAndWait()

		#This will make Rabbit remember something
		elif "remember" in query2:
			rem = query2.replace("remember", "")
			audio.say("Ok, I will remember this")
			audio.runAndWait()

		#This will say the Date
		elif query2 in Date:
			today_date = datetime.datetime.now()
			date = str(today_date.strftime("%B")) + " " + str(today_date.strftime("%d")) + "." + " " + str(today_date.strftime("%Y"))
			audio.say("The date is...")
			audio.say(date)
			audio.runAndWait()

		elif query == 'please say that again?':
			audio.say('Please say that again?')
			repeat = "yes"

#==================================================================================================================================#

#FROM HERE STARTS KEYWORD FINDING

		#This will open any website
		elif "open" in query2:
			opening = query2.replace("open", "")
			audio.say("Opening" + opening)
			audio.runAndWait()
			webbrowser.open(opening+".com")

		#This will repeat what is said
		elif "repeat" in query2:
			audio.say("what do you want me to repeat?")
			repeating = takeCommand().lower()
			audio.say(repeating)
			audio.runAndWait()

		#This will read joke from file and tell
		elif "joke" in query2 or "jokes" in query2:
			joke_file = open("jokes.txt", "r")
			jokes = joke_file.readlines()
			joke_file.close()
			audio.say("So... Here is a joke for you")
			audio.runAndWait()
			audio.say(jokes[random.randint(0, 11)])
			audio.runAndWait()

		#This will show weather on google
		elif "weather" in query2 or "climate" in query2:
			audio.say("Showing you the current weather")
			audio.runAndWait()
			webbrowser.open("https://www.google.com/search?q="+query2+"&oq="+query2+"+&aqs=chrome..69i57j69i59l3j0i433l3j0.6295j1j15&sourceid=chrome&ie=UTF-8")

		#This idk why works and searches the query... If it does not satisfy the above conditions
		elif 'wikipedia' or 'wiki' in query2:
			result = wikipedia.summary(query2, sentences = 2)
			audio.say("According to Wikipedia")
			audio.runAndWait()
			audio.say(result)
			audio.runAndWait()

		else:
			learn()

		if repeat == "yes":
			start = "hello rabbit"
		else:
			start = "end"