import urllib
def read_text():
	file_location = "E:\Mini-Project\Check Profanity\movie_quotes.txt"

	file = open(file_location)
	contents = file.read()
	file.close()
	
	check_profanity(contents)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	result = connection.read()
	connection.close()

	if("true" in result):
		print("Profanity Alert!!")
	elif("false" in result):
		print("No Bad Words!")
	else:
		print("Couldn't scan the document properly.")

read_text()
