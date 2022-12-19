
beernight = open("log1.txt", "r")
guests = open("guests.log", "w")
hosts = open("hosts.log", "w")

text1 = (": I can do ", ": My yard is available ", " at ")
text2 = " at "
rep = (" ", " ", " ")

for line in beernight:
    for txt1, repl in zip(text1, rep):
        line = line.replace(txt1, repl)
    guests.write(line)


beernight.close()
guests.close()
