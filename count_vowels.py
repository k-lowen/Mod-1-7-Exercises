def count_vowels(user_sentence):
    '''function: takes user's sentence and returns how many vowels present
        parameters: string
        return: number of vowels in sentence'''


    number_of_A = user_sentence.count("a")
    number_of_E = user_sentence.count("e")
    number_of_I = user_sentence.count("i")
    number_of_O = user_sentence.count("0")
    number_of_U = user_sentence.count("u")
    total_vowel_sum = number_of_A + number_of_E + number_of_I + number_of_O + number_of_U
    return total_vowel_sum

def main():

    user_sentence = input("Enter your sentence: ")
    user_sentence.lower()

    print(count_vowels(user_sentence))

main()
