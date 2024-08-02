
# Opening Files

# Let's create and write our first file
file = open('new_file.txt', 'w')
file.write('Writing to a file from Python!') # using the .write() method to write data to a file
file.close() # this ensures that data gets commited, and keeps your computer from harm

# Overwriting data in a file
file = open('new_file.txt', 'w')
file.write("Overwriting previous data\n")
file.close()

# Adding to a file without overwriting - 'a' (append) mode
file = open('new_file.txt', 'a') # 'a' mode appends to where our last entry left off without overwriting
file.write('Adding to my file with "a" mode!\n')
file.close()

# reading data within files
file = open('new_file.txt', 'r') # reading a file with 'r' mode
# content = file.read()
lines = file.readlines()
file.close()
# print(content)
# print(lines)

#-- with : allows us to open files to a specific code block, and automatically closes the file when the code block is exited

with open('new_file.txt', 'r') as file:
    for line in file:
        print(line.strip()) # remove new line characters \n by default


#------------------------

#-- Storing data from a list

flowers = ["Wysteria", "Sun Flowers", "Orchids", "Marigolds"]

with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower + '\n')

#-- Storing data from a dictionary

clubs = {
    'Driver': 'Cobra',
    'Irons': 'Sirixion',
    'Hybrid': 'Callaway',
    'Putter': 'Ping'
}

#-- looping through a dictionary:  .keys(), .values(), .items()

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f"{club}: {brand}\n")


# Storing data from a nested dictionary
#-- { title : {author: name, genre: name, desc: summary}}

books = {
    'Green Lights' : {"Author": 'Matthew McConaughey', 'Genre': 'Briography', 'Desc': 'This is a really cool book'},
    'Cloud Atlas' : {'Author': 'David Mitchell', 'Genre': 'Sci-Fi', 'Desc': 'I really love this book'},
    'Diary of a Wimpy Kid' : {'Author': 'Jeff Kiney', 'Genre': 'YAF', 'Desc': 'A tale of a wimpy kid...'},
    'Black Flags' : {'Author': 'Joby Ray', 'Genre': 'Nonfiction', 'Desc': 'Potentially, this is a story about pirates?'},
    '1984' : {'Author': 'Geaorge Orwell', 'Genre': 'Fiction', 'Desc': 'Crazy distopyian future stuff'}
}

def add_books(some_books):
    with open('books.txt', 'w') as file:
        for title, info in some_books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")

add_books(books)