import sys
# def difficulty():
    # print("Choose level difficulty:\n1. Easy (5 mistakes)\n2. Midium (3 mistakes)\n3. Hard (1 mistake)")
    # level = int(input())
    # if level == 1:
    #     no_of_tries = 5
    #     # return 5
    # elif level == 2:
    #     no_of_tries = 3
    #     # return         
    # elif level == 3:
    #     no_of_tries = 1
    #     # return 1
    # else:
    #     print("You choosen wrong number.")

    
word = "kamila"
used_letters = []
user_words = []

def find_indexes(word, letter):
    indexes = [] # zresetowac indexes?

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
            # k a m i l a # Działa to w ten sposob
            # 0 1 2 3 4 5

    return indexes

def show_state_of_game():
    print()
    print(user_words)
    
    print("Used Letters:", used_letters)
    print()

def word_init():
    
    for _ in word:
        user_words.append("_")

#def difficult_level
class main_hangman():
    print("Choose level difficulty:\n1. Easy (5 mistakes)\n2. Midium (3 mistakes)\n3. Hard (1 mistake)")
    level = int(input())
    if level == 1:
        no_of_tries = 5
    elif level == 2:
        no_of_tries = 3  
    elif level == 3:
        no_of_tries = 1
    else:
        print("You choosen wrong number.")
        
    
    word_init()
    while no_of_tries != 0:
        print("Tries remaining:", no_of_tries)
        letter = input("Choose a letter: ")
        used_letters.append(letter)
        found_indexes = find_indexes(word, letter)
        
        if len(found_indexes) == 0:
            print("Unfortunatelly that letter does not exist in the word.")
            no_of_tries -= 1
        if no_of_tries == 0:
            print("Game Over!")
            # sys.exit(0)
        else:
            for index in found_indexes:
                user_words[index] = letter
            if "".join(user_words) == word: # Zamienia obraz listy na string
                print("YEA, This is that word!")
                if input("Do you want to play again? yes/no: ") == 'yes':

                    user_words.clear()

                    word_init()
                    
                    # continue
                else:
                    print("See you next time!")
                    exit()
    
    
        show_state_of_game()
main_hangman()
### Gra wyłącza sie na koniec 
# Własciwa walidacja, co podaje uzytkownik, czy litera, czy nie kilka liter na raz, badz cyfry ( try:)
# Nie mozna pozwolic uzytkownikowi wpisywac drugi raz tej samej litery
# Lista słow do odgadniecia zamiast zmiennej words
# slowa z zewnetrznego API lub pliku
# jesli slowo bylo w grze nie pozwalamy aby ponownie sie wybralo
### restart gry po wylaczeniu czy chcesz zagrac jeszcze raz
### sztywna liczba szans, poziomy trudnosci z 3/5 i 1 szansa
