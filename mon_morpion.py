from tkinter import * 
from tkinter.messagebox import *
from random import randint

#######################
# Copier ici vos fonctions de test d'alignement

def test_ligne(T,i,numero_joueur):
    # test si la ligne i du tableau T est constituée des 3 mêmes numéros du joueur
    ...

def test_colonne(T,j,numero_joueur):
    # test si la colonne j du tableau T est constituée des 3 mêmes numéros du joueur
    ...

def test_diagonale(T,numero_joueur):
    # test si la diagonale du tableau T est constituée des 3 mêmes numéros du joueur
    ...

def test_antidiagonale(T, numero_joueur):
    # test si la deuxième diagonale du tableau T est constituée des 3 mêmes numéros du joueur
    ...

def test_alignement(T, numero_joueur):
    ...

##############################################################
# Le reste du code est fourni : exécuter le programme pour jouer !
##########################################################################################################
def is_free(pion_i,pion_j):
    return grille_joueur1[pion_i][pion_j] == 0  and grille_joueur2[pion_i][pion_j] == 0

def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    global tourJoueur1, choix_manuel, end_of_game, id_pions, grille_joueur1, grille_joueur2
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    # archivage de la position
    pion_i = X//TAILLE_CARRE
    pion_j = Y//TAILLE_CARRE
    # centrage
    X = (X//TAILLE_CARRE) * TAILLE_CARRE + TAILLE_CARRE//2
    Y = (Y//TAILLE_CARRE) * TAILLE_CARRE + TAILLE_CARRE//2
    if end_of_game :
        showerror("Fin du jeu", "Veuillez cliquer sur rejouer")
    elif is_free(pion_i,pion_j) :  
        # on dessine un pion
        if tourJoueur1 :
            id_pions.append(canvas.create_oval(X-r,Y-r,X+r,Y+r,fill='red'))
            grille_joueur1[pion_i][pion_j] = 1
            end_of_game = test_alignement(grille_joueur1, 1)
            if end_of_game :
                showinfo("Gagné","Un alignement est détecté : le joueur 1 a gagné")
            elif choix_manuel :
                tourJoueur1 = False
            else: 
                pion_ordi = False
                while not(pion_ordi):
                    ordi_pion_i, ordi_pion_j = randint(0,2), randint(0,2)
                    pion_ordi = is_free(ordi_pion_i, ordi_pion_j)
                X = ordi_pion_i * TAILLE_CARRE + TAILLE_CARRE//2
                Y = ordi_pion_j * TAILLE_CARRE + TAILLE_CARRE//2
                id_pions.append(canvas.create_oval(X-r,Y-r,X+r,Y+r,fill='blue'))
                grille_joueur2[ordi_pion_i][ordi_pion_j] = 2
                end_of_game = test_alignement(grille_joueur2, 2)
                if end_of_game :
                    showinfo("Gagné","Un alignement est détecté : l'ordi a gagné")
                
        else :
            id_pions.append(canvas.create_oval(X-r,Y-r,X+r,Y+r,fill='blue'))
            grille_joueur2[pion_i][pion_j] = 2
            end_of_game = test_alignement(grille_joueur2, 2)
            if end_of_game :
                showinfo("Gagné","Un alignement est détecté : le joueur 2 a gagné")
            elif choix_manuel :
                tourJoueur1 = True
            else :
                pion_ordi = False
                while not(pion_ordi):
                    ordi_pion_i, ordi_pion_j = randint(0,2), randint(0,2)
                    pion_ordi = is_free(ordi_pion_i, ordi_pion_j)
                X = ordi_pion_i * TAILLE_CARRE + TAILLE_CARRE//2
                Y = ordi_pion_j * TAILLE_CARRE + TAILLE_CARRE//2
                id_pions.append(canvas.create_oval(X-r,Y-r,X+r,Y+r,fill='red'))
                grille_joueur1[ordi_pion_i][ordi_pion_j] = 1
                end_of_game = test_alignement(grille_joueur1, 1)
                if end_of_game :
                    showinfo("Gagné","Un alignement est détecté : l'ordi a gagné")
    else :
        askokcancel("Coup interdit","Case déjà occupée, veuillez rejouer")
    return 0
        
def initialisation():
    """ Remet à zéro la grille du jeu """
    global tourJoueur1, end_of_game, choix_manuel, id_pions, grille_joueur1, grille_joueur2
    while len(id_pions) > 0 :
        pion = id_pions.pop()
        canvas.delete(pion)
    tourJoueur1 = True
    end_of_game = False
    grille_joueur1 = [[0,0,0] , [0,0,0] , [0,0,0] ]
    grille_joueur2 = [[0,0,0] , [0,0,0] , [0,0,0] ]
    
    if not(choix_manuel) and ordi_commence :
        pion_ordi = False
        while not(pion_ordi):
            ordi_pion_i, ordi_pion_j = randint(0,2), randint(0,2)
            pion_ordi = is_free(ordi_pion_i, ordi_pion_j)
        X = ordi_pion_i * TAILLE_CARRE + TAILLE_CARRE//2
        Y = ordi_pion_j * TAILLE_CARRE + TAILLE_CARRE//2
        id_pions.append(canvas.create_oval(X-r,Y-r,X+r,Y+r,fill='red'))
        grille_joueur1[ordi_pion_i][ordi_pion_j] = 1
        tourJoueur1 = False
    return 0
    
def option_manuel():
    global choix_manuel 
    choix_manuel = mode_manuel.get() == 1
    return None

def selection_joueur_debut():
    global ordi_commence
    ordi_commence = qui_commence.get() == 1
    return None

# géométrie de la fenetre
TAILLE_CARRE = 100
NB_CARRE = 3
r = 30 # rayon du pion

# initialisation des variables
grille_joueur1 = [[0,0,0] , [0,0,0] , [0,0,0] ]
grille_joueur2 = [[0,0,0] , [0,0,0] , [0,0,0] ]
tourJoueur1 = True
end_of_game = False
choix_manuel = False
ordi_commence = False
id_pions = []


#################### Définition de la géométrie de la fenetre
fenetre = Tk()

fenetre.title('Mini Morpion')
fenetre['bg']='white'
# barre de menu
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Menu", menu=menu1)
fenetre.config(menu=menubar)

# bloc de gauche : la grille et les deux boutons à cliquer
left_frame = Frame(fenetre, width=NB_CARRE * TAILLE_CARRE + 40, height=NB_CARRE * TAILLE_CARRE + 40, bg='white')
left_frame.pack(side='left', fill='both', padx=10, pady=5, expand=True)

canvas = Canvas(left_frame, width=NB_CARRE * TAILLE_CARRE, height=NB_CARRE * TAILLE_CARRE, background='yellow')
x1 = TAILLE_CARRE
for _ in range(2):
    canvas.create_line(x1, 0, x1, NB_CARRE * TAILLE_CARRE)
    x1 += TAILLE_CARRE
y1 = TAILLE_CARRE
for _ in range(2):
    canvas.create_line(0, y1, NB_CARRE * TAILLE_CARRE, y1)
    y1 += TAILLE_CARRE
canvas.pack(padx=20,pady=20)
# détection d'un clic sur la grille
canvas.bind('<Button-1>', clic)

# Création de widgets Button (bouton Quitter et Effacer)
bottom_frame = Frame(left_frame, width=NB_CARRE * TAILLE_CARRE, height=50,  bg='white')
bottom_frame.pack(side='bottom', fill='both', padx=10, pady=10, expand=True)
Button(bottom_frame, text = '(re)Jouer', command = initialisation).pack(side='left',padx = 5,pady = 5)
Button(bottom_frame, text = 'Quitter', command = fenetre.destroy).pack(side='right')

# bloc de groite : sélection manuel/ordi et choix du joueur qui commence
right_frame = Frame(fenetre, width=NB_CARRE * TAILLE_CARRE, height=TAILLE_CARRE,  bg='white')
right_frame.pack(side='right', fill='both', padx=10, pady=100, expand=True)

petit_bloc1 = Frame(right_frame, width=NB_CARRE * TAILLE_CARRE, height=TAILLE_CARRE,  bg='white')
petit_bloc1.pack(side='top', fill='both', padx=10, pady=20, expand=True)
mode_manuel = IntVar() 
bouton1 = Radiobutton(petit_bloc1, text="Mode Manuel ", variable=mode_manuel, value=1, command=option_manuel)
bouton2 = Radiobutton(petit_bloc1, text="Contre l'ordi", variable=mode_manuel, value=2, command=option_manuel)
bouton1.pack()
bouton2.pack()

petit_bloc2 = Frame(right_frame, width=NB_CARRE * TAILLE_CARRE, height=TAILLE_CARRE,  bg='white')
petit_bloc2.pack(side='top', fill='both', padx=10, pady=20, expand=True)
label1 = Label(petit_bloc2, text="Si jeu contre l'ordi :",relief="raised",bg="yellow")
label1.pack()
qui_commence = IntVar() 
bouton3 = Radiobutton(petit_bloc2, text="Ordi en premier ",bg="red", variable=qui_commence, value=1, command=selection_joueur_debut)
bouton4 = Radiobutton(petit_bloc2, text="Ordi joue en second",bg="blue", variable=qui_commence, value=2, command=selection_joueur_debut)
bouton3.pack()
bouton4.pack()
##########################################################################



# corps du programme


initialisation()


fenetre.mainloop()