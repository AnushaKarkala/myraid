
if __name__ == "__main__":

    # a = 'Anusha'
    #
    # dict_new = {}
    #
    # for i in a.lower():
    #   if i in dict_new.keys():
    #         dict_new[i] = dict_new[i] + 1
    #   else:
    #       dict_new[i] = 1
    #
    # print (dict_new)

    ############################Strings in multiple lines ###########

    # name = '''anusha
    # is a good girl.She
    # likes food'''
    # print(name)
    # name = "anusha is a \n good girl\n with no brains"
    # print(name)

    ###################################Bytes######################

    # name = "Anusha"
    # print(name)
    # name =name.encode("utf8")
    # print(name)
    # name =name.decode("utf8")
    # print(name)
    #
    # String1 = "GeeksForGeeks"
    # print(String1[3:12]) ## 3 inclusive and 12 exclusive
    # print(String1[-1]) ## last character

    # Escaping Single Quote
    # String1 = 'I \'m a "Geek"'
    # print("\nEscaping Single Quote: ")
    # print(String1)
    #
    # # Escaping Double Quotes
    # String1 = "I'm a \"Geek\""
    # print("\nEscaping Double Quotes: ")
    # print(String1)
    #
    # ## Escaping Back slashes
    # String1 = "C:\\Python\\Geeks\\"
    # print("\nEscaping Backslashes: ")
    # print(String1)

    # Printing Geeks in HEX
    # String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
    # print("\nPrinting in HEX with the use of Escape Sequences: ")
    # print(String1)
    #
    # # Using raw String to
    # # ignore Escape Sequences
    # String1 = R"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
    # print("\nPrinting Raw String in HEX Format: ")
    # print(String1)

    ######## Strng formatting ##########

    # age = 36
    # txt = "My name is John, I am " + age
    # print(txt) ## TypeError: can only concatenate str (not "int") to str

    # quantity = 3
    # itemno = 567
    # price = 49.95
    #
    # myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    # print(myorder.format(quantity, itemno, price)) ## use format to conct string and numbers
    #
    # myorder = "I want {} pieces of item {} for {} dollars."
    # print(myorder.format(quantity, itemno, price))
    #
    # hello = "The name is:{name} and age is :{age}".format(name = "Anusha",age = 56)
    # print(hello)
    #
    # type = 5
    # result = 'troubling'
    # print('I wondered why the program was %s me. Then it dawned on me it was a %d .' %(result, type))
    #
    # print("This site is {0:f}% securely {1}!!".format(100, "encrypted"))
    # print("My average of this {0} was {1:.2f}%".format("semester", 78.234876))
    # print("The {0} of 100 is {1:b}".format("binary", 100))
    # print("The {0} of 100 is {1:o}".format("octal", 100))
    # print("It is {0:5} degrees outside !".format(40)) ## 5 spaces to left
    # print("{0:^16} was founded in {1:<10}!".format("GeeksforGeeks", 2009)) ## centre align and right align
    #
    # i =1
    # print("{:6d} {:6d} {:6d} {:6d}".format(i, i ** 2, i ** 3, i ** 4)) ## 6 spaces for decimal


    ########## String methods ##########

    # import string
    #
    # result = string.digits
    # print(result)
    #
    # num = '15460'
    # print(num.isdigit()) ## return true

    # ch = "geeksforgeeks"
    # ch1 = "geeks"
    # pos = ch.index(ch1,2,14)
    #
    #
    # print("The first position of geeks after 2nd index : ", end="")
    # print(pos)
    #
    # # ch1 = "gfg"
    # # pos = ch.index(ch1, 2) ## ValueError: substring not found
    #
    # word = 'geeks for geeks'
    # print(word.find('g', 4, 10)) ## 4 inclusive , 10 exclusive ## returns -1 if not found

    # make it suitable for caseless comparison
    # str = "GEEkS 45"
    # print(str.casefold()) ## Implements caseless string matching and converts to lower case (global characters)
    # print(str.upper())
    # print(str.lower())
    # print(str.title()) ## Convert string to title case
    # print(str.capitalize()) ## Converts the first character of the string to a capital (uppercase) letter
    # print(str.swapcase()) ## Converts all uppercase characters to lowercase and vice versa
    # print(str.startswith("ge")) ## Returns “True” if a string starts with the given prefix
    # print(str.endswith("5")) ## Returns “True” if a string ends with the given prefix
    #
    string = "thoeking has the largest army in the entire world the"
    print(string.strip("lshtk")) ## removes "tlhek" if present in start or end in any order.
    ## First character in string should be present in stripped charcters.
    ## Last character in string should be present in stripped charcters.


    # print(string.strip()) ## remove white spaces

    # string = "Welcome everyone to\rthe world of Geeks\nGeeksforGeeks"
    # print(string.splitlines()) ## will exclude line breaks in list items
    # print(string.splitlines(25))
    # print(string.splitlines(True)) ## will include line breaks in list items

    # string = "geeks for geeks"
    # print(string.rstrip('ges')) ## should match exactly.same like strip()
    # #
    # string1 = "Geeks@For@Geeks@Is@For@Geeks"
    # print(string1.partition('@'))
    # print(string1.rpartition('not'))
    # print(string.partition('not'))
    #
    # # print(string.rpartition()) ##  TypeError: rpartition() takes exactly one argument (0 given)
    # # print(string.rpartition("")) ## ValueError: empty separator
    #
    # print(string.rindex('geeks', 0, 10)) ## search between 0 and 10 indices
    # result = string.rfind('tr')
    # print("Substring 'for' found at index :", result)
    # print(string.replace("geeks", "GeeksforGeeks",1)) ## old string,new string,times to be replaced
    #
    # list1 = ['1', '2', '3', '4']
    # s = "-"
    # s = s.join(list1)
    # print(s)
    #
    # print(string.islower())
    # print(string.isupper())
    # print(string1.istitle())
    #
    # string = '\n \n \n'
    # print(string.isspace())
    # string = 'Geeks\nfor\ngeeks'
    # print(string.isspace()) ## return true if all characters are space
    # print(string.isprintable()) ## \n are non printable
    # print(string.isnumeric()) ## fractions,decimals,sub script,super script,roman numerals,unicode,float,int
    # print(string.isidentifier()) ## returns true if valid identifier(with no space,not beginning with number etc)
    # print(string.isdigit())  ## is all are digits
    # print(s.isdecimal())
    # print(string.isalpha()) ## returns true if all are alphabets
    # string = 'Geeks3FORgeeks'
    #
    # print(string.isalnum()) ## return true if string has both alpha and numberic
    # print(string.capitalize()) ## only first alphabet of string
    #
    # string = "geeksforgeeks"
    # print(string.center(45, '#')) ## length of string after padding , padding character.If padding character not specified then empty string by default
    # print(string.count("geeks", 0, 20)) ## start index and end index
    # print(text.endswith('for geeks'))













