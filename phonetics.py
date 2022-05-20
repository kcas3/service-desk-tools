# An easy way to have phonetics at work for spottier/bad audio calls

word = input("Please input a word to be translated (all lowercase): ")
word_to_list = list(word)

alphabet = { "a":"Alfa",     "b":"Bravo",    "c":"Charlie",
             "d":"Delta",    "e":"Echo",     "f":"Foxtrot",
             "g":"Golf",     "h":"Hotel",    "i":"India",
             "j":"Juliett",  "k":"Kilo",     "l":"Lima",
             "m":"Mike",     "n":"November", "o":"Oscar",
             "p":"Papa",     "q":"Quebec",   "r":"Romeo",
             "s":"Sierra",   "t":"Tango",    "u":"Uniform",
             "v":"Victor",   "w":"Whiskey",  "x":"X-ray",
             "y":"Yankee",   "z":"Zulu",     "A":"Alfa", 
             "B":"Bravo",    "C":"Charlie",  "D":"Delta", 
             "E":"Echo",     "F":"Foxtrot",  "G":"Golf", 
             "H":"Hotel",    "I":"India",    "J":"Juliett", 
             "K":"Kilo",     "L":"Lima",     "M":"Mike", 
             "N":"November", "O":"Oscar",    "P":"Papa", 
             "Q":"Quebec",   "R":"Romeo",    "S":"Sierra", 
             "T":"Tango",    "U":"Uniform",  "V":"Victor", 
             "W":"Whiskey",  "X":"X-ray",    "Y":"Yankee", 
             "Z":"Zulu",     " ":" ",        "-":"-"
             ".":"." }

for i in word_to_list:
    print(alphabet[i])
