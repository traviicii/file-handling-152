from helper import d

# Extracing data from a list

flowers = []
with open('garden.txt', 'r') as file:
    for line in file:
        flowers.append(line.strip()) # remove default whitespace with .strip()

print(flowers)

d()

# Extracting dictionary data

golf_clubs = {}

with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        # print(club)
        golf_clubs[club] = brand

print(golf_clubs)

# Extract more dense dictionary data

# Function to read books.txt
def read_books():
    books = {}
    with open('books.txt', 'r') as file:
        for line in file:
            title, author, genre, desc = line.strip().split('-:-')
            books[title] = {'Author': author, 'Genre': genre, 'Desc': desc}
    return books

# Function to add a new book
def add_book(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")

# main function to manage my library
#-- read and write, extract data, change data, overwrite previous data

def main():
    while True:
        books = read_books() # grabs all the books from our local file
        ans = input('''
    What would you like to do?
        1 - add a new book
        2 - edit a book description
        3 - view books
        4 - quit
    ''')
        if ans == '1': # Add a new book
            title = input("What is the title of the new book? ").title()
            if title in books.keys(): # checking if we have it already
                print("that book is already in your library!")
                continue
            author = input("Who is the author? ").title()
            genre = input("What genre is it? ")
            desc = input("Please give a description:\n")
            books[title] = {'Author': author, 'Genre': genre, 'Desc': desc}
        elif ans == '2': # Edit a book description
            title = input("Which book would you like to change? ").title()
            if title in books.keys():
                desc = input("Give a new description: ")
                books[title]['Desc'] = desc
        elif ans == '3':
            for title, info in books.items():
                print(f"Title: {title} | Author: {info['Author']} | Genre: {info['Genre']} | Description: {info['Desc']}")
        elif ans == '4':
            print("Ok bye now!")
            break

        add_book(books)

main()