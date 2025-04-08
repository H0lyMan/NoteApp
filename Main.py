import os

#   Method responsible for showing only one part of notes
def showone(source):
    for i in range(source.__len__()):
        x = i+1
        print(x.__str__() +". "+ source[i])

#   Method responsible for showing full notes
def shownote(source1, source2):
    for i in range(source1.__len__()):
        x = i+1
        print(x.__str__() +". |"+source1[i]+"| - "+source2[i])

#   Method responsible for adding notes
def add(source1, source2):
    new = input("Add your title: ")
    source1.append(new)
    new = input("Add your note: ")
    source2.append(new)

#   Method responsible for deleting notes
def delete(source1, source2):
    showone(source1)
    inpt = input("Select note number to delete:\n")
    x = int(inpt) - 1
    source1.pop(x)
    source2.pop(x)

#   Method responsible for editing notes
def edit(source1, source2):
    showone(source1)
    inpt1 = input("Choose your note: ")
    x = int(inpt1) - 1
    inpt2 = input("Edit your title: ")
    source1[x] = inpt2
    inpt2 = input("Edit your note: ")
    source2[x] = inpt2

#   Lists declaration
titles = list()
notes = list()

while True:

    print("Welcome in note app \n\t"
          "| if you want to check your notes click 1 |\n\t"
          "| if you want to add your note click 2 |\n\t"
          "| if you want to delete your note click 3 |\n\t"
          "| if you want to edit your note click 4 |\n"
          "Click x if you want to finish")
    inpt = input()

    if inpt == "1":
        os.system('cls')
        shownote(titles, notes)

    elif inpt == "2":
        add(titles, notes)

    elif inpt == "3":
        delete(titles, notes)

    elif inpt == "4":
        edit(titles, notes)

    elif inpt == "X" or "x":
        break