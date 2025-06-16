import tkinter as tk  # Importation de tkinter pour créer des interfaces graphiques
import customtkinter as ctk  # Importation de customtkinter pour avoir des widgets plus modernes et personnalisés

def lancer_partie(self):  # Méthode pour lancer une nouvelle partie
    self.clear_screen()  # Efface l'écran précédent
    # Recharge l'image du logo et du texte
    self.logo_image_label = tk.Label(self.fenetre_principal, image=self.frames[0], bg=self.fenetre_principal.cget("fg_color"))
    self.logo_image_label.pack(pady=10)

    self.logo_texte_label = tk.Label(self.fenetre_principal, image=self.logo_texte, bg=self.fenetre_principal.cget("fg_color"))
    self.logo_texte_label.pack(pady=10)

    # Titre pour la sélection de la difficulté
    label = ctk.CTkLabel(self.fenetre_principal, text="Sélectionnez un niveau de difficulté: ", 
                         font=("Arial", 22), text_color="white", bg_color=self.fenetre_principal.cget("fg_color"))
    label.pack(pady=0)

    # Bouton pour sélectionner le niveau de difficulté "Facile"
    btn_facile = ctk.CTkButton(self.fenetre_principal, text="Facile", width=250, height=50, 
                             fg_color="green", font=("Arial Black", 20), corner_radius=30,
                             text_color="white", hover_color="#007ACC", 
                             bg_color=self.fenetre_principal.cget("fg_color"), command=self.lancement_du_jeu)
    btn_facile.pack(pady=10)
    
    # Bouton pour sélectionner le niveau de difficulté "Normal"
    btn_normal = ctk.CTkButton(self.fenetre_principal, text="Normal", width=250, height=50, 
                               fg_color="#4CAF50", font=("Arial Black", 20), corner_radius=30,
                               text_color="white", hover_color="#007ACC", bg_color=self.fenetre_principal.cget("fg_color"))
    btn_normal.pack(pady=10)
    
    # Bouton pour sélectionner le niveau de difficulté "Difficile"
    btn_difficile = ctk.CTkButton(self.fenetre_principal, text="Difficile", width=250, height=50, 
                                  fg_color="blue", font=("Arial Black", 20), corner_radius=30,
                                  text_color="white", hover_color="#007ACC", bg_color=self.fenetre_principal.cget("fg_color"))
    btn_difficile.pack(pady=10)

    # Bouton pour revenir au menu principal
    btn_retour = ctk.CTkButton(self.fenetre_principal, text=" Retour", width=250, height=50, 
                             fg_color="purple", font=("Arial Black", 20), corner_radius=30,
                             text_color="white", hover_color="#007ACC", command=self.menu_principal, bg_color=self.fenetre_principal.cget("fg_color"))
    btn_retour.pack(pady=10)
