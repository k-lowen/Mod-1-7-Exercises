def main():
    number = int(input("Enter number: "))

    #calculations

    first_digit = number // 1000
    second_digit = (number - (first_digit *1000)) // 100
    third_digit = (number - (first_digit * 1000) - (second_digit * 100)) // 10
    fourth_digit = (number - (first_digit * 1000) - (second_digit * 100) - (third_digit * 10))

    print("The first number is: ", first_digit)
    print("The second number is: ", second_digit)
    print("The third number is: ", third_digit)
    print("The fourth number is: ", fourth_digit)


main()
