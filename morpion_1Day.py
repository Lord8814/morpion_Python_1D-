grille = {"1": [" ", " ", " "], 
            "2": [" ", " ", " "],
            "3": [" ", " ", " "]
        }

def afficher_Grille():

    print(f"{grille['1'][0]} | {grille['1'][1]} | {grille['1'][2]}")
    print("---------")
    print(f"{grille['2'][0]} | {grille['2'][1]} | {grille['2'][2]}")
    print("---------")
    print(f"{grille['3'][0]} | {grille['3'][1]} | {grille['3'][2]}")



def placement_Grille(l, c, p):
    if grille[l][c] == (" "):
       grille[l][c] = p


    else:
        print("Cette case est deja utilisé")
        jouer(p)
    
    afficher_Grille()
    if not egalite():
        test_victoire(p)
    
    

def jouer(p):
    
    print("Joueur ", p, "Placer votre pion dans une case vide.")
    l, c = map(int, input(f"Joueur {p}, entrez le numéro de la ligne (1 à 3) et le numéro de la colonne (0 à 2) séparés par un espace: ").split())
    if l > 0 and l < 4 and c >-1 and c<3:
        l=str(l)
        placement_Grille(l, c, p)

    else:
        jouer(p)

def egalite():
    for ligne in grille.values():
        for case in ligne:    
            if case == " ":
                return False
            
    print("Egalité dommage")
    exit()


def test_victoire(p):
    a = []
    X = ["X", "X", "X"]
    O = ["O", "O", "O"]


# test victoire ligne 
    for key in grille:
        a = grille[key]
        if a == X or a == O:
            print("victoire ligne")
            victoire(p)
            
# test victoire diagonal
    if grille["1"][0] == grille["2"][1] == grille["3"][2] != " " or grille["1"][2] == grille["2"][1] == grille["3"][0] != " ":
        print("victoire diago")
        victoire(p)
# test victoire colone
    for i in range(3):
        if grille["1"][i] == grille["2"][i] == grille["3"][i] != " ":
            print("victoire colone")
            victoire(p)

    if p == "X":
        p = "O"
    else:
        p = "X"
    jouer(p)
        


def victoire(p):
    print("Bravo joueur", p ,"tu as gagner")
    exit()

afficher_Grille()
    
jouer("X")


    


