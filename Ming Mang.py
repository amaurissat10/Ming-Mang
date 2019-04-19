def newBoard(n):    #Fonction qui va créer une liste à deux dimensions
    list = []
    list.append(firstLine(n))   #Appelle la fonction qui créé la première ligne
    for i in range(0,n-2):
        list.append(middleLine(n))  #Appelle la fonction qui créé la première ligne et l'ajoute n-2 fois
    list.append(lastLine(n))   #Appelle la fonction qui créé la dernière ligne
    return list

def firstLine(n):   #Fonction qui créera uniquement la première ligne
    list = []
    list.append(1)
    for i in range(0,n-1):
        list.append(2)
    return list

def middleLine(n):   #Fonction qui créera uniquement les lignes du milieu
    list = []
    list.append(1)
    for i in range(0,n-2):
        list.append(0)
    list.append(2)
    return list

def lastLine(n):   #Fonction qui créera uniquement la dernière ligne
    list = []
    for i in range(0,n-1):
        list.append(1)
    list.append(2)
    return list

def displayBoard(board,n):  #Procédure qui affiche le plateau de jeu
    for i in range(0,n+1):
        print(i,end="  ")   #Partie qui ajoute le numéro des colonnes
    print("")
    for i in range(0,n):
        print(i+1,end="  ")    #Partie qui affiche le numéro des lignes
        for j in range(0,n):    #Si l'élément à l'emplacement i,j est un 0 on affiche un ".",...
            if board[i][j] == 0:
                element = "."
            elif board[i][j] == 1:
                element = "x"
            elif board[i][j] == 2:
                element = "o"
            print(element,end="  ")
        print("")

def possiblePawn(board,n,player,i,j):   #Fonction qui vérifie si le pion sélectionné par le joueur peut etre sélectionné
    if 0 <= i < n and 0 <= j < n or 0 <= i < n and 0 <= j < n:
        if board[i][j] == player:  #Il faut que le pion soit égal au joueur
            return True
        elif board[i][j] == 0:  #Cas où il n'y a pas de pion
            print("Il n'y a pas de pion ici !")
            return False
        elif board[i][j] != player:  #Cas où le pion sélectionné n'appartient pas au joueur
            print("Ne volez pas de pions au joueur",board[i][j],"!")
            return False
    else:
        return False

def selectPawn(board,n,player): #Fonction qui demande les coordonnées d'un pion déplaçable au joueur
    i = int(input("Entrez le numéro d'une LIGNE contenant un pion déplaçable : "))
    j = int(input("Entrez le numéro d'une COLONNE contenant un pion déplaçable : "))
    i,j = i-1,j-1
    return i,j

def possibleDestination(board,n,i,j,k,l):   #Fonction qui vérifie si le pion sélectionné par le joueur peut etre déplacé à l'endroit entré par le joueur
    if 0 <= k < n and 0 <= l < n:
        if k == i and board[k][l] == 0 or l == j and board[k][l] == 0:
            if i < k:   #Cas où le pion est déplacé de haut en bas
                if k-i == 1:    #Retourne true si le pion est déplacé d'une case
                    return True
                for x in range(i+1,k):  #Sinon vérifie qu'il n'y a aucun pion entre le départ et l'arrivée
                    if board[x][j] != 0:
                        return False
            elif i > k:   #Cas où le pion est déplacé de bas en haut
                if i-k == 1:
                    return True
                for x in range((i-1),k,-1):
                    if board[x][j] != 0:
                        return False
            elif j < l:   #Cas où le pion est déplacé de gauche à droite
                if l-j == 1:
                    return True
                for x in range(j+1,l):
                    if board[i][x] != 0:
                        return False
            elif j > l:   #Cas où le pion est déplacé de droite à gauche
                if j-l == 1:
                    return True
                for x in range((j-1),l,-1):
                    if board[i][x] != 0:
                        return False
            else:
                return False
        else:
            if k != i and l != j:
                print("Vous devez positionner votre pion sur la même ligne/colonne !")
            elif k == i and l == j:
                print("Vous devez déplacer votre pion !")
            elif board[k][l] != 0:
                print("Vous ne pouvez pas positionner de pion là où il y en a déjà un !")
            return False
    else:
        return False

def selectDestination(board,n,i,j): #Fonction qui demande les coordonnées d'un emplacement où déplacer le pion
    k = int(input("Entrez le numéro d'une LIGNE où déplacer le pion : "))
    l = int(input("Entrez le numéro d'une COLONNE où déplacer le pion : "))
    k,l = k-1,l-1
    return k,l

def previewMove(board,n,i,j):   #Fonction qui vérifie que le pion sélectionné peut être déplacé
    if cornersCheck(board,n,i,j) == True:
        print("Vous ne pouvez pas sélectionner le pion ["+str(i+1)+"]/["+str(j+1)+"] car il est bloqué dans un coin.")
        return False
    elif middleCheck(board,n,i,j) == True:
        print("Vous ne pouvez pas sélectionner le pion ["+str(i+1)+"]/["+str(j+1)+"] car il est bloqué.")
        return False
    return True

def move(board,n,player,i,j,k,l):   #Procédure qui déplace le pion
    board[i][j] = 0
    board[k][l] = player

def capture(board,k,l):   #Procédure qui vérifie l'appropriation des pions aux joueurs en fonction des cas
    if l != 0:
        leftCapture(board,k,l)
    if l != n-1:
        rightCapture(board,k,l)
    if k != 0:
        topCapture(board,k,l)
    if k != n-1:
        bottomCapture(board,k,l)

def rightCapture(board,k,l):    #Procédure qui approprie des pions aux joueurs à droite
    if board[k][l+1] != board[k][l] and board[k][l+1] != 0:
        for x in range(l+1,n):
            if board[k][x] == board[k][l]:
                for y in range(x,l,-1):
                    board[k][y] = board[k][l]
            elif board[k][x] == 0:
                break

def leftCapture(board,k,l):    #Procédure qui approprie des pions aux joueurs à gauche
    if board[k][l-1] != board[k][l] and board[k][l-1] != 0:
        for x in range(l-1,-1,-1):
            if board[k][x] == board[k][l]:
                for y in range(x,l):
                    board[k][y] = board[k][l]
            elif board[k][x] == 0:
                break

def topCapture(board,k,l):    #Procédure qui approprie des pions aux joueurs en haut
    if board[k-1][l] != board[k][l] and board[k-1][l] != 0:
        for x in range(k-1,-1,-1):
            if board[x][l] == board[k][l]:
                for y in range(x,k):
                    board[y][l] = board[k][l]
            elif board[x][l] == 0:
                break

def bottomCapture(board,k,l):    #Procédure qui approprie des pions aux joueurs en dessous
    if board[k+1][l] != board[k][l] and board[k+1][l] != 0:
        for x in range(k+1,n):
            if board[x][l] == board[k][l]:
                for y in range(x,k,-1):
                    board[y][l] = board[k][l]
            elif board[x][l] == 0:
                break

def lose(board,n,player):   #Fonction qui vérifie que le jeu est terminé ou non
    pawnCount = 0
    isolatedPawnsCount = 0
    for i in range(0,n):
        for j in range(0,n): #Vérifie chaque pion un par un
            if board[i][j] == player:
                pawnCount +=1
                if cornersCheck(board,n,i,j) == False and middleCheck(board,n,i,j) == True:
                    isolatedPawnsCount +=1
                elif cornersCheck(board,n,i,j) == True:
                    isolatedPawnsCount +=1
    if isolatedPawnsCount == pawnCount: #nombre de pions du joueur = nombre de pion isolé --> partie terminée
        return True
    else:
        return False

def middleCheck(board,n,i,j):
    isolatedPawn = 0
    if 0 < i < n:
        if board[i-1][j] != 0:  #Vérifiera au dessus
            isolatedPawn +=1
    if 0 <= i < n-1:
        if board[i+1][j] != 0:  #Vérifiera en dessous
            isolatedPawn +=1
    if 0 < j < n:
        if board[i][j-1] != 0:  #Vérifiera à gauche
            isolatedPawn +=1
    if 0 <= j < n-1:
        if board[i][j+1] != 0:  #Vérifiera à droite
            isolatedPawn +=1
    if (i == 0 or i == n-1 or j == 0 or j == n-1) and isolatedPawn == 3:    #Cas où le pion isolé est situé sur un flanc du board
        return True
    elif isolatedPawn == 4:
        return True
    else:
        return False

def cornersCheck(board,n,i,j):
    if i == 0 and j == 0:  #Coin en haut à gauche
        if board[i+1][j] != 0:  #Vérifiera en dessous
            if board[i][j+1] != 0:  #Vérifiera à droite
                return True
    if i == n-1 and j == 0:  #Coin en bas à gauche
        if board[i-1][j] != 0:  #Vérifiera au dessus
            if board[i][j+1] != 0:  #Vérifiera à droite
                return True
    if i == 0 and j == n-1:  #Coin en haut à droite
        if board[i+1][j] != 0:  #Vérifiera en dessous
            if board[i][j-1] != 0:  #Vérifiera à gauche
                return True
    if i == n-1 and j == n-1:  #Coin en bas à droite
        if board[i-1][j] != 0:  #Vérifiera au dessus
            if board[i][j-1] != 0:  #Vérifiera à gauche
                return True
    else:
        return False

def mingMang(n):
    if n < 3:
        print("Augmentez la valeur de n !")
        return
    board = newBoard(n) #On appelle la fonction newBoard qui va créer un nouveau plateau de jeu
    player = 1  #On définit la variable joueur à 1
    while lose(board,n,player) == False:    #Tant que la fonction lose retourne False, la boucle fonctionne
        displayBoard(board,n)   #Appelle la procédure qui va afficher le plateau de jeu
        print("C'est au joueur",player,"de jouer")
        i,j=selectPawn(board,n,player)  #Stocke dans i et j le résultat de la fonction selectPawn
        while possiblePawn(board,n,player,i,j) == False or previewMove(board,n,i,j) == False:   #Vérifie que le pion est sélectionnable et déplaçable
            i,j=selectPawn(board,n,player)
        k,l=selectDestination(board,n,i,j)  #Stocke dans k et l le résultat de la fonction selectDestination
        while possibleDestination(board,n,i,j,k,l) == False:   #Vérifie que le pion est positionnable à l'endroit choisi
            k,l=selectDestination(board,n,i,j)
        move(board,n,player,i,j,k,l)    #Appelle move pour déplacer le pion
        capture(board,k,l)  #Effectue l'appropriation des pions
        if player == 1: #Change de joueur à chaque fin de tour
            player = 2
        elif player == 2:
            player = 1
    if player == 1: #Si la boucle While se termine, indique qui a gagné
        print("Le joueur 2 a gagné !")
    elif player == 2:
        print("Le joueur 1 a gagné !")
    displayBoard(board,n)

n = int(input("Entrez le nombre de lignes/colonnes de votre plateau de jeu : "))
mingMang(n)
