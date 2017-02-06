from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import randint
import time

def news():
	searchurl = "http://ukr.net"
	f = urlopen(searchurl)
	html = f.read()
	soup = BeautifulSoup(html, "html.parser")
	for ultag in soup.find_all('ul', {'class': 'top-news-list'}):
		for litag in ultag.find_all('li'):
			print(litag.text)

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
	print("How do you feel now, %s?" % name)
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
			print("Emm...just relax, %s! Take a short nap or even a long dream. Meow-meow :)" % name)
		elif your_emotion == str(emotions['happy']):
			print("I am very pleased with this fact")
			sing_song()
		else:
			print("Sorry, %s. I can't help you with this. Choose option I can handle" % name)

def game():
	count = 0
	choise = ''
	options = ('rock','paper','scissors')
	print("=== ROCK, PAPER, SCISSORS! ===\nHINT: use rock, paper or scissors")
	while choise != 'q':
		comp = options[randint(0,2)]
		print("Your choise:")
		choise = input()
		if choise == comp: 
			print("#Hmm. It's draw. Result:", count)
		elif choise == options[0]:
			if comp == options[2]:
				count += 1
				print("#Great! You won! Result:", count)
			else:
				count -= 1
				print("#Oops! You lose! Result:", count)
		elif choise == options[1]:
			if comp == options[0]:
				count += 1
				print("#Great! You won! Result:", count)
			else:
				count -= 1
				print("#Oops! You lose! Result:", count)
		elif choise == options[2]:
			if comp == options[1]:
				count += 1
				print("#Great! You won! Result:", count)
			else:
				count -= 1
				print("#Oops! You lose! Result:", count)
		else:
			print("uncorrect input. Use only 'paper','rock' or 'scissors'\n")
		print("==== Next round! ==== #For exit press 'q'")

def about_me():
	s = '''    
Hi! My name is CatBot. I was created to help my owner be in a good mood!
I can play with you, tell you jokes, show latest news and even sing a
karaoke, meow-meow :)

v.1.0
----------------------
'''
	print(s)
	return 0

########## Start ###########

print(
'''
　　　　　／＞　 フ 
　　　　　| 　_　 _| 
　 　　　／`ミ _x 彡 
　　 　 /　　　 　 | 
　　　 /　 ヽ　　 ﾉ 
　／￣|　　 |　|　| 
　| (￣ヽ＿_ヽ_)_) 
　＼二つ
'''
	)
print("Hi there, my dear friend! I am CatBot")
name = input("What's your name?\n")
print("nice to meet you, %s!" % name)
mood = 0
choice = ''

while choice != 'q':
    print("\n[1] Enter 1 to check latest Ukrainian news")
    print("[2] Enter 2 to play interesting game")
    print("[3] Enter 3 just to chat with me.")
    print("[a] Enter 'a' About me")
    print("[q] Enter 'q' to quit.")
    
    choice = input("\nWhat would you like to do?\n")
    
    if choice == '1':
        print("\nHere I have collected some latest news:\n")
        news()
    elif choice == '2':
        print("\nHere is ROCK, PARER, SCISSORS game. Enjoy it!\n")
        game()
    elif choice == '3':
        print("\nIf you feel loneliness I'll try to help you, %s?\n" % name)
        chat()
    elif choice == 'q':
        print("\nSee you later!\n")
    elif choice == 'a':
    	about_me()
    elif choice == 'drink':
    	print("I drink only milk and recommend it to you, %s!" % name)
    elif choice == 'damn it':
    	print("God loves you, %s! Be patient!" % name)
    elif choice == "catbot":
    	print("Hello! It's me.")
    elif choice == "sleep":
    	print("Sweet dreams, %s!" % name)
    elif choice == "eat":
    	print("It's the most beautiful thing I like to do, %s!" % name)
    else:
        print("\nI don't understand. please try again.\n")
        
print("Bye, %s!" % name)