
# Lecture Notes: Regex

## Usecases
- Searching text data for data of a paricular pattern
- Validating Data
- Manipulating Text
- Building patterns to analyze and manipulate text

### Terminology:
**Literal characters**: exact characters
**Metacharacters**: special symbols that represent broader categories

Make sure to always import Regex!
```python
import re
```

## Regex Methods/Functions

- `re.findall(pattern, text)` : retrieves all non-overlaping matches of the pattern and returns a list of all the matches

```python
# Find how many times I used the word "and"
text = 'Hi my name is Dylan, and I like tog and do things and stuff.'

ands = re.findall(r'and', text) # Always start with a raw string : r'<string>' to construct a regex pattern
print(len(ands))

#find all hashtags in post
post = 'I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Coder'

tags = re.findall(r'#\w+', post)
print(tags)

#find all words that start with b and end with the letter e
sentence = 'Abe asked to build a bridge be but he was told "beware of the beehives!".'

bes = re.findall(r'\bb\w*e\b', sentence)
print(bes)

#Finding email addresses
text = 'You can contact me at t.p@gmail.co or travis-p2@codingtemple.com, traviscpeck@email.com'

#username can include letters a-z, digits, _, -, .
#domain can include letters a-z, digits, _, - 
#domain extension needs to be only 2 or 3 character a-z

# when making a pattern, break it up into pieces
emails = re.findall(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', text)
print(emails)
```

- `re.search(pattern, text)` : searches a string for a pattern match, and returns the first occurance as a match object
    - Great for validation
```python
email = input("Enter an email: ")
#email = 'tp@email.com'
found = re.search(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', email)
print(found) # print out the match object
print(found.group()) # use .group() to unpack the match that was found
if found:
    print(f'{found.group()} Is a Valid Email.')
else:
    print('Invalid Email')

#Validating Phone Numbers

# I want to accept a variety of different phone numbers
# 000-000-0000
# 000 000 0000
# 0000000000

number = 'My phone number is: 770 888 1180'
#                         [-\s]       [-\s] also works, just using parens to be different
phone = re.search(r'\d{3}(-|\s)?\d{3}(-|\s)?\d{4}', number)
print(phone)
```

- `re.match(pattern, text)` : Will return a match object if there is a pattern match at the very beginning of the text

```python
text = 'Hello, World'

obj = re.match(r'Hello', text)

print(obj)

# seems useless?
#check to see if a website is secure
#https or http

url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print('This site is secure!')
else:
    print('This site is not very secure!')
```

- `re.split(pattern, text)` splits the text on occurances of the pattern, returns a list

```python
#split on the garbage
text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r"[.,;\s-]+", text)
print(words)

words2 = text.split(r'[.,;]') # Can't use regex with a classic .split() method
print(words2)
```

- `re.sub(pattern, replacer, text)` : replaces occurances of the pattern in a string with a replacer

```python
number = "(770) 888-1180"

# Want to replace anything that isn't a number
formated_number = re.sub(r'\D', '', number)
print(formated_number)

#Anonymous chat
chat = '''
@Yvebee123 : "I think i love regex"
@Travis : "Aren't you married"
@Yvebee123 : "It's just not the same"
@Travis : "They better not see this!"
'''

anon_chat = re.sub(r"@\w+", "@user-anon", chat)
print(anon_chat)
```

### Side Quest - Grouping

```python
pattern = r'(\d+)-(\d+)' # versus [\d+]-[\d+]
text = '123-456'
match = re.search(pattern, text)
if match:
    print(match.group()) # Prints entire match '123-456'
    print("Group 1:", match.group(1))  # Output: Group 1: 123
    print("Group 2:", match.group(2))  # Output: Group 2: 456

```
