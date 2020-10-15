invalid_input = True

print ('░█████╗░██████╗░███████╗░█████╗░')
print ('░█████╗░██████╗░███████╗░█████╗░')
print ('██╔══██╗██╔══██╗██╔════╝██╔══██╗')
print ('███████║██████╔╝█████╗░░███████║')
print ('██╔══██║██╔══██╗██╔══╝░░██╔══██║')
print ('██║░░██║██║░░██║███████╗██║░░██║')
print ('╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝')

def area_calculator():
    print ("Hello, and welcome!")
    input_ = input("What shape do you want to calculate the area of?")
    
    if input_ == "square":
        length = int(input("What is the side length?"))
        area = length ** 2

        print ('The area of the ' + input_ + ' is ' + str(area))

        invalid_input = False

    elif input_ == "rectangle":
        length = int(input("What is the length?"))
        width = int(input("What is the width?"))
        area = length * width

        print ('The area of the ' + input_ + ' is ' + str(area))

        invalid_input = False

    elif input_ == "triangle":
        base = int(input("What is the base?"))
        height = int(input("What is the hieght?"))
        area = base * height / 2

        print ('The area of the ' + input_ + ' is ' + str(area))

        invalid_input = False

    elif input_ == "circle":
        radius = int(input("What is the radius?"))
        pi = int(3.14159265359)
        area = pi * radius ** 2

        print ('The area of the ' + input_ + ' is ' + str(area))

        invalid_inputinput = False
        
    else:
        print ('Invalid')

        invalid_inputinput = False

while invalid_input:
        
    area_calculator()

    
