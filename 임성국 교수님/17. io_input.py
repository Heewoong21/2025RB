def reverse(text):
  return text[::-1]
def is_palindrome(text):
  text = ''.join(text.lower() for text in text if text.isalnum())
  return text == reverse(text)

something = input("Enter a text: ")

if is_palindrome(something):
  print("Yes, it is a palindrome")
else:
  print("No, it is not a palindrome")