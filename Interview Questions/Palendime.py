#how to write palindrome
def palindrome(input):
    revarsedinput = input[::-1]
    if input == revarsedinput:
        print "{} it is palindrome".format(input)
    else:
        print "{} it is not palindrome".format(input)
palindrome("akka")
palindrome("anna")
palindrome("sis")
palindrome("mam")
palindrome("dad")

palindrome("peddu")
palindrome("anjan")

