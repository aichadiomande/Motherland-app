# -*- coding: utf-8 -*-
import tkinter as tk
import customtkinter as ctk
import json
from langues import Traducteur
import random

class QCM:
    def __init__(self, app, fichier_questions,  quizz_instance):
        
        self.app = app  
        self.quizz = quizz_instance 
        self.index_question = 0
        self.questions = self.charger_questions(fichier_questions)
        self.reponse_choisie = tk.StringVar()
        self.boutons_radio = []
        self.label_question = None
        self.next_button = None

    def charger_questions(self, fichier):
        with open(fichier, "r", encoding='utf-8') as f:
            questions = json.load(f) 
        random.shuffle(questions)
        return questions

    def afficher_question(self):
        if self.index_question >= len(self.questions):
            self.label_question.config(text="Fin du quiz.")
            for btn in self.boutons_radio: 
                btn.destroy()
            if self.next_button:
                self.next_button.destroy() 
            return

        question_actuelle = self.questions[self.index_question] 

        self.reponse_choisie.set(None) 

        if self.label_question is None: 
            self.label_question = tk.Label(self.app, font=("Arial", 16), bg="#00AEEF", fg="white", wraplength=700, justify="left")
            self.label_question.place(x=700, y=200)

        self.label_question.config(text=question_actuelle["question"]) 

        for btn in self.boutons_radio:
            btn.destroy()
        self.boutons_radio.clear()

        for i, option in enumerate(question_actuelle["options"]):
            radio = tk.Radiobutton(self.app, text=option, variable=self.reponse_choisie,
                                   value=option, font=("Arial", 14), bg="#00AEEF", fg="black",
                                   selectcolor="lightgray", anchor="w", width=30, justify="left")
            radio.place(x=700, y=280 + i * 40) 
            self.boutons_radio.append(radio)

        if self.next_button is None:
            self.next_button = ctk.CTkButton(self.app, text="Valider", command=self.verifier_reponse)
            self.next_button.place(x=720, y=350)
        else:
            self.next_button.configure(command=self.verifier_reponse) 
            
            

    def verifier_reponse(self):
        bonne_reponse = self.questions[self.index_question]["reponse"]
        reponse = self.reponse_choisie.get()
        
        if reponse != bonne_reponse:
            self.quizz.points -= 3
        else:
            self.quizz.points += 2
    
        self.quizz._mettre_a_jour_points()
        if self.quizz.points <= 0:
            self.quizz.points=0
            self.quizz._mettre_a_jour_points()
            self.label_question.configure(text="Partie terminée. 😞")
            for btn in self.boutons_radio:
                btn.config(state="disabled")

            self.next_button.configure(state="disabled")
            
            self.app.after(3000, self.quizz._retour_menu_principal)
            
        
        self.index_question += 1
        self.afficher_question()
        self.app.update()  
        
    def effacer_qcm (self):
        self.label_question.destroy()
        self.next_button.destroy()
        for btn in self.boutons_radio:
            btn.destroy()
            
        
            
if __name__ == "__main__":
    from quizz import Quizz
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("QCM de Géographie")
    root.geometry("800x600")
    root.configure(fg_color="#00AEEF")
    app_principale = None
    traducteur = Traducteur()
    quizz_instance = Quizz(root, app_principale, traducteur)
    quizz_instance._mettre_a_jour_points()  
    quizz_instance.canvas.place_forget()
    quizz_instance.lbl_question.place_forget()
    
    fichier = "questions.json"  

    qcm = QCM(root, fichier,quizz_instance)
    qcm.afficher_question()

    root.mainloop()
