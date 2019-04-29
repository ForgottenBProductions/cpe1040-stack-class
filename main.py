from stack import *

#Defs
def test_integers():
    print("int test")
    s = Stack(7)
    s.push(5) 
    t = s.pop() 
    print(t)


def test_floats():
    print("float test")
    s = Stack(2.3) 
    s.push(5.0) 
    t = s.pop() 
    print(t)




def test_strings():
    print("string test")
    s = Stack("")
    s.push("Sharks suck") 
    t = s.pop() 
    print(t)



def test_exception():
    print("exception test")
    s = Stack(5) 
    s.push("Sharks suck") 
    t = s.pop() 
    print(t) 
def safe_test_int_exception():
    print("safe int test")
    s = IntStack()
    s.push(1.0)


def safe_test_int():
    print("safe non int test")
    s = IntStack()
    s.push(5)

if __name__ == '__main__':

    #Exceptions and Errors

     try:
         test_exception() 

     except ValueError: 
         print("exception test value error")


     try:
         test_strings() 

     except ValueError: 
         print("string test value error") 



     try:
         test_integers() 

     except ValueError:
         print("integer test value error") 



     try:
         test_floats() 

     except ValueError:
         print("float test value error")




     try:
         safe_test_nonint() 

     except ValueError:
         print("safe test non int value error") 


     try:
         safe_test_int() 

     except ValueError:
         print("safe test int value error") 
         
