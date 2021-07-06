file = open(input("Enter file name: "))
count = int()

for line in file:
    if line.startswith("From: "):
        count += 1
        words = line.split()
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
