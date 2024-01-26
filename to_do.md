## ToDo
classe modèle - tableaux de voitures - pour adapter Driving(.). Mettre en plus les circuits (en mettre 1 pour l'instant)

Architecture de code propre pour améliorer la note.

Pas grave si le controleur a bcp de paramètres / lignes.

Pk la physique est dans le controleur ? : elle devrait etre dans la voiture. Faire plutot une méthode drive associée à la voiture.

Le controleur prends juste en paramètres des touches. c'est la voiture qui décide si ca va avancer vite (lié au poids de la voiture par exemple).

Pour collision voiture/voiture : faire aussi avec les masques (car biblio associée).

Faire aussi une classe circuit pour faire propre (associe un masque à chaque circuit manuellement).

Pas besoin de classe collision.

Le controleur : GÈRE LES TOUCHES seulement. Cependant on peut quand meme mettre les collisions dans le controleur car on gere manuellement avec les masques.