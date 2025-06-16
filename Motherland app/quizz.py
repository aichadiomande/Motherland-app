
import customtkinter as ctk

import random
import math
from PIL import Image, ImageTk
from langues import Traducteur
import QCM
class RoueDeLaChance:
    
    def __init__(self, parent, callback,traducteur ):
        
        self.parent = parent
        self.callback = callback
        
        self.traducteur = traducteur
        
        self.recompenses = ["Indice", "+4 pts", "+5 pts", "Fin du jeu", "Le jeu continue"]
        self.is_derniere_chance = False
        self.est_en_rotation = False
        
        self.frame = ctk.CTkFrame(parent, width=320, height=320, fg_color="#333333")
        
        self.canvas = ctk.CTkCanvas(self.frame, width=300, height=300, bg="#333333", highlightthickness=0)
       
        self.canvas.pack(pady=10)

        self.bouton_tourner = ctk.CTkButton(self.frame, text=self.traducteur.traduire("Tourner"), command=self.lancer_rotation)
        self.bouton_tourner.pack(pady=(0, 5))

        self.label_resultat = ctk.CTkLabel(self.frame, text="", font=("Arial", 14, "bold"))
        self.label_resultat.place(relx=0.5, rely=0.85, anchor="center")

        self.dessiner_roue(0) 
        
        
    def recompenses_traduites(self):
        return [self.traducteur.traduire(r) if r in {"Indice", "Fin du jeu", "Le jeu continue"} else r for r in self.recompenses]

    
    def cacher(self):
        self.frame.place_forget()
        self.label_resultat.configure(text="")

    def couleur_spicchio(self, i):
        return ["#FF5733", "#33A1FF", "#33FF57", "#FFC300", "#C70039", "#8E44AD"][i] 

    def dessiner_roue(self, rotation=0):
        self.canvas.delete("all") 
       
        cx, cy, r = 150, 150, 100  
        n = len(self.recompenses) 
        angle = 360 / n  
    
        for i, txt in enumerate(self.recompenses_traduites()):
            
            start = i * angle + rotation  
            self.canvas.create_arc(cx - r, cy - r, cx + r, cy + r,
                                   start=start, extent=angle,
                                   fill=self.couleur_spicchio(i), outline="white", width=2)

            mid = math.radians(start + angle / 2) 
            x = cx + 1.2 * r * math.cos(mid)  
            y = cy + 1.2 * r * math.sin(mid)
            
            self.canvas.create_text(x, y, text=txt, font=("Arial", 10, "bold"), fill="white")

  
    def lancer_rotation(self):
        
        if self.est_en_rotation:
            return  
        

        self.est_en_rotation = True
        self.bouton_tourner.configure(state="disabled") 
        self.label_resultat.configure(text="")
        self.label_resultat.configure(text=self.traducteur.traduire("La roue tourne…"))
        
  
        self.angle_courant = 0  
        
        
        self.angle_total = random.randint(720, 1440) + random.uniform(0, 360)  
        
        self.vitesse = 10  
        self.frames = 0
        self.max_frames = 120  
        
        self.parent.after(self.vitesse, self._animer)
        

    def _animer(self):
        if self.frames < self.max_frames:
            
            progression = self.frames / self.max_frames 
            
            step = (1 - progression) * (self.angle_total / self.max_frames)
            
            self.angle_courant += step  
            self.dessiner_roue(self.angle_courant)  
            self.frames += 1  
            
          
            self.parent.after(self.vitesse, self._animer)
        else:
           
            self.angle_final = self.angle_courant 
            
            self.dessiner_roue(self.angle_courant)
            self._afficher_resultat()
            
    def _afficher_resultat(self):
        n = len(self.recompenses)
        angle = 360 / n
        
        angle_corrected = (270 - (self.angle_final % 360)) % 360 
        
        
        idx = int(angle_corrected // angle)  
        
        res = self.recompenses_traduites()[idx]
        self.label_resultat.configure(text="%s %s" % (self.traducteur.traduire("Résultat :"), res))

       
        self.est_en_rotation = False
        self.callback(res)  
        

class Quizz:
    def __init__(self, root, app_principale, traducteur):
        self.root = root
         
        self.canvas = ctk.CTkCanvas(root, width=950, height=951, bg="#00AEEF", highlightthickness=0)
        img = Image.open("africa.png").resize((950, 951))
        self.app = app_principale
        self.traducteur = traducteur

        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")
        
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        

        self.lbl_question = ctk.CTkLabel(root, text="", font=("Arial", 20), fg_color="grey")
        self.lbl_question.place(relx=0.3, rely=0.8, anchor="center")

        self.lbl_timer = ctk.CTkLabel( root,text="%s : %s" % (self.traducteur.traduire("Temps restant"), "00:30"),
        font=("Arial", 16),fg_color="grey")

        self.lbl_timer.place(x=10, y=10)

        self.points = 10 
       
        points_text = "%s %d" % (self.traducteur.traduire("Points :"), self.points)
        self.lbl_points = ctk.CTkLabel(root, text=points_text, font=("Arial", 16), fg_color="grey")
        self.lbl_points.place(x=10, y=40)

        self.lbl_indice = ctk.CTkLabel(root, text="", font=("Arial", 16), fg_color="grey")
        self.lbl_indice.place(relx=0.3, rely=0.85, anchor="center")

        self.roue = RoueDeLaChance(root, self._gerer_recompense, self.traducteur)
        self.roue.frame.place_forget()
        self.compte_timer_id = None

        self._charger_pays()
        self._nouveau_quiz()
        
        self.indice_montrer = False
        self.reponse_apres_indice = False

        self.mettre_a_jour_textes()
        self.QCM = None
        
        


        
    def mettre_a_jour_textes(self):
        m, s = divmod(self.temps, 60)
        self.lbl_timer.configure(text="%s : %02d:%02d" % (self.traducteur.traduire("Temps restant"), m, s))
        self._mettre_a_jour_points()  
        
    def _mettre_a_jour_points(self):
        points_text = "%s %d" % (self.traducteur.traduire("Points :"), self.points)
        
        self.lbl_points.configure(text=points_text)

    def _charger_pays(self):
        self.pays_coord = {
    "Algérie": ((300, 110), "nord-ouest"),
    "Tunisie": ((380, 50), "nord-est"),
    "Maroc": ((190, 85), "nord-ouest"),
    "Mauritanie": ((170, 230), "ouest"),
    "Mali": ((250, 250), "centre-ouest"),
    "Niger": ((380, 250), "centre-est"),
    "Tchad": ((500, 250), "centre"),
    "Libye": ((480, 120), "nord-est"),
    "Égypte": ((600, 110), "nord-est"),
    "Soudan": ((620, 250), "est"),
    "Soudan du Sud": ((620, 400), "sud-est"),
    "Éthiopie": ((720, 370), "sud-est"),
    "Djibouti": ((770, 337), "sud-est"),
    "Érythrée": ((720, 280), "est"),
    "Somalie": ((840, 370), "sud-est"),
    "Cameroun": ((435, 400), "centre-sud"),
    "Nigéria": ((370, 350), "centre-ouest"),
    "République centrafricaine": ((500, 405), "centre-sud"),
    "Gabon": ((410, 500), "sud-ouest"),
    "Guinée équatoriale": ((400, 469), "sud-ouest"),
    "Congo": ((460, 510), "sud"),
    "Congo (RDC)": ((540, 510), "sud"),
    "Angola": ((490, 650), "sud-ouest"),
    "Kenya": ((710, 480), "est"),
    "Ouganda": ((655, 465), "est"),
    "Tanzanie": ((690, 570), "sud-est"),
    "Zambie": ((580, 680), "sud"),
    "Zimbabwe": ((620, 740), "sud"),
    "Afrique du Sud": ((560, 880), "sud"),
    "Madagascar": ((820, 720), "est"),
    "Maurice": ((920, 750), "est"),
    "Seychelles": ((870, 617), "est"),
    "Sénégal": ((100, 290), "ouest"),
    "Guinée-Bissau": ((110, 332), "ouest"),
    "Gambie": ((102, 313), "ouest"),
    "Guinée": ((150, 345), "ouest"),
    "Côte d'Ivoire": ((210, 390), "ouest"),
    "Ghana": ((270, 380), "ouest"),
    "Bénin": ((310, 350), "centre-ouest"),
    "Togo": ((292, 370), "centre-ouest"),
    "Burkina Faso": ((270, 320), "ouest"),
    "Sierra Leone": ((145, 380), "ouest"),
    "Libéria": ((170, 405), "ouest"),
    "Rwanda": ((628, 516), "est"),
    "Burundi": ((628, 535), "est"),
    "Malawi": ((670, 670), "sud-est"),
    "Mozambique": ((670, 720), "sud-est"),
    "Namibie": ((480, 760), "sud-ouest"),
    "Botswana": ((560, 770), "sud"),
    "Lesotho": ((595, 880), "sud"),
    "Eswatini": ((634, 840), "sud"),
    "Comores": ((790, 650), "est"),
    "Cap-Vert": ((10, 276), "ouest"),
    "Sao Tomé-et-Principe": ((350, 490), "centre-ouest"),
} 
    """dictionnaire tuple"""
    def _nouveau_quiz(self):
        self.lbl_indice.configure(text="")
        self.temps = 30
        self.pays_correct = random.choice(list(self.pays_coord.keys()))
        question = self.traducteur.traduire("Où se trouve") + f" {self.pays_correct} ?" 
        self.lbl_question.configure(text=question)
        self._creer_voyants()
        self._compte_a_rebours()
        

    def _creer_voyants(self):
        self.canvas.delete("voyant")
        self.voyants_ids = []  
        self.oid_to_pays = {} 
       
        for pays, (coord, indice) in self.pays_coord.items():
            x, y = coord
            oid = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue", tags="voyant")
            
            self.voyants_ids.append(oid)
            
            self.oid_to_pays[oid] = pays #ajoute clees a la liste
            self.canvas.tag_bind(oid, "<Button-1>", lambda e, p=pays: self._verifier_reponse(p))
            

    def _compte_a_rebours(self):
        """MISE A JOURS TEMPS"""
        if self.compte_timer_id: 
            
            self.root.after_cancel(self.compte_timer_id)
            
        if self.temps >= 0:
            m, s = divmod(self.temps, 60) 
            self.lbl_timer.configure(text="%s : %02d:%02d" % (self.traducteur.traduire("Temps restant"), m, s))

            self.temps -= 1
            self.compte_timer_id = self.root.after(1000, self._compte_a_rebours)
            
        else:
            
            self.lbl_timer.configure(
                text="%s : 00:00" % self.traducteur.traduire("Temps restant")
            ) 
            self.lbl_question.configure(text=self.traducteur.traduire("Temps écoulé ! 😞"))
            self.root.after(2000, self._nouveau_quiz)
   
    def _activer_clics_voyants(self):
        for oid in self.voyants_ids:
            pays = self.oid_to_pays[oid]
            self.canvas.tag_bind(oid, "<Button-1>", lambda e, p=pays: self._verifier_reponse(p))
            
    
    def _verifier_reponse(self, choix):
        
        for oid in self.voyants_ids:
            self.canvas.tag_unbind(oid, "<Button-1>") 
  
        self.dernier_pays = self.pays_correct 
 
        if self.indice_montrer and choix != self.pays_correct: 
            
                self.reponse_apres_indice = True 
            

                self.lbl_question.configure(text=self.traducteur.traduire("Partie terminée. 😞"))
                self.root.after(2500, lambda: self._retour_menu_principal())
                return
        
        if choix == self.pays_correct:
            self.lbl_question.configure(text=self.traducteur.traduire("Bravo ! Correct !"))
            self.points += 2
            self._mettre_a_jour_points() 
          
            self.canvas.place_forget() 
            self.lbl_question.place_forget()
            
            self.QCM = QCM.QCM(self.root, "questions.json", self) 
            self.QCM.afficher_question()

        else:
            
            self.lbl_question.configure(text=self.traducteur.traduire("Dommage, ce n'est pas le bon pays."))
            for oid, nom in self.oid_to_pays.items():
                if nom == self.pays_correct:
                    self.canvas.itemconfig(oid, fill="red")  

            self.points -= 3
            if self.points < 0:
                self.points = 0 
            self._mettre_a_jour_points()
            
    
           
            if self.points <= 0 and not self.roue.frame.winfo_ismapped():
                self.roue.is_derniere_chance = True
                self.roue.frame.place(relx=0.85, rely=0.5, anchor="center") 
                
                self.roue.bouton_tourner.configure(state="normal")
                
            elif not self.indice_montrer:
                
                self.root.after(2000, self._nouveau_quiz)
                self.root.after(2000, self._activer_clics_voyants)


    def _gerer_recompense(self, resultat):
        
        
        if resultat == "+5 pts":
            self.points += 5
            self._mettre_a_jour_points()
            
            self.roue.is_derniere_chance = False  
            self.root.after(2000, self.roue.cacher)
            self.root.after(3000, self._nouveau_quiz)

        elif resultat == "+4 pts":
            self.points += 4
            self._mettre_a_jour_points()
            self.roue.is_derniere_chance = False  
            self.root.after(2000, self.roue.cacher)
            self.root.after(3000, self._nouveau_quiz)

        
        elif resultat == self.traducteur.traduire( "Indice"):
            
            
            self.root.after(2000, self.roue.cacher)  
            

            question = self.traducteur.traduire("Où se trouve") + f" {self.pays_correct} ?"
            self.lbl_question.configure(text=question)
            indice = self.pays_coord[self.pays_correct][1]  
            
            self.root.after(2500, lambda: self.lbl_indice.configure(text=f"Indice : {indice}"))
            self.root.after(2500, self._activer_clics_voyants) 
            self.indice_montrer = True 
            self.reponse_apres_indice = True

        
        elif resultat == self.traducteur.traduire("Fin du jeu") and self.roue.is_derniere_chance:
            
            self.lbl_question.configure(text=self.traducteur.traduire("Partie terminée. 😞"))
            self.root.after(2000, self.roue.cacher)
            
            self.root.after(4000, lambda: self._retour_menu_principal())
        
        elif resultat == self.traducteur.traduire("Le jeu continue"):
            
            def continuer_jeu():
                self.roue.cacher()
                self._nouveau_quiz()
            self.root.after(2000, continuer_jeu)
 
        if self.points > 0 and self.roue.is_derniere_chance:
            self.roue.is_derniere_chance = False
            self.roue.cacher() 
            self.root.after(3000, self._nouveau_quiz) 

    def _retour_menu_principal(self):
        if self.QCM:
            self.QCM.effacer_qcm()
            self.QCM = None
            
        if self.app:
            
            self.app()

    

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("1300x960")
    menu_principal = None
    traducteur = Traducteur()
    quiz=Quizz(app, menu_principal, traducteur)  
    app.mainloop()


