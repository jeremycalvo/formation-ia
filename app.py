import plotly.express as px
import pandas as pd

# PART 5

data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')


data['chiffre_affaires'] = data['prix'] * data['qte']

product_revenue = data.groupby('produit')['chiffre_affaires'].sum()

print("CA par produit:",product_revenue)

revenue_mean = product_revenue.mean()
revenue_median = product_revenue.median()

print("Moyenne CA par produit:",revenue_mean)
print("Médianne CA par produit", revenue_median)

product_volume = data.groupby('produit')['qte'].sum()

print()
print("Volume par produit",product_volume)

volume_mean = product_volume.mean()
volume_median = product_volume.median()
print("Moyenne volume par produit:", volume_mean)
print("Médiane volume par produit", volume_median )

volume_std = product_volume.std()
volume_var = product_volume.var()

print()
print("Ecart-type volume par produit:", volume_std)
print("Variance volument par produit:", volume_var)

# PART 6
ventes = {}
for produit, qte in zip(data['produit'], data['qte']):
    ventes[produit] = ventes.get(produit, 0) + qte

most_sold = max(ventes, key= ventes.get)
least_sold = min(ventes, key = ventes.get)

print()
print("Produit le plus vendu: ",most_sold)
print("Produit le moins vendu: ",least_sold)


# PART 7

figure1 = px.pie(data, values='qte', names='produit', title='Volume de ventes par produit')
figure1.write_html('volume_par_produit.html')

figure2 = px.pie(data, values='chiffre_affaires', names='produit', title="Chiffre d'affaires par produit"
)
figure2.write_html('ca_par_produit.html')