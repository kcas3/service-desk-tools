# An easy way to have phonetics at work for spottier/bad audio calls

word = input("Please input a word to be translated (all lowercase): ")
word_to_list = list(word)

alphabet = { "a":"Alfa", "b":"Bravo", "c":"Charlie",
             "d":"Delta", "e":"Echo", "f":"Foxtrot",
             "g":"Golf", "h":"Hotel", "i":"India",
             "j":"Juliett", "k":"Kilo", "l":"Lima",
             "m":"Mike", "n":"November", "o":"Oscar",
             "p":"Papa", "q":"Quebec", "r":"Romeo",
             "s":"Sierra", "t":"Tango", "u":"Uniform",
             "v":"Victor", "w":"Whiskey", "x":"X-ray",
             "y":"Yankee", "z":"Zulu", " ":" ", "-":"-" }

for i in word_to_list:
    print(alphabet[i])
