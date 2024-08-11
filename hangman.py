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
    print("     I             ( )")
    print("     I")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_3():
    print("     I---------------")
    print("     I              |")
    print("     I             ( )")
    print("     I            --|")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_3():
    print("     I---------------")
    print("     I              |")
    print("     I             ( )")
    print("     I            --|--")
    print("     I")
    print("    I  I")
    print("   I    I")
    print("  I      I")

def stage_4():
    print("     I---------------")
    print("     I              |")
    print("     I             ( )")
    print("     I            --|--")
    print("     I             { }")
    print("    I  I")
    print("   I    I")
    print("  I      I")
    

# list of random words
words_list = ["machinery", "battery", "ethnic", "bell", "formation", "egg", "cut", "infect", "pleasant", "casualty"]

random_index = random.randint(0, len(words_list) - 1)
# Select the word at the random index
random_word = words_list[random_index]
 
# Print the selected word
print("Randomly selected word:", random_word)