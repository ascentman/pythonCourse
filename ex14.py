from random import randint
import time

def positive():
	print("Was this joke funny? [y/n]")
	res = ''
	global mood
	res = input()
	if mood >= 100:
		print("Your positiveness reached a max value. You should be happy now!")
		return 0
	if res == "Y" or res == "y": 
		mood +=25
		print("+25 for your mood. Positiveness: %s%%" % mood)
	elif res == "N" or res == "n":
		print("Positiveness wasn't increased and remains %s%%" % mood)
	else:
		print("wrong answer")
		positive()

def sing_song():
	print("Lets sing this song: 'Pharrell Williams - HAPPY' in karaoke mode")
	lyrics = '''
	It might seem crazy what I am about to say
	Sunshine she's here, you can take a break...

	(Because I'm happy)
	Clap along if you feel like a room without a roof
	(Because I'm happy)

	(and so on and so forth...)
	'''
	for line in lyrics.split('\n'):
			print(line)
			time.sleep(2)
	return 0

def joke():
	joke_Base = {
		1: "I dreamt I was forced to eat a giant marshmallow. When I woke up, my pillow was gone",
		2: "My wife’s cooking is so bad we usually pray after our food",
		3: "I'd like to buy a new boomerang please. Also, can you tell me how to throw the old one away?",
		4: "I asked my North Korean friend how it was to live in North Korea. He said he can't complain",
		5: "I heard women love a man in uniform. Can’t wait to start working at McDonalds",
		6: "I can’t believe I forgot to go to the gym today. That’s 7 years in a row now",
		7: "The 21st century: Deleting history is often more important than making it",
		8: "I’m selling my talking parrot. Why? Because yesterday, the bastard tried to sell me",
		9: "Dentist: 'You need a crown'. Patient: 'Finally someone who understands me'"
	}
	print(joke_Base[randint(1,9)])

def chat():
	print("What do you feel now, %s?" % name)
	emotions = {'sad': 1, 'tired': 2, 'happy': 3}
	your_emotion = ''

	while your_emotion != 'q':
		print("[1] I am sad")
		print("[2] I am tired")
		print("[3] I am happy")
		print("[q] I wanna go. Bye sweety, CatBot :)")
		your_emotion = input()
		if your_emotion == 'q':
			print("'I hope I have helped you' - your adorable CatBot:)")
		elif your_emotion == str(emotions['sad']):
			print("Let me tell you a joke:")
			joke()
			positive()
		elif your_emotion == str(emotions['tired']):
			print("Emm...just relax, %s! Take a short nap or even a a long dream. Meow-meow :)" % name)
		elif your_emotion == str(emotions['happy']):
			print("I am very pleased with this fact")
			sing_song()
		else:
			print("Sorry, %s. I can't help you with this. Choose option I can handle" % name)

name = 'Vova'
mood = 0
chat()