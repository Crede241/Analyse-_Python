import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Charger seulement les 100 premières lignes du fichier Excel
file_path = 'D:\Test transport\sales data.xlsx'
df_sales = pd.read_excel(file_path, sheet_name='sales data', nrows=100)


# Couleurs pour chaque type d'appareil
colors = {'PC': 'blue', 'Mobile': 'red', 'Tablet': 'green'}

# Créer la figure et les axes
fig, ax = plt.subplots()

# Créer le scatter plot avec les valeurs spécifiques
scatter = ax.scatter(df_sales['order_value_EUR'],
                     df_sales['cost'],
                     c=df_sales['device_type'].map(colors), 
                     alpha=0.7,
                     s=df_sales['cost'] / 100)

# Créer les légendes personnalisées
legend_handles = [mpatches.Patch(color=color, label=device_type)
                  for device_type, color in colors.items()]

ax.legend(handles=legend_handles, title="Produit")

# Ajouter des labels et un titre
ax.set_xlabel('Prix unitaire')
ax.set_ylabel('Ventes totales')
ax.set_title('Prix unitaire VS ventes totales par produit')

# Afficher la grille
ax.grid(True)

# Afficher le graphique
plt.show()
