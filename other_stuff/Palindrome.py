print("""--- This program is to check if the entered word is Palindrome or not.
If the word is palindrome it will return True otherwise you will be prompt
to enter different word---
..........................""")
a = input("Enter some text here: ").lower()
class Palindrome:
	#@staticmethod
	def is_palindrome(word):
		while word != word[::-1]:
		    word = input("No! enter something different: ").lower()
		return True
print(Palindrome.is_palindrome(a))
