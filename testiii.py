name = input("Please type in a name: ")
year = input("Please type in a year: ")

text = f"Mary is a valiant knight, born in the year {year}. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents."

text = text.replace("Mary", name)

print(text)
