import random

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
            '''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    ========='''
    ]
    print (graphic[hangman])
    return

# Définition du start avec une boucle pour rester dans le jeu autant qu'on veut
def start():
    print("Jouons au Pendu")
    while game():
        pass
    scores()
    

# Définition du jeu de ces variables et des mouvements
def game():
    dictionary = [
    "PANGOLIN",
    "SCOLOPENDRE",
    "HIPPOCAMPE",
    "CARCAJOU",
    "FENNEC",
    "MACAQUES",
    "AXOLOTL",
    "CAMELEON",
    "AUTRUCHE",
    "IGUANE",
    "TARENTULE",
    "DAUPHIN",
    "CACATOES",
    "EPAGNEUL",
    "CAMELEON",
    "BALEINE",
    "ELEPHANT",
    ]
    # on choisit le mot avec la fonction choice
    word = random.choice(dictionary)
    word_length = len(word)
    # on met en place les underscores pour les lettres
    clue = word_length * ["_"]
    # Déclaration des différentes variable
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    # boucle sur les essais possible jusqu'a défaite ou mot trouvé
    while (letters_wrong!= tries) and ("".join(clue)!= word ):
        letter = guess_letter()
        if len(letter)== 1 and letter.isalpha():
            # on vérifie que la lettre n'a pas déja été joué
            if letters_tried.find(letter) != -1:
                print ("vous avez déja joué la lettre", letter)
            else :
                letters_tried = letters_tried + letter
                first_index=word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Hé non",letter, " est la mauvaise lettre")
                else: 
                    print("Félicitations", letter, "existe" )
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print ("Faites un autre choix")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Essais : ", letters_tried)

        if letters_wrong == tries:
            print("Fin du jeu")
            print("Le mot était ",word)
            computer_score += 1
        if "".join(clue) == word :
            print("Gagné \o/")
            print( "Le mot était ",word)
            player_score += 1
    return play_again()

def guess_letter():
    print
    letter = input("Devinez le mot mystère : ").upper()
    letter.strip()
    letter.lower()
    print 
    return letter

def play_again():
    answer = input("Voulez vous rejouer ? o/n : ")
    if answer in ("y", "Y", "yes","o", "oui", "OH OUI!"):
        return answer
    else:
        print("Bon ben tant pis bisous")

def scores(): 
    global player_score, computer_score
    print("Meilleurs scores")
    print ("Joueur: ",player_score)
    print ("Ordinatron", computer_score) 

if __name__ == "__main__":
    start()
