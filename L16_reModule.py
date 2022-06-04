import re

# Function 	Description
# findall 	Returns a list containing all matches
# search 	Returns a Match object if there is a match anywhere in the string
# split 	Returns a list where the string has been split at each match
# sub 	Replaces one or many matches with a string

text = "The quick brown fox jumps over the lazy dog"
print('text: ', text)

print('re.search("^The.*fox", text): ', re.search("^The.*fox", text))
print('re.search("^The.*fox", text).group(): ',
      re.search("^The.*fox", text).group())
print('re.search("\s", text).start(): ', re.search("\s", text).start())
print('re.search(r"\bq\w+", text).span(): ', re.search(r"\bq\w+", text).span())

print('re.split("\s", text): ', re.split("\s", text))
print('re.split("\s", text, 3): ', re.split("\s", text, 3))

print('re.sub("\s", "-", text): ', re.sub("\s", "-", text))
print('re.sub("\s", "-", text, 4): ', re.sub("\s", "-", text, 4))
print()

text = "the rain in the spain"
print('text: ', text)
print('re.findall("\w*ain", text): ', re.findall("\w*ain", text))
print('re.findall("vain", text): ', re.findall("vain", text))
print()

# Character 	Description 	Example
# [] 	A set of characters 	"[a-m]"
# \ 	Signals a special sequence (can also be used to escape special characters) 	"\d"
# . 	Any character (except newline character) 	"he..o"
# ^ 	Starts with 	"^hello"
# $ 	Ends with 	"planet$"
# * 	Zero or more occurrences 	"he.*o"
# + 	One or more occurrences 	"he.+o"
# ? 	Zero or one occurrences 	"he.?o"
# {} 	Exactly the specified number of occurrences 	"he.{2}o"
# | 	Either or 	"falls|stays"
# () 	Capture and group


# the output will be...

# text:  The quick brown fox jumps over the lazy dog
# re.search("^The.*fox", text):  <re.Match object; span=(0, 19), match='The quick brown fox'>
# re.search("^The.*fox", text).group():  The quick brown fox
# re.search("\s", text).start():  3
# re.search(rq\w+", text).span():  (4, 9)
# re.split("\s", text):  ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# re.split("\s", text, 3):  ['The', 'quick', 'brown', 'fox jumps over the lazy dog']
# re.sub("\s", "-", text):  The-quick-brown-fox-jumps-over-the-lazy-dog
# re.sub("\s", "-", text, 4):  The-quick-brown-fox-jumps over the lazy dog

# text:  the rain in the spain
# re.findall("\w*ain", text):  ['rain', 'spain']
# re.findall("vain", text):  []
