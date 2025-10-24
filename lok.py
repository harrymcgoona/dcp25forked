# AI Shakespere
# Name: Lok Ching Tam
# Student number: C24385243

import random
import re

def load_abc_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    return lines

def dani(poem):
    poem = ''.join(poem)
    words = re.split(r'[,.!?:;\s]+', poem)

    for i, word in enumerate(words):
        if not word:
            words.pop(i)

    for i in range(len(words)):
        if i < len(words)-1 and words[i] not in model.keys():
            model[words[i]] = [words[i+1]]
        elif i < len(words)-1 and words[i] in model.keys():
            if words[i+1] not in model[words[i]]:
                model[words[i]].append(words[i+1])
        elif i == len(words)-1 and words[i] not in model.keys():
            model[words[i]] = []
    
    return model

raw_lines = load_abc_file('data/shakespere.txt')
lines = [line.strip().lower() for line in raw_lines]


len_poem = 15
len_blank = 2
num_poems = int(len(lines)/len_blank+len_poem)
poems = []
model = {}
for i in range(num_poems):
    if i % (len_poem+len_blank)== 0:
        index = lines[i].strip()
        poem = lines[i+len_blank:i+len_blank+len_poem]
        poems += poem
        model = dani(poem)


def create_model_txt():
    with open("lectures/week6/model.txt", "w") as f:
        for key, val in model.items():
            f.write(f"{key}: {val}\n")

#create_model_txt()



def ai_poet(random_key, lines, words):
    line = 0
    while line < lines:
        word = 0
        while word < words:
            if model[random_key]:
                random_value = random.choice(model[random_key])
                if line == 0 and word == 0:
                    print(f" {random_value.capitalize()}", end='')
                else:
                    print(f" {random_value}", end='')
                random_key = random_value
                word += 1
            else:
                print('.')
                return
        if line == 13:
            print(".")
            return 
        print(",")
        line += 1

random_key = random.choice(list(model.keys()))
ai_poet(random_key, lines=14, words=8)