def area_calculator():
    print ("Hello, and welcome!")
    input_ = input("What shape do you want to calculate the area of?")

    if input_ == "square":
        length = int(input("What is the side length?"))
        area = length ** 2

        print ('The area of the ' + input_ + ' is ' + str(area))

    elif input_ == "rectangle":
        length = int(input("What is the length?"))
        width = int(input("What is the width?"))
        area = length * width

        print ('The area of the ' + input_ + ' is ' + str(area))

    elif input_ == "triangle":
        base = int(input("What is the base?"))
        height = int(input("What is the hieght?"))
        area = base * height / 2

        print ('The area of the ' + input_ + ' is ' + str(area))

    elif input_ == "circle":
        radius = int(input("What is the radius?"))
        pi = int(3.14159265359)
        area = pi * radius ** 2

        print ('The area of the ' + input_ + ' is ' + str(area))
        
area_calculator()

    
