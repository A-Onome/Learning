age = int(input("Enter age: "))
if age < 13:
    print ("You are a child")
else:
    if age < 20:
        print("You are a teenager")
    else:
        if age < 30:
            print("You are a millennial")
        else:
            print("You are an adult")