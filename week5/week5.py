import random
import pyttsx3
import pandas as pd

chrs = ["Doctor", "Priest", "Teacher", "Bus Driver", "Student", "Fair Maid", "Soldier", "Sailor", "Captain", "sad old woman", "angry farmer"]
verbs = ["threw", "cooked", "cooked for", "composed with", "programmed", "tickeled", "jumped on", "danced with", "played a tune with", "kicked", "programmed"]
objects = ["cat", "table", "joystick", "xbox", "laptop", "window", "house", "flute", "tank", "projector", "spoon", "fork handle", "candle", "dogs paw", "eyeball"]
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("Once upon a time")
for i in range(len(days)):
    r_chr = random.randrange(0, len(chrs))
    r_chr1 = random.randrange(0, len(chrs))
    r_vrb = random.randrange(0, len(verbs))
    r_obj = random.randrange(0, len(objects))
    message = f"The {chrs[r_chr]} {verbs[r_vrb]} the {chrs[r_chr1]} with the {objects[r_obj]} on {days[i]}"
    print(message)
    #engine.say(message)
    # engine.runAndWait()

print("The end")

sli = chrs[2:]
sli = chrs[2:3]

message:str = "<html><body>Hello<b>     world              </b></body><html>"

ib = message.index("<b>")
ibb = message.index("</b>")
between = message[ib + 3:ibb]
cleaned = between.strip()
trad = message[7: 19]
print(trad)
print(sli)

# a dictionary
tune = {"title" : "The TU Dublin Polka", "downloads": 300}
tune["downloads"]

for key in tune.keys():
    print(key + " " + str(tune[key]))


# a list of dictionaries!
tunes = [{"title" : "The TU Dublin Polka", "downloads": 300},
         {"title" : "The Dublin Reel", "downloads": 300},
         {"title" : "The TU Dublin Polka", "downloads": 300}]

tunes_df = pd.DataFrame(tunes)

print(tunes_df.head())

# read a file into a list of strings
with open("data/oneills.abc", 'r', encoding='latin-1') as f:
    lines = f.readlines()

oneills = []
current_tune = None

for line in lines:    
    if line.startswith("X:"):
        # we are in a new tune
        x = int(line[2:]) # retrieve the index number
        current_tune = {"x": x}         
    elif line.startswith("T:"):
        title = line[2:].strip()
        current_tune["title"] = title
    elif line.strip() == "" and current_tune:
        oneills.append(current_tune)
        current_tune = None
    pass

for tune in oneills:
    print(tune)

all_tunes = pd.DataFrame(oneills)

print(all_tunes.head())

amy = {"name" : "Amy", "gamer_tag" : "rose_killer", "high_score": 306, "money": 1000.0}

amy["inventry"] = {"gun", "mallet", "wand", "cat"}

print("Amy: " + str(amy))
print("Inv: " + str(amy["inventry"]))

amy["inventry"].add("mallet")

has_mallet = "mallet" in amy["inventry"]
print(has_mallet)

for key in amy.keys():
    print(key + " " + str(amy[key]))

for vals in amy.values():
    print(vals)

