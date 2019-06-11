num = 10

def show():
    global num # makes use of same container as in main function
                # global function is used where we need to read
                   # or write the property of a main function
    num=num%3
    print(">>1. num is: ",num)

show()
print(">>2. num is : ",num)

#use case: cart