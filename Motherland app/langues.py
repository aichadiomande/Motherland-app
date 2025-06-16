class Traducteur:
    def __init__(self, langue="fr"):
        """➡️ langue est un paramètre de la méthode __init__, et self.langue est un attribut de l’objet."""
        self.langue = langue
        self.traductions = {
    "fr": {
        "⬅ Retour": "⬅ Retour",
        "Thème initial": "Thème initial",
        "Nouvelle Partie": "Nouvelle Partie",
        "Mode clair": "Mode clair",
        "Options": "Options",
        "Quitter": "Quitter",
        "Reprendre une Partie": "Reprendre une Partie",
        "Joueurs": "Joueurs",
        "Son": "Son",
        "Mode sombre": "Mode sombre",
        "Langues": "Langues",
        "Thème": "Thème",
        "Retour": "Retour",
        "Sélectionner la langue": "Sélectionner la langue",
        "Anglais": "Anglais",
        "Français": "Français",
        "Néerlandais": "Néerlandais",
        "Fermer": "Fermer",
        "Volume": "Volume",
        "Activer son": "Activer son",
        #"Prochaine question": "Prochaine question",
        "Game over! Merci pour avoir joué!": "Fin du jeu! Merci d'avoir joué!",
        #"Nom du joueur": "Nom du joueur",  # Nouvelle traduction ajoutée
        "🌍 Sélectionner la langue:": "🌍 Sélectionner la langue:",
        "🔆 Sélectionner le théme:": "🔆 Sélectionner le théme:",
        "Saisir nom": "Saisir nom",  # Nouvelle traduction ajoutée
        #"Nom enregistré": "Nom enregistré avec succès !"  # Nouvelle traduction ajoutée
        "Facile": "Facile",
        "Normal": "Normal",
        "Difficile": "Difficile",
        "Temps restant": "Temps restant" ,
        "quizz suivants": "quizz suivants",
        "Prochaine Question": "Prochaine Question",
        "Temps écoulé! Essayez encore.": "Temps écoulé! Essayez encore.",
        "Points :": "Points :",
        "Où se trouve": "Où se trouve",
        "Dommage, ce n'est pas le bon pays.": "Dommage, ce n'est pas le bon pays.",
        "Bravo ! Correct !": "Bravo ! Correct !",
        "Partie terminée. 😞": "Partie terminée. 😞",
        "La roue tourne…": "La roue tourne…",
        "Tourner": "Tourner", 
        "Indice": "Indice",
        "Le jeu continue": "Le jeu continue",
        "Fin du jeu": "Fin du jeu",
        "Résultat :": "Résultat :",
     },
    "en": {
        "⬅ Retour": "⬅ Back",
        "Thème initial": "Default theme",
        "Nouvelle Partie": "New Game",
        "Mode clair": "Light mode",
        "Options": "Settings",
        "Quitter": "Quit",
        "Reprendre une Partie": "Resume Game",
        "Joueurs": "Players",
        "Son": "Sound",
        "Mode sombre": "Dark mode",
        "Langues": "Languages",
        "Thème": "Theme",
        "Retour": "Back",
        "Sélectionner la langue": "Select Language",
        "Anglais": "English",
        "Français": "French",
        "Néerlandais": "Dutch",
        "Fermer": "Close",
        "Volume": "Volume",
        "Activer son": "Enable Sound",
        #"Prochaine question": "Next Question",
        "Game over! Merci pour avoir joué!": "Game over! Thank you for playing!",
        #"Nom du joueur": "Player Name",  # Nouvelle traduction ajoutée
        "🔆 Sélectionner le théme:": "🔆 Select the theme:",
        "🌍 Sélectionner la langue:": "🌍 Select language:",
        "Saisir nom": "Enter name",  # Nouvelle traduction ajoutée
        #"Nom enregistré": "Name successfully recorded!"  # Nouvelle traduction ajoutée
        "Facile": "Easy",
        "Normal": "Normal",
        "Difficile": "Hard",
        "Temps restant": "Time left" ,
        "quizz suivants": "next quizzes",
        "Prochaine Question": "Next Question",
        "Temps écoulé! Essayez encore.": "Time's up! Try again.",
        "Points :": "Points :",
        "Où se trouve": "Where is",
        "Dommage, ce n'est pas le bon pays.": "Too bad, this is not the right country.", 
        "Bravo ! Correct !": "Well done! Correct!",
        "Partie terminée. 😞": "Game over. 😞", 
        "La roue tourne…" : "The wheel turns…",
        "Tourner" : "Turn",
        "Indice": "Hint", 
        "Le jeu continue": "The game continues",
        "Fin du jeu": "End of the game",
        "Résultat :": "Result:",
     },    
    "nl": {
        "⬅ Retour": "⬅ Terug",
        "Thème initial": "Standaardthema",
        "Nouvelle Partie": "Nieuw Spel",
        "Mode clair": "Lichte modus",
        "Options": "Opties",
        "Quitter": "Afsluiten",
        "Reprendre une Partie": "Hervatten Spel",
        "Joueurs": "Spelers",
        "Son": "Geluid",
        "Mode sombre": "Donkere modus",
        "Langues": "Talen",
        "Thème": "Thema",
        "Retour": "Terug",
        "Sélectionner la langue": "Selecteer Taal",
        "Anglais": "Engels",
        "Français": "Frans",
        "Néerlandais": "Nederlands",
        "Fermer": "Sluiten",
        "Volume": "Volume",
        "Activer son": "Geluid Inschakelen",
        #"Prochaine question": "Volgende Vraag",
        "Game over! Merci pour avoir joué!": "Game over! Bedankt voor het spelen!",
        #"Nom du joueur": "Speler Naam",  # Nouvelle traduction ajoutée
        "🔆 Sélectionner le théme:": "🔆 Thema selecteren:",
        "🌍 Sélectionner la langue:": "🌍 Taal selecteren:",
        "Saisir nom": "Naam invoeren",  # Nouvelle traduction ajoutée
        #"Nom enregistré": "Naam succesvol geregistreerd!"  # Nouvelle traduction ajoutée
        "Facile": "Makkelijk",
        "Normal": "Normaal",
        "Difficile": "Moeilijk",
        
        "quizz suivants": "volgende quizzen",
        "Prochaine Question": "Volgende Vraag",
        "Temps restant": "Resterende tijd",
        "Temps écoulé! Essayez encore.": "Tijd is om! Probeer opnieuw.",
        "Points :": "Punten :",
        "Où se trouve": "Waar ligt",
        "Dommage, ce n'est pas le bon pays.": "Jammer, dit is niet het juiste land.", 
        "Bravo ! Correct !": "Goed zo! Correct!",
        "Partie terminée. 😞": "Spel afgelopen. 😞",
        "La roue tourne…" : "Het wiel draait…",
        "Tourner" : "Draaien",
        "Indice": "Hint",
        "Le jeu continue": "Het spel gaat verder",
        "Fin du jeu": "Einde van het spel",
        "Résultat :": "Resultaat:",
    }
}

    """sur moderland je fais:traducteur = Traducteur(self.langue) une instance (un objet) pour minservir de la classe Traducteur
    créée à partir de la classe Traducteur importer dans ce module. mm sans self.langue ca marche cest deja de dafault"""

    def set_langue(self, langue):
        self.langue = langue
        """Elle change la langue actuelle utilisée par l’objet Traducteur.
Autrement dit : elle modifie l’attribut self.langue. JE LAPPELLE DANS CHANGER LANGUE SUR MOTHERLAND QUAND JE CLIQUE SUR UN BOUTON """
    def traduire(self, texte):
        return self.traductions.get(self.langue, {}).get(texte, texte)
    """ si trouve pas ka langue dictionnaire vide, si il troyve pas texte traduit il redonne le mm texte
    
   SI ON APPUIE SUR AUCUN BOUTON POUR TRADUIR JEXECUTE LE CONSTRUCTEUR DE TRADUIRE
   traducteur = Traducteur() DE DEFAULT EN FRANCAUS ET 
   LES AUTRE BOUTONS ONT SELF.TRADUCTEUR TRADUIRE DONC IL CHERCHENT DANS LE 
   DICTIONNAIRE FRANCAIS
    
    """
    
