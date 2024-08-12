import random

def stage_1():
    print("     I---------------")
    print("     I              |")
    print("     I")
    print("     I")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_2():
    print("     I---------------")
    print("     I              |")
    print("     I              O")
    print("     I")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_3():
    print("     I---------------")
    print("     I              |")
    print("     I              O")
    print("     I             ( ")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_4():
    print("     I---------------")
    print("     I              |")
    print("     I              O")
    print("     I             ( )")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_5():
    print("     I---------------")
    print("     I              |")
    print("     I              O")
    print("     I             ( ) ")
    print("     I              |")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_6():
    print("     I---------------")
    print("     I              |")
    print("     I              O")
    print("     I             ( )")
    print("     I              |")
    print("     I             /")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_7():
    print("     I---------------")
    print("     I              |")
    print("     I              O ")
    print("     I             ( )")
    print("     I              |")
    print("     I             / \ ")
    print("    I  I")
    print("   I    I")
    print("  I      I")



# list of random words
machinery = ["m","a","c","i","n","e","r","y"]
battery = ["b", "a", "t", "t", "e", "r", "y"]
ethnic = ["e", "t", "h", "n", "i", "c"]
bell = ["b", "e", "l", "l"]
formation = ["f", "o", "r", "m", "a", "t", "i", "o", "n"]
egg = ["e", "g", "g"]
cut = ["c", "u", "t"]
infect = ["i", "n", "f", "e", "c", "t"]
pleasant = ["p", "l", "e", "a", "s", "a", "n", "t"]
casualty = ["c", "a", "s", "u", "a", "l", "t", "y"]
# all the words avalibkle for random picking 
words_list = [machinery, battery, ethnic, bell, formation, egg, cut, infect, pleasant, casualty]
#number of tries 
num = 0
correct_guess = []
random_index = random.randint(0, len(words_list) - 1)
# Select the word at the random index
random_word = words_list[random_index]
 
# Print the selected word
print("Randomly selected word:", random_word)

print("Welcome to hangman!")
userinput = input("To start please enter a letter:")
while num < 8:
    i = 0
    while i <= (len(random_word) -1):
        if i == userinput: 
            print(f"correct '{userinput}' is in the word")
            correct_guess.insert(i, userinput)
        else: 
            print(f"'{userinput}' is not in the word")