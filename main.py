import itertools
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def word_generator():
    print(Fore.RED + '• Username Generator | made by saphars#0037')
    valid = False
    lower = 1
    upper = 3
    lists = ["abcdefghijklmnopqrstuvwxyz0123456789_",
             "abcdefghijklmnopqrstuvwxyz0123456789",
             "abcdefghijklmnopqrstuvwxyz",
             "0123456789"]
    usernames = []
    while not valid:
        word_length = input(f"> How long do you want the words to be?\n"
                            f"  Ex. 1-3, 3, 2, 2-4, 1-5\n"
                            f"> ")
        if "-" in word_length:
            lower = word_length.split("-")[0]
            upper = word_length.split("-")[1]
        else:
            lower = word_length
            upper = word_length
        try:
            lower = int(lower)
            upper = int(upper)
            valid = True
        except ValueError:
            print(f"> Invalid input!")
    valid = False
    list_index = 0
    while not valid:
        char_list = input(f"> 1. A-Z, 0-9, _\n"
                          f"> 2. A-Z, 0-9\n"
                          f"> 3. A-Z\n"
                          f"> 4. 0-9\n"
                          f"> ")
        if char_list in ["1", "2", "3", "4"]:
            valid = True
            list_index = int(char_list) - 1
    for i in range(lower, upper + 1):
        combinations = [''.join(i) for i in itertools.product(lists[list_index], repeat=i)]
        usernames.extend(combinations)
    file_name = input(f"> Where would you like to save these?\n"
                      f"> Enter a file name...\n"
                      f"> ")
    with open(f"{file_name.replace('.txt', '')}.txt", "a") as f:
        for username in usernames:
            f.write(f"{username}\n")
    print(f"> Generated {len(usernames)} different combinations and saved to "
          f"{file_name.replace('.txt', '')}.txt!\n"
          f"> ")


if __name__ == '__main__':
    word_generator()

Y = input('')
print('Y')