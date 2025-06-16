# -*- coding: utf-8 -*-
"""
Created on Wed May  7 20:48:18 2025

@author: isma0
"""


from audioplayer import AudioPlayer

class SoundManager:
    def __init__(self, app):
        self.app = app
        self.player = None
        self.musique_activee = False
        self.fichier_audio = "udu-nigerian-instrument-322564.mp3"  # Modifica con il tuo file se diverso

    def activer_musique(self):
        """Démarre la musique en boucle si elle est désactivée"""
        if not self.musique_activee:
            self.player = AudioPlayer(self.fichier_audio)
            
            self.player.play(loop=-1)   # -1 = boucle infinie
            self.musique_activee = True
            
            

    def couper_musique(self):
        """Arrête la musique si elle est active"""
        if self.player:
            self.player.stop()
            self.musique_activee = False
"""
 if not self.player.is_playing():
            self.player = AudioPlayer(self.morceau_courant)
            self.player.play()
    
        if self.root:
            self.root.after(1000, self._verifier_boucle)  
            
            
            # Appelle cette fonction à nouveau dans 1 seconde. MAIS CA RENTRAIT PAS DANS LA BOUCLE
   Le problème ici, c’est que ce code ne redémarre la musique que si elle n'est pas en train de jouer (not self.player.is_playing()), 
   mais il ne vérifie pas si elle est terminée. Donc, si la musique s'arrête naturellement (parce qu’elle est finie), is_playing() 
   renverra False, mais seulement une fois que after l’a re-testé         
            . SE LA MUSICA NON SUONA RIAPRO IL FICHER 
           Si le son est arrêté manuellement (par exemple avec stop()), alors is_playing() renvoie False, donc la musique repart.

🔹 Mais si le son se termine naturellement (c’est-à-dire qu’on arrive à la fin du fichier audio), cela dépend de la façon dont la classe AudioPlayer est conçue :

Si is_playing() ne retourne pas False quand la musique se termine toute seule, alors elle ne sera jamais relancée.

Et même si is_playing() retourne bien False, ce contrôle (after(1000, ...)) est fait seulement toutes les secondes, donc il peut y avoir un petit délai.  
            
            
            AVANT JE VOULAIS APPELER CETTE FONCTION CHAQUE UNE SECONDE POUR VERIFIER SI LE SON JOUAI OU PAS MAIS CA RENTRAIT PAS DANS LA BOUCLE


Cette classe gère le lecteur audio.

__init__:

self.player est l’objet du lecteur audio (initialement None). LA LIBRERIE 

self.musique_activee indique si la musique est en train de jouer (booléen).FALSE TRUE

self.fichier_audio contient le chemin vers le fichier mp3 à jouer.

activer_musique(self):

Si la musique n’est pas déjà active (if not self.musique_activee), on crée un nouveau lecteur AudioPlayer avec le fichier mp3.

Puis on lance la musique en boucle infinie (loop=-1).

On met self.musique_activee = True pour signaler que la musique joue.

couper_musique(self):

Si un lecteur existe (if self.player), on arrête la musique (self.player.stop()).

On met self.musique_activee = False pour signaler que la musique est stoppée.
----------------------------------------------------------------------------------------------------
La bibliothèque audioplayer (un module Python tiers) a sa propre implémentation de la méthode play().

Dans cette méthode, le paramètre loop est défini comme suit dans la doc ou le code source :

loop=0 → pas de répétition

loop=n (nombre positif) → répétitions n fois

loop=-1 → boucle infinie
la méthode play() prend un paramètre nommé loop.
IN REALTA SI POTEVA FARE SENZA GLI IF BASTAVA AUDIO PLAYER

"""


  

