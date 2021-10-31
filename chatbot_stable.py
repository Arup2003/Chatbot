
import speech_recognition as sr 
import webbrowser, datetime, os
import wikipedia, random, playsound
from gtts import gTTS

#=================================================================================================================================#
#------------------------------*V-1.0*-LAST UPDATE: AGAIN BROUGHT BACK THE VOICE AND ACCENTS -------------------------------------#
#=================================================================================================================================#


#This variable is for remembering when someone asks to remember somethig
rem = "nothing"
#This variable means that the program has not run  yet
start_switch = "off"
#This is the default accent
accent = 'en-ph'
#This will open the files and make them a list and then close them
question = open("text.txt", "r")
answers = open("textans.txt", "r")
ans = answers.readlines()
data = question.readlines()
question.close()
answers.close()

#This defines the trigger speech, and reply
def startup(statement):
	global start
	start = takeCommand().lower()
	if start == "hello rabbit":
		if statement == "off":
			speak("Hey there! How may I help you?")
			global start_switch
			start_switch = "on"
		else:
			speak("Hello")

#This is the learning section where the AI will learn 
def learn():
	speak("Sorry, I am still learning")
	speak("Please help me improve.")
	speak("Do you want to help me?")
	pop = takeCommand().lower()
	if pop == "yes" or pop == "sure":
		speak("Is it question?")
		final = takeCommand().lower()
		if final == "yes" or final =='yep' :
			speak("What is the answer to your question?")
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
				speak("I have added" + new_answer + "as the answer")

		else:
			speak("Okay alright")
			pass
	else:
		speak("okay alright")
		pass

#This will make Rabbit speak
def speak(reply):
	audio = gTTS(text = reply,lang = accent) 
	audio.save('voice.mp3') 
	playsound.playsound('voice.mp3')
	os.remove('voice.mp3')

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
	
	startup(start_switch)

	#This is for exiting in the start menu
	if start == "exit" or start == "bye" or start == "bye bye" or start == "see you later":
		speak("Bye then! See you later!")
		Exit = False
		
	#From here running starts
	while start == "hello rabbit":
		#This will not make this while loop repeat if not specified
		repeat = "no"
		
		#This is the main input of the audio
		query = takeCommand().lower()   #lower() is used to keep all your queries in lowercase.

#*************************************************************************************************************************************************************************************************************************************************************************************************************************************************#
		#These are the lists which keep internal questions
		
		Time = ['what\'s the time', 'what time is it', 'what time is it now', 'time','what is the time', 'whats the time', 'tell me the time', 'i need to know the time', 'i wish to know the time']
		Date = ['what date is it', 'what is todays date', 'what is the date', 'what is the date as of today', 'how is the date', 'tell me the date', 'tell me todays date','i wish to know the date', 'i want to know the date', 'i want to know todays date']
		Day = ['what day is it', 'what is the day', 'is it monday', 'is it tuesday', 'is it wednesday', 'is it thursday','is it friday', 'is it saturday', 'is it sunday', 'is it a weekend', 'what is todays day', 'what weekday is it', 'tell me what day is it', 'tell me the day', 'tell me todays day','what is todays day']

#*************************************************************************************************************************************************************************************************************************************************************************************************************************************************#
		
		#query1 is used when reading files and query2 is for normal usage
		query1 = str(query+"\n")
		query2 = str(query)
		
		#This will check is question file if the question exists
		if query1 in data:
			number = data.index(query1)
			speak(ans[number])

		#Exiting
		elif query2 == "exit" or query2 == "bye bye" or query2 == "see you later" or query2 == "bye":
			speak("Bye... See you later")
			Exit = False
		
		#This is for the answer to say what Rabbit was asked to remember
		elif query2 == "what did i ask you to remember":
			if rem == "nothing":
				speak("You did not ask me to remember anything")
			else:
				speak("You asked me to remember that..." + rem)

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
			speak(time)

		#This will tell the day 
		elif query2 in Day:
			today_day = datetime.datetime.now()
			day = today_day.strftime("%A")
			speak("Today is...")
			speak(day)

		#This will make Rabbit remember something
		elif "remember" in query2:
			rem = query2.replace("remember", "")
			speak("Ok, I will remember this")

		#This will say the Date
		elif query2 in Date:
			today_date = datetime.datetime.now()
			date = str(today_date.strftime("%B")) + " " + str(today_date.strftime("%d")) + "." + " " + str(today_date.strftime("%Y"))
			speak("The date is...")
			speak(date)

		elif query == 'please say that again?':
			speak('Please say that again?')
			repeat = "yes"

#==================================================================================================================================#

#FROM HERE STARTS KEYWORD FINDING

		#This will open any website
		elif "open" in query2:
			opening = query2.replace("open", "")
			speak("Opening" + opening)
			webbrowser.open(opening+".com")

		#This will repeat what is said
		elif "repeat" in query2:
			speak("what do you want me to repeat?")
			repeating = takeCommand().lower()
			speak(repeating)

		#This will read joke from file and tell
		elif "joke" in query2 or "jokes" in query2:
			joke_file = open("jokes.txt", "r")
			jokes = joke_file.readlines()
			joke_file.close()
			speak("So... Here is a joke for you")
			speak(jokes[random.randint(0, 11)])

		#This will show weather on google
		elif "weather" in query2 or "climate" in query2:
			speak("Showing you the current weather")
			webbrowser.open("https://www.google.com/search?q="+query2+"&oq="+query2+"+&aqs=chrome..69i57j69i59l3j0i433l3j0.6295j1j15&sourceid=chrome&ie=UTF-8")
		
		#This will change the accent of rabbit
		elif "change" in query2 and "voice" in query2:
			accents = ['en-ph','en-au', 'en-in', 'en-ng', 'en-nz', 'en-ca']
			speak("Ok! Now I will cycle through the accents that I know... If you say. CHANGE. I will go to the next accent")
			stop = True
			while stop == True:
				for accent_number in accents:
					if accent_number == 'en-ca':
						accent = accent_number
						speak("This is the last accent I know")
						speak("Do you want me to speak in this accent or change?")
						change_accent = takeCommand().lower()
				
						if change_accent == "change":
							speak("Okay... Cycling through the accents again")
							stop = True
						else:
							speak("Okay, now I will speak to you in this accent. Seems nice!")
							stop = False
							break
					else:
						stop = False
						accent = accent_number
						speak("Do you want me to speak in this accent or change?")
						change_accent = takeCommand().lower()
						
						if change_accent == "change":
							speak("Okay, switching to the next accent")
						else:
							speak("Okay, now I will speak to you in this accent. Seems nice!")
							break

		#This idk why works and searches the query... If it does not satisfy the above conditions
		elif 'wikipedia' or 'wiki' in query2:
			result = wikipedia.summary(query2, sentences = 2)
			speak("According to Wikipedia")
			speak(result)

		else:
			learn()

		if repeat == "yes":
			start = "hello rabbit"
		else:
			start = "end"
