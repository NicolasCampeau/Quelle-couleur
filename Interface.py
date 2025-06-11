import tkinter as tk
import random

# Base de données d'objets avec leur couleur
objet_couleurs = {
    "une boîte de Coca-Cola": "rouge",
    "un citron": "jaune",
    "un panda": "noir et blanc",
    "la pelouse": "verte",
    "le ciel par temps clair": "bleu",
    "une orange": "orange",
    "un corbeau": "noir",
    "le lait": "blanc",
    "une aubergine": "violet",
    "un feu de circulation pour 'stop'": "rouge",
    "le logo de Facebook": "bleu",
    "un kiwi (extérieur)": "brun",
    "un kiwi (intérieur)": "vert",
    "le drapeau du Canada (la feuille)": "rouge",
    "la neige": "blanc",
    "une fraise": "rouge"
}

# Initialisation de la fenêtre principale
racine = tk.Tk()
racine.title("Quelle couleur ? 🎨")
racine.geometry("500x200")

question_label = tk.Label(racine, text="", font=("Helvetica", 16), wraplength=480)
question_label.pack(pady=30)

bouton_action = tk.Button(racine, text="", font=("Helvetica", 14), width=25)
bouton_action.pack(pady=10)

# Variables globales
question = ""
reponse = ""
affiche_question = True

# Fonction pour choisir une nouvelle question
def choisir_nouvelle_question():
    global question, reponse
    objet, couleur = random.choice(list(objet_couleurs.items()))
    del objet_couleurs[objet]
    question = f"De quelle couleur est {objet} ?"
    reponse = f"Réponse : {couleur}"

# Fonction pour changer l'état d'affichage
def changer_vue():
    global affiche_question
    if affiche_question:
        # Montrer la réponse
        affiche_question = False
        mettre_a_jour_interface()
    else:
        # Nouvelle question
        choisir_nouvelle_question()
        affiche_question = True
        mettre_a_jour_interface()

# Met à jour l'affichage
def mettre_a_jour_interface():
    if affiche_question:
        question_label.config(text=question)
        bouton_action.config(text="Voir la réponse")
    else:
        question_label.config(text=reponse)
        bouton_action.config(text="Question suivante")

# Initialisation
bouton_action.config(command=changer_vue)
choisir_nouvelle_question()
mettre_a_jour_interface()

racine.mainloop()
