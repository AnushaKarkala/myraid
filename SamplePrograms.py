
def ReverseNumber():
    number = int(input("Enter a number to be reversed : "))
    reverse = 0

    while (number > 0):
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10
    print("Reversed number is :",reverse)


def IsPrime():
    number = int(input("Enter a number to check if its prime or not : "))
    flag = True
    for i in range(2,number//2):
        if number%i == 0:
            print("Number is not prime")
            flag=False
            break
    if flag:
        print("Number is prime")


def IterativeFibonnaci():
    number = int(input("Enter a number for fibonnaci series : "))
    first = 0
    second = 1

    for i in range(0,number):
        if i < 2:
            result = i
        else:
            result = first + second
            first = second
            second = result
        print(str(result)+"\n")


def recursiveFib():
    first, second = 0, 1
    n = int(input("please give a number for fibonacci series : "))

    def fibonacci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    print("fibonacci series are : ")
    for i in range(0, n):
        print(fibonacci(i))

def FindGreatest():
    n1 = int(input("please give first number : "))
    n2 = int(input("please give second number : "))
    n3 = int(input("please give third number : "))
    if n1 >= n2 and n1 >= n3:
        print(" {n1} is greatest".format(n1=n1));
    if n2 >= n1 and n2 >= n3:
        print(" {n2} is greatest".format(n2=n2));
    if n3 >= n1 and n3 >= n2:
        print("{n3} is greatest".format(n3=n3));

def swapnumbers():
    n1 = int(input("please give first number : "))
    n2 = int(input("please give second number : "))

    n2 = n1+n2
    n1 = n2-n1
    n2 = n2-n1

    print("swapped numbers are :",n1,n2)

def reverseString():
    n1 = input("Enter a string to be reversed: ")
    txt = n1[::-1]
    print(txt)

def addmatrix():
    # Program to add two matrices using nested loop

    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    # result = []

    # iterate through rows
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]

    for r in result:
        print(r)

def sortwords():
    my_str = input("Enter a sentence to be sorted by words: ")

    # my_str = "Hello this Is an Example With cased letters"
    words = [word.lower() for word in my_str.split()]
    words.sort()
    print("The sorted words are:")
    for word in words:
        print(word)

def sortvalues():
    dt = {5: 4, 1: 6, 6: 3}
    sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1], reverse=True)}
    print(sorted_dt)

def countdigits():
    num = int(input("Enter a number whose digits are to be counted: "))
    num = 3452
    count = 0
    while num != 0:
        num //= 10
        count += 1
    print("Number of digits: " + str(count))

def CheckLeap():
    Year = int(input("Enter the year to verify it be leap or not: "))
    if ((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
        print("Given Year is a leap Year");
    else:
        print("Given Year is not a leap Year")


if __name__ == "__main__" :
    ReverseNumber()
    IsPrime()
    IterativeFibonnaci()
    recursiveFib()
    FindGreatest()
    swapnumbers()
    reverseString()
    addmatrix()
    sortwords()
    sortvalues()
    countdigits()






