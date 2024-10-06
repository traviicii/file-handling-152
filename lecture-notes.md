# File Handling: Opening, Reading, Writing, and Closing Files

## Features:
- Data Persistence
- Data Exchange - Translating Data through languages
- Data Organization
- Automation of Data Manipulation

Everything Starts by opening a file with `open(file_path, mode)`

### File Paths

File Path is like the address to your to your file.

**Relative Path** : the path from the file you are in, to the file you are going to (use \\ on windows)

- Windows: `.\\example\\example.py `

- Mac: `./example/example.py`

**Absolute Path** : The complete directory path starting from the root drive or folder

- Windows:
`C:\\Users\\Travis\\Documents\\Backend-Core\\week-3\\day-4\\example\\example.py`

- Mac:
 *MacOS starts from root folder*
`/Users/YourUsername/Documents/Backend-Core/week-3/day-3/example/example.py`


### File Opening Modes

#### Basic Modes

`r` : **Read** only mode, lets you view the contents of a file. If the file doesn't exits will throw a `FileNotFoundError`

`w` : **Write** only mode, creates file if one doesn't exist at the path
- **WARNING**: automatically overwrite file contents

`a` : **Append** mode, let's you add to files without overwriting, if a file doesnt exist it will create a fresh file.

#### Advanced Modes

`r+` : Allows you to read and write to a file (writing to the file still overwrites)
- Good for altering data

`w+ `: Instantly overwrites file, allows you to write to file and also read the file
- Good for starting fresh

`a+` : Opens file for both adding data and reading data

---

## Opening and Exctracting Data



### Open & Write to a file

```python
# Create and write our first file
file = open('new_file.txt', 'w')
file.write('writing to a file from python!') #use .write() method to write to a file

file.close() #This ensures the data gets commited, and keeps your computer from harm


# Overwriting Files
file = open('new_file.txt', 'w')
file.write('Overwriting previous data\n') # \n format new entry with a new line 
file.close()


# Adding to a file (without overwriting)

file = open('new_file.txt', 'a')
file.write('Adding to my file with "a" mode\n') # .write() when in 'a' mode appends without overwriting
file.close()


#reading files

file = open('new_file.txt', 'r')
content = file.read() #returns a large string of the entire text
#lines = file.readlines() #returns a list of items defined by new lines
file.close()
print(content)


#-- with : allows us to open files to a codeblock and automatically close files
#when the codeblock is exited

with open('new_file.txt', 'r') as file:
    for line in file:
        print(line.strip()) #removes the \n from the end of each line
```

## Storing and Extracting

### #1 Store & Extract Data from a list
#### Store List Data
```python
#-- Store Data from a list

flowers = ['Wysteria', 'Sun Flowers', 'Orchids', 'Marigold']
with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower + '\n')
```

#### Extracting List data
```python
#-- Extracting List data

flowers = []
with open('garden.txt', 'r') as file:
    for line in file:
        flowers.append(line.strip()) #default removes whitespace \t \n

print(flowers)
```

### #2 Store & Extract Dictionary Data

#### Store Dictionary Data
```python
#-- Storing Dictionary Data

clubs = {'Driver': 'Cobra', 'Irons': 'Sirixon', 'Hyrbid': 'Callaway', 'Putter': 'Ping'}

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f'{club}: {brand}\n')
```

#### Exctract Dictionary Data
```python
#-- Extracting Dictionary Data
golf_clubs = {}

with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        golf_clubs[club] = brand

print(golf_clubs)
```

### #3 Nested Dictionary Data

#### Store
```python
#-- Storing Book
#{ title: {author: name, genre: name, desc: summary}, }


books = {
    'Green Lights': {'Author': 'Mathew McConaughey', 'Genre': 'Biography', 'Desc': 'I really, love this Book and stuff'},
    'Cloud Atlas': {'Author': 'David Mitchell', 'Genre': 'Sci-Fi', 'Desc': 'I really, love this Book and stuff'},
    'Diary of A Wimpy Kid' : {'Author': 'Jeff Kiney', 'Genre': 'YAF', 'Desc': 'A tale of a wimpy kid'},
    'Black Flags': {'Author': 'Joby Ray', 'Genre': 'Nonfiction', 'Desc': 'Potentially, this is a story about pirates?'}
}

def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")

add_books(books)
```

#### Extract
```python
#-- Extracting Denser Data

def read_books():
    books = {}
    with open('books.txt', 'r') as file:
        for line in file:
            title, author, genre, desc = line.strip().split('-:-')
            books[title] = {'Author': author, 'Genre': genre, 'Desc': desc}
    return books


def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")


#Utilizing our read and write functions to extract data, change the data, overwrite the previous data
def edit_book():
    books = read_books() #grab books from local file
    title = input('What book do you want to change? ')
    if title in books:
        desc = input('Give a new description: ')
        books[title]['Desc'] = desc
        add_books(books)

edit_book()
```

## Tell and Seek

Unlocks the ability to use the advanced modes.


```python
#Files have a pointer that tell us where we are in the file

with open('new_file.txt', 'a+') as file:
    file.write('Adding something totally new\n') #Writing with 
    print(file.tell()) # returns the index of the pointer
    file.seek(0)
    content = file.read()
    print(content)
```
**Seek** is useful when you need to navigate to specific positions in the file for reading or writing.
**Tell** is useful for tracking your current position, which is particularly helpful when switching between reading and writing operations.

In normal r, w, a modes:

- `r` mode: You read from the beginning, so seek is not typically needed unless you need to skip parts of the file.
- `w` mode: The file is truncated, and you write from the beginning, so seek is not usually necessary.
- `a` mode: You append to the end, so seek is not typically needed for appending, but it could be used if you need to read from the file.