import re
from helper import clear

def write_show(shows): # save current list of shows from our local function scope
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

def add_show(shows):
    clear()
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("what is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows) # write to shows file

def read_shows(): # read the shows file and return the list of shows
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

def view(shows):
    clear()
    print("Shows List")
    print('-----------------------')
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

def remove_show(shows):
    view(shows)
    option = int(input("\n\nChoose a number for the show you'd like to remove: "))
    show = shows.pop(option - 1)
    print(f"\n{show['Title']} was sucessfully removed!")
    write_show(shows)


def main():
    while True:
        show_list = read_shows()
        action = input('''
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Quit
''')
        if action == '1':
            add_show(show_list) # function to add a show
        elif action == '2':
            remove_show(show_list) # function to remove a show
        elif action == '3':
            view(show_list) # function to view list of shows
        elif action == '4':
            print("Thanks for using this app!")
            break

main()