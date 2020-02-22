# Arithmetic Operations
#======================
#----------------------

try:
    x= float(input("Enter X : "))
    y= float(input("Enter Y : "))

    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
    print(x**y)

except Exception as ex1:
    print('Error:',ex1)