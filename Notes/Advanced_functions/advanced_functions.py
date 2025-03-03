#Alex Anderson

# 1. What is a helper function?
    # Function called inside of a function to complete part of the task

# 2. What is the purpose of a helper function?
    # To make your functions simple

# 3. What is an inner function?
    # A function that is defined inside of another function

# 4. What is the scope of a variable in a function WITH an inner function?
    # A local including the inner function

# 5. Why do we use inner functions?
    # To access to local variables without needing to pass info in parameters
    # To orginize sections of your function

# 6. What is a closure function?
    #A function to store all of the return statements

# 7. Why do we write closure functions?
    # To decrese the number of paramiters

# 8. What is recursion?
    # When you call a function inside of itself

# 9. How does recursion work?
    # Inside of a function it has somthing that causes it to run itself again

# A wrapper function excists to keep the inner function safe fromn the rest of the code

#--------------------------------------------------------------------------------------

def check_input(user_txt):
    try:
        user_txt.isnumeric() == True
    except:
        return True
    else:
        return False

def hello(name):
    if check_input(name) == False:
        print("Please only input letters.")
        return
    else:
        print(f"Hello {name}!")

#user = input("What is your name:\n").strip().capitalize()
#hello(user)

#---------------------------------------------------------

def fun1():
    msg = "This is somthing"
    return msg

def fun2(msg):
    print(msg)

#--------------------------------------------

def fun(a):
    # outer function remembers the value of a

    def adder(b):
        return a + b
    
    return adder #returning the closure

val = fun(10) #call outer & set a

print(val(5)) #call inner function & set b

#------------------------------------------

def end(income):

    def calc(cost, type):
        percent = cost/income * 100
        print(f"Your  {type} is ${cost:.2f} and that is {percent:.0f}")
    
    return calc

def user_input(type):
    return int(input(f"What is your monthly {type}: \n$"))

#income = user_input("income")
#rent = user_input("rent")
#utilites = user_input("utilites")
#transportation = user_input("transportation")

#ready = end(income)

#ready(rent, "rent")
#ready(utilites, "utilites")
#ready(transporation, "transporation")