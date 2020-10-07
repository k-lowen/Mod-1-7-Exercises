def calculate_average(list_of_numbers):
    '''function: finds average of a list of numbers
    parameters: one list
    returns: average of list'''

    
    sum_of_numbers = sum(list_of_numbers)
    average = sum_of_numbers / len(list_of_numbers)

    return average

def main():
    list_of_numbers = [5, 100, 3, 2004, -4]

    print(calculate_average(list_of_numbers))


main()

    

    
