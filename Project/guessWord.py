import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


chars = 7
count = 0

while chars >= count:
    word = random.choice(words)
    count +=1
    text = input(f"Guesses Number: rainbow, computer, science, programming''python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks'\n Type Word: ").lower()

    if text == word:
        print(f"Your guessing Word {text.upper()} is  Correct .. ")
        break
    elif chars <= count and text != word:
        print(f"Try Many More Time... Please Try Agiagn Leter: !")
        break
    elif text != word:
        print(f"Your guessing Word {text} Not Correct .. Correct Word Is {word}...")