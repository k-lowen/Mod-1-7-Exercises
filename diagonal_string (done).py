def diagonal_string(word):
    index = 0
    space = " "
    multiples = 1
    while (index < len(word)):
        print(space* multiples + word[index])
        index += 1
        multiples += 1
        

def main():

    user_input = input("Enter word\n")

    print(diagonal_string(user_input))
    



main()
        
