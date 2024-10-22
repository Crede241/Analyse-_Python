import matplotlib.pyplot as plt

# Créer une figure et des sous-graphes
fig, ax = plt.subplots(figsize=(10, 5))

# Tracer une courbe avec des paramètres d'apparence
ax.plot([1, 2, 3, 4], [10, 20, 25, 26],
        color='yellow', linestyle='-', marker='o')
ax.plot([1, 2, 3, 4], [12, 16, 18, 24],
        color='green', linestyle='--', marker='o')

# Ajouter les labels et le titre
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Un graphique avec Matplotlib')

# Ajouter une grille et définir les limites des axes
ax.grid(True)
ax.set_xlim(0, 5)
ax.set_ylim(0, 35)

# Ajouter une légende au graphique
ax.legend(["Série 1", "Série 2"])

# Afficher la figure
plt.show()
