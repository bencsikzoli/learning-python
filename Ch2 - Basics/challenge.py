# Task is to build a program that detects if the given word, string, number is a palingrom or not.
# Script continues to run until we type the word 'exit'

# Create a function to detect if the string is a palindrome or not
def isPalindrome(givenWord):
    if givenWord == givenWord[::-1]:
        return True
    else:
        return False


        # TODO: while 'exit' is not typed
run = True
while (run):
    givenWord = input(
        "What is the word to be checked? Or type 'exit' to quit\n")

    # check for exit
    if givenWord == "exit":
        run = False
        break

    givenWord = givenWord.lower()

    # strip all the spaces and punctuation from the string
    newstr = ""
    for x in givenWord:
        if x.isalnum():
            newstr += x

    print("Palindrome test:", isPalindrome(newstr))
