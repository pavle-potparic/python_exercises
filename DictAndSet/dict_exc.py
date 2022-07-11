moj_dict = {}
moj_dict["ime"] = "Pavle"
moj_dict["ime"] = "Veljko"

# print(moj_dict)

imena = ["Marko", "Pera", "Janko"]

if(imena.__contains__("Veljko")):
    imena.remove("Veljko")

if("Veljko" in imena):
    imena.remove("Veljko")

# imena.pop(2)

# print(imena)
number = 0
for ime in imena:
    number = number + 1
    print(ime.ljust(15, ' ') + ime.ljust(len(ime) - number, '*') + ime.ljust(15, '-'))

