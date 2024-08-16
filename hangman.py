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
def game(user_attemst):
    userinput = input("To start please enter a letter: ").lower()
    if len(userinput) > 1:
        print("please enter only one chartor ")
        game(num)
    trytest = False  # reset the loop mechanism
    i = 0
    num = 0

    while i <= (len(random_word) - 1):
        if random_word[i] == userinput: 
            print(i)
            print(f"Correct! '{userinput}' is in the word")
            correct_guess[i] = userinput
            print(correct_guess)
            trytest = True  # set to true when a correct input is found
        #else:
            #print(f"Not in letter {i+1}")
        
        i += 1

        # If the loop finishes and no correct guess was found
        if i == len(random_word) and trytest == False:
            print(f"'{userinput}' is not in the word")
            num += 2
            user_attemst += 1
            print(num)
    
    return num  # Return num at the end of the function


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
num = 1
user_attemst = 0
correct_guess = []

random_index = random.randint(0, len(words_list) - 1)
# Select the word at the random index
random_word = words_list[random_index]
 
# Print the selected word
print("Randomly selected word:", random_word)

print("Welcome to hangman!")
# crate list at the lenth of the chosen word 
while len(correct_guess) < len(random_word):
    correct_guess.append('_')
print(num)
try :
    while num < 8:
        print(num)
        num = game(user_attemst)
except TypeError:
    print(num)
