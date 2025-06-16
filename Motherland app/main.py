import tkinter as tk  
import customtkinter as ctk  
from PIL import Image, ImageTk, ImageSequence  
import tkinter.messagebox as messagebox  
import gestionnaire_menu
import quizz
from langues import Traducteur  
import sound_manager as sm
class MotherlandApp(ctk.CTk):  

    def __init__(self): 
        super().__init__()  
        
        self.title("Motherland")  
        
        screen_width = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight() 
        
        
        app_width = int(screen_width * 1)
        app_height = int(screen_height * 1)
        
        
        x = (screen_width - app_width) // 2 
        y = (screen_height - app_height) // 2
        
        self.geometry(f"{app_width}x{app_height}+{x}+{y}") 
        
        self.langue = "fr"  
        self.traducteur = Traducteur(self.langue)  
        
        self.soundManager = sm.SoundManager(self)
        
        self.switch_son_active = False 
        
        

        self.fenetre_principal = ctk.CTkFrame(self, fg_color="#00AEEF", width=800, height=600)
        
        
        self.fenetre_principal.pack(fill="both", expand=True)  
        
      
        self.logo_image = Image.open("maps-unscreen.gif")  
        self.frames = [ImageTk.PhotoImage(img.resize((400, 400))) for img in ImageSequence.Iterator(self.logo_image)]
        self.frame_current = 0 
        
        self.logo_texte = Image.open("flamingtext_com-12581004097-removebg-preview.png") 
        self.logo_texte = ImageTk.PhotoImage(self.logo_texte)  
        
        self.create_widgets()  
  
        self.animate_gif()


    def create_widgets(self):  
        
        
        self.logo_image_label = tk.Label(self.fenetre_principal, image=self.frames[0], bg=self.fenetre_principal.cget("fg_color"))
        
        self.logo_image_label.pack(pady=2)
      
        self.logo_texte_label = tk.Label(self.fenetre_principal, image=self.logo_texte, bg=self.fenetre_principal.cget("fg_color"))
        self.logo_texte_label.pack(pady=2)  
        self.bouton_commencer = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("Nouvelle Partie"), font=("Arial Black", 20),
                                              fg_color="green", width=250, height=60, corner_radius=30, text_color="white",
                                              hover_color="#007ACC", command=self.lancer_partie, bg_color=self.fenetre_principal.cget("fg_color"))
        self.bouton_commencer.pack(pady=10) 
        self.options_bouton = ctk.CTkButton(self.fenetre_principal,  text=self.traducteur.traduire("Options"), font=("Arial Black", 20),
                                            fg_color="blue", width=250, height=60, corner_radius=30, text_color="white",
                                            hover_color="#007ACC", command=self.options, bg_color=self.fenetre_principal.cget("fg_color"))
        self.options_bouton.pack(pady=10)

        self.quitter_bouton = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("Quitter"), font=("Arial Black", 20),
                                             fg_color="purple", width=250, height=60, corner_radius=30, text_color="white",
                                             hover_color="#007ACC", bg_color=self.fenetre_principal.cget("fg_color"), command=self.quitter_app)
        self.quitter_bouton.pack(pady=10)
        self.animate_gif()

    def animate_gif(self): 
       
        self.logo_image_label.config(image=self.frames[self.frame_current])  
        self.frame_current = (self.frame_current + 1) % len(self.frames)  
  
        self.after(100, self.animate_gif)  
        

    def clear_screen(self):  
        for widget in self.fenetre_principal.winfo_children():  
            
            widget.destroy()  

    def lancer_partie(self): 
        
        gestionnaire_menu.lancer_partie(self) 

        
    def lancement_du_jeu(self):
      
       self.clear_screen()  
       
       btn_retour = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("Retour"), width=250, height=50,
                                  fg_color="purple", font=("Arial Black", 20), corner_radius=30,
                                  text_color="white", hover_color="#007ACC", command=self.menu_principal, bg_color=self.fenetre_principal.cget("fg_color"))
       btn_retour.place(x=20, y=650)  
       
       self.quiz = quizz.Quizz(self, self.menu_principal,self.traducteur) 
      
       
       
    def menu_principal(self):
      
       try:
            self.quiz.QCM.effacer_qcm()
            self.quiz.QCM = None 
         
      
       except:
            pass  
       self.clear_screen()
       
       self.create_widgets()
       
       self.quiz.lbl_timer.place_forget()
       
       
       self.quiz.lbl_points.place_forget()
       
       self.quiz.lbl_question.place_forget()
       self.quiz.roue.frame.place_forget()
       self.quiz.lbl_indice.place_forget()
       
      
        
       self.quiz.canvas.place_forget()
       self.popup_window.place_forget()
       
       
       self.quiz.recommencer_button.place_forget()
       
       self.frame_current = 0
       self.animate_gif() 
       
  
        
        
    def options(self):
       
        self.clear_screen()
        self.liste_boutons = []  
        
    
        self.logo_image_label = tk.Label(self.fenetre_principal, image=self.frames[0], bg=self.fenetre_principal.cget("fg_color"))
        self.logo_image_label.pack()
    
        self.logo_texte_label = tk.Label(self.fenetre_principal, image=self.logo_texte, bg=self.fenetre_principal.cget("fg_color"))
        self.logo_texte_label.pack()
    
        
    
        btn_son = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("Son"), width=250, height=50,
                                fg_color="#4CAF50", font=("Arial Black", 20), corner_radius=30,
                                text_color="white", hover_color="#007ACC",
                                command=self.ouvrir_parametres_son)
        btn_son.pack(pady=9)
        self.liste_boutons.append(btn_son)
    
        btn_langues = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("Langues"), width=250, height=50,
                                    fg_color="blue", font=("Arial Black", 20), corner_radius=30,
                                    text_color="white", hover_color="#007ACC",
                                    command= self.ouvrir_parametres_langues)
        btn_langues.pack(pady=9)
        self.liste_boutons.append(btn_langues)
    
        btn_theme = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("Thème"), width=250, height=50,
                                  fg_color="darkblue", font=("Arial Black", 20), corner_radius=30,
                                  text_color="white", hover_color="#007ACC",
                                  command= self.ouvrir_parametres_theme)
        btn_theme.pack(pady=9)
        self.liste_boutons.append(btn_theme)
    
        
        
    
        btn_retour = ctk.CTkButton(self.fenetre_principal, text=self.traducteur.traduire("⬅ Retour"), width=250, height=50,
                                   fg_color="purple", font=("Arial Black", 20), corner_radius=30,
                                   text_color="white", hover_color="#007ACC",
                                   command=self.menu_principal)
        btn_retour.pack(pady=9)
        
        self.liste_boutons = [ btn_son, btn_langues, btn_theme, btn_retour]
        
        self.animate_gif()

    
    
       
    def ouvrir_parametres_langues(self):
      
       for bouton in self.liste_boutons:
           bouton.configure(state="disabled")
           
      
       self.popup_frame_langues = ctk.CTkFrame(self.fenetre_principal, fg_color="#333333", corner_radius=20, 
                                               border_width=3, border_color="yellow", width=300, height=180)  
    
       self.popup_frame_langues.place(relx=0.5, rely=0.5, anchor="center")
       
      
       ctk.CTkLabel(self.popup_frame_langues, text=self.traducteur.traduire("🌍 Sélectionner la langue:"), font=("Arial Black", 18), text_color="yellow").pack(padx=10, pady=10)
       
      
       btn_anglais = ctk.CTkButton(self.popup_frame_langues, text=self.traducteur.traduire("Anglais"), font=("Arial", 14), fg_color="green",  text_color="white", command=lambda: self.changer_langue("en") )
       btn_anglais.pack(pady=5)
       
      
       btn_francais = ctk.CTkButton(self.popup_frame_langues, text=self.traducteur.traduire("Français"), font=("Arial", 14), fg_color="blue", text_color="white",  command=lambda: self.changer_langue("fr"))
       btn_francais.pack(pady=5)
       
       
       btn_neerlandais = ctk.CTkButton(self.popup_frame_langues, text=self.traducteur.traduire("Néerlandais"), font=("Arial", 14), fg_color="orange", text_color="white",  command=lambda: self.changer_langue("nl"))
       btn_neerlandais.pack(pady=5)
       
      
       fermer_bouton = ctk.CTkButton(self.popup_frame_langues, text=self.traducteur.traduire("Fermer"), font=("Arial Black", 12), fg_color="red", text_color="white", 
                                     command=self.fermer_popup_langues)
       fermer_bouton.pack(pady=10)
       self.liste_boutons.extend([btn_anglais, btn_francais, btn_neerlandais])
      
       
    def fermer_popup_langues(self):
        
        self.popup_frame_langues.place_forget()
        for bouton in self.liste_boutons:
            bouton.configure(state="normal") 
            
      
    def mettre_a_jour_textes(self):
        for bouton in self.liste_boutons:
            ancien_texte = bouton.cget("text")
            bouton.configure(text=self.traducteur.traduire(ancien_texte))

    
       
    def changer_langue(self, langue):
        self.traducteur.set_langue(langue)
        self.options()  
        self.ouvrir_parametres_langues()  
        try:
            self.quiz.roue.cacher()
        except:
            pass


    def ouvrir_parametres_son(self):
        
        for bouton in self.liste_boutons:
            bouton.configure(state="disabled")
        self.popup_window = ctk.CTkFrame(self, fg_color="#333333", corner_radius=20,
                                         border_width=3, border_color="yellow", width=300)
        self.popup_window.place(relx=0.5, rely=0.5, anchor="center")
    
        ctk.CTkLabel(self.popup_window, text="🎵", font=("Arial Black", 25), text_color="yellow").pack(anchor="w", padx=10, pady=(10, 5))
    
        self.switch_son = ctk.CTkSwitch(self.popup_window, text="Activer son", command=self.basculer_son)
        self.switch_son.pack(pady=10) 
    
        self.popup_window.after(100, lambda: self.switch_son.select() if self.switch_son_active else self.switch_son.deselect())
    
        fermer_bouton = ctk.CTkButton(self.popup_window, text="Fermer", font=("Arial Black", 12),
                                      fg_color="red", text_color="white", command=self.fermer_popup_son)
        fermer_bouton.pack(pady=(20, 10))

    def fermer_popup_son(self):
        
        self.popup_window.place_forget()
 
        for bouton in self.liste_boutons:
            bouton.configure(state="normal")    

    
    

    def basculer_son(self):
    
        if self.switch_son.get() == 1:  
            self.switch_son_active = True  
            
            self.soundManager.activer_musique()  
            
        else:
            self.switch_son_active = False  
            self.soundManager.couper_musique()  
        

    

    
    def quitter_app(self):
       
        reponse = messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter l'application ?")
        if reponse:  
            self.soundManager.couper_musique()
            self.destroy()  
            
    def ouvrir_parametres_theme(self):
        
        for bouton in self.liste_boutons:
            bouton.configure(state="disabled")
        
        self.popup_frame_theme = ctk.CTkFrame(self.fenetre_principal, fg_color="#333333", corner_radius=20, 
                                              border_width=3, border_color="yellow", width=200, height=200)  
       
        self.popup_frame_theme.place(relx=0.5, rely=0.5, anchor="center")
       
        ctk.CTkLabel(self.popup_frame_theme, text=self.traducteur.traduire("🔆 Sélectionner le théme:"), font=("Arial Black", 18), text_color="yellow").pack(anchor="w", padx=10, pady=5)
        
      
        btn_sombre = ctk.CTkButton(self.popup_frame_theme, text=self.traducteur.traduire("Mode sombre"), font=("Arial", 14), fg_color="green", text_color="white", 
                                   command=self.activer_mode_sombre)
        btn_sombre.pack(pady=5)
        
      
        btn_clair = ctk.CTkButton(self.popup_frame_theme, text=self.traducteur.traduire("Mode clair"), font=("Arial", 14), fg_color="blue", text_color="white", 
                                  command=self.activer_mode_clair)
        btn_clair.pack(pady=5)
      
        btn_retour = ctk.CTkButton(self.popup_frame_theme, text=self.traducteur.traduire("Thème initial"), font=("Arial", 14), fg_color="orange", text_color="white", 
                                   command=self.activer_mode_retour)
        btn_retour.pack(pady=5)
       
        fermer_bouton = ctk.CTkButton(self.popup_frame_theme, text=self.traducteur.traduire("Fermer"), font=("Arial Black", 12), fg_color="red", text_color="white", 
                                      command=self.fermer_popup_theme)
        fermer_bouton.pack(pady=10)
    
    
    def activer_mode_sombre(self):
        
        self.fenetre_principal.configure(fg_color="#1E1E1E") 
        self.update_widget_colors("#1E1E1E") 
    
    
    def activer_mode_clair(self):
        
        self.fenetre_principal.configure(fg_color="white")  
        self.update_widget_colors("white")  
    
    
    def activer_mode_retour(self):
        
        self.fenetre_principal.configure(fg_color="#00AEEF")  
        self.update_widget_colors("#00AEEF")  
    
    
    def update_widget_colors(self, bg_color):
       
        self.logo_image_label.configure(bg=bg_color)  
        self.logo_texte_label.configure(bg=bg_color)  
        self.fenetre_principal.configure(bg=bg_color)  
        
    
    def fermer_popup_theme(self):
      
        for bouton in self.liste_boutons:
            bouton.configure(state="normal")
        self.popup_frame_theme.place_forget() 
    

if __name__ == "__main__":
    app = MotherlandApp()  
    app.mainloop()  
