

message = input(">")
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😄",
    ":P": "😛", 
    ";)": "😉",
    ":o": "😮",  
    ":/": "😕",
    ":|": "😐",
    ":*": "😘",
    ":3": "😺",
    ":$": "😳",
    ":@": "😠",
    ":!": "😲",
    }

words= message.split(" ")
output = " "
for word in words:  
    output += emojis.get(word, word) + " "
print(output)  # Print the final output without trailing spaces