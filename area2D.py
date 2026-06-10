## area of basic 2D shapes
def simple_shapes_area():
    if shape == "rectangle":
        l = int(input("Length:"))
        b = int(input("Breadth:"))
        print("Area:",l*b)
    elif shape == "square":
        s = int(input("Side:"))
        print("Area:",s*s)
    elif shape == "triangle":
        print("1. using height and base.\n2. using three sides.")
        n = int(input("Enter ur choice:"))
        if n==1:
            h = int(input("Height:"))
            b = int(input("Base:"))
            print("Area:",0.5*h*b)
        elif n==2:
            s1 = int(input("Side 1:"))
            s2 = int(input("Side 2:"))
            s3 = int(input("Side 3:"))
            s = (s1+s2+s3)/2
            area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
            print("Area:",area)
        else:
            print("You made the wrong choice son.")
    elif shape == "circle":
        r = int(input("Radius: "))
        print("Area:",2*3.14*r)
    else:                                 
        print("This code doesn't work for this shape.")

print("1.Rectangle\n2.Square\n3.Triangle\n4.Circle")
shape = input("Enter a shape from above: ").lower()
simple_shapes_area()
