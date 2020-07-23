import math

def print_area_of_circle(radius):
    pi = math.pi
    area = pi * (radius**2)
    print(f'The area of the circle is {area:.2f}.')

print_area_of_circle(3)

def divides_self(num):
    """ Takes in a positive integer and determines if that number "devides itself"
    input: integer
    output: Boolean

    >>> divides_self(128)
    True
    >>> divides_self(12)
    True
    >>>divides_self(120)
    False
    """
    # Plan
    # What happens in num equals 0
    
    # if num less than or equals 0
    #   return False
    # if less than 10
    #   return True
    #
    if num <= 0:
        return False
    #  split num into individual digits and
    #  loop through each digit in num
    #       if digit does not evenly divide into num or if digit equals 0
    #           return False
    
    for x in range(len(num)):        
        if x % 2 != 0 or x == 0:
            return False 
        else:
            return True
    #  if we get through all the digits 
    #   return True
    print(f"{num} will divide itself!")    
    #Going to need modulo (even division)
    #May need split
    #Need method for isolation each digit in the num

divides_self(128)