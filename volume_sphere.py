def volume_sphere(rad):
    '''function: calculates volume of a sphere
    parameters: user input for one float for radius
    returns: volume of sphere'''

    #calculations
    pi = 3.14159
    volume = (4/3) * pi * (rad ** 3)
    return volume

def main():
    radius = float(input("Please enter the radius of the sphere: "))

    #note that a radius cannot be a negative number

    if (radius < 0):
        print("Please enter a value greater than zero ")

    else:
        print(volume_sphere(radius))
        
main()
