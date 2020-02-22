#Coded my myself
'''
try:
    x=input("Enter First Name : ")
    y=input("Enter Last Name : ")

    print("Hello Mr.",x+ " " +y,"I love you")
except Exception as ex1:
    print('Error',ex1) '''

#Coded by Sir
try:
    x=input("Enter First Name : ")
    y=input("Enter Last Name : ")

    print("Hello Mr.{0} {1} I love you".format(x,y))
except Exception as ex1:
    print('Error',ex1)