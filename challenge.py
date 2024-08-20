# Task 1
numbersList = [int(input("Enter an integer: ")) for i in range(8)]
sum = 0
for number in numbersList:
    sum += number
print(f"Sum: {sum}")

# Task 2
booksList = ("Siku Njema", "The Mom Test", "Tales of an Economic Hitman", "Animal Farm", "Chozi la Heri")
for book in booksList:
    print(book)

# Task 3
name = input("What's your name? ")
age = input("How old are you? ")
color = input("What's your favorite color? ")
infoDict = {
    "name": name,
    "age": age,
    "favourite color": color
}
print(infoDict)

# Task 4
set1 = {int(input("Enter an integer for the first set: ")) for i in range(5)}
set2 = {int(input("Enter an integer for the second set: ")) for i in range(5)}
intersectionSet = set1 & set2
print(f"First set: {set1}")
print(f"Second set: {set2}")
print(f"Common numbers: {intersectionSet}")

# Task 5
listOfWords = ["one", "phone", "book", "three", "nine"]
listOfOddWords = []
for word in listOfWords:
    if len(word) % 2 == 1:
        listOfOddWords.append(word)
print(listOfOddWords)