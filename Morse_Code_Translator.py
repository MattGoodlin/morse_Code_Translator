#Matt Goodlin
#Morse Code Translator... Input a word and it will be translated into Morse Code


#Morse Code Dictionary
translator = {
'a' : '.-',
'b' : '-...',
'c' : '-.-.',
'd' : '-..',
'e' : '.',
'f' : '..-.',
'g' : '--.',
'h' : '....',
'i' : '..',
'j' : '.---',
'k' : '-.-',
'l' : '.-..',
'm' : '--',
'n' : '-.',
'o' : '---',
'p' : '.--.',
'q' : '--.-',
'r' : '.-.',
's' : '...',
't' : '-',
'u' : '..-',
'v' : '...-',
'w' : '.--',
'x' : '-..-',
'y' : '-.--',
'z' : '--..',
'1' : '.----',
'2' : '..---',
'3' : '...--',
'4' : '....-',
'5' : '.....',
'6' : '-....',
'7' : '--...',
'8' : '---..',
'9' : '----.',
'0' : '-----',
' ' : ' '
}

#Splitting the message into individual characters so it can be iterated through
def split(word):
	return [char for char in word]

#Matching each split character with it's respecive morse code and returning it as a concatenated string
def translate(split_word):
	message = ''
	for character in split_word:
		morseCodedLetter = translator[character]
		message = message + morseCodedLetter
	return message


#Putting it all together
def main():
	uncodedMessage = input('What would you like to translate?')
	uncodedMessage = uncodedMessage.lower()
	split_word = split(uncodedMessage)
	translatedWord = translate(split_word)

	print(translatedWord)


if __name__ == '__main__':
	main()
