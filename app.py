import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance


# Titres
st.title("Iris")
st.subheader("Analyse exploratoire de données (EDA)")


# EDA
my_dataset = "iris.csv"

# To Improve speed and cache data
@st.cache(persist=True)
def explore_data(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df 


# Visualiser les parties du Dataset
if st.checkbox("Visualiser les extrémités du DataFrame"):
	data = explore_data(my_dataset)
	if st.button("Head"):
		st.write(data.head())
	if st.button("Tail"):
		st.write(data.tail())
	else:
		st.write(data.head(2))

# Afficher le Dataset
if st.checkbox("Afficher tout le DataFrame"):
	data = explore_data(my_dataset)
	st.dataframe(data)

# Description du Dataset
if st.checkbox("Afficher le nom des colonnes"):
	data = explore_data(my_dataset)
	st.text("Colonnes:")
	st.write(data.columns)

# Dimensions du Dataset
data_dim = st.radio('Afficher le nombre de lignes et de colonnes',('Lignes','Colonnes'))
if data_dim == 'Lignes':
	data = explore_data(my_dataset)
	st.text("Nombre de lignes")
	st.write(len(data))
if data_dim == 'Colonnes':
	data = explore_data(my_dataset)
	st.text("Nombre de colonnes")
	st.write(data.shape[1])


if st.checkbox("Résumé du Dataset"):
	data = explore_data(my_dataset)
	st.write(data.describe())

# Selection des espèces
species_option = st.selectbox('Selection des colonnes',('sepal_length','sepal_width','petal_length','petal_width','species'))
data = explore_data(my_dataset)
if species_option == 'sepal_length':
	st.write(data['sepal_length'])
elif species_option == 'sepal_width':
	st.write(data['sepal_width'])
elif species_option == 'petal_length':
	st.write(data['petal_length'])
elif species_option == 'petal_width':
	st.write(data['petal_width'])
elif species_option == 'species':
	st.write(data['species'])
else:
	st.write("Selectionnez une colonne")

# Affichage des graphiques
if st.checkbox("Diagramme Bar Plot avec Matplotlib "):
	data = explore_data(my_dataset)
	data.plot(kind='bar')
	st.pyplot()
	st.set_option('deprecation.showPyplotGlobalUse', False)


# Affichage des graphiques
if st.checkbox("Graphique de corrélation (Matplotlib) "):
	data = explore_data(my_dataset)
	plt.matshow(data.corr())
	st.pyplot()

# Affichage des graphiques
if st.checkbox("Graphique de correlation (Seaborn) "):
	data = explore_data(my_dataset)
	st.write(sns.heatmap(data.corr(),annot=True))
	# Use Matplotlib to render seaborn
	st.pyplot()

# Traitement des images d'Iris
@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im

# Images des différentes espèces
species_type = st.radio("Choisissez l'espèce d'Iris à afficher?",('Setosa','Versicolor','Virginica'))

if species_type == 'Setosa':
	st.text("Affichage de l'espèce Setosa")
	st.image(load_image('imgs/iris_setosa.jpg'))
elif species_type == 'Versicolor':
	st.text("Affichage de l'espèce Versicolor")
	st.image(load_image('imgs/iris_versicolor.jpg'))
elif species_type == 'Virginica':
	st.text("Affichage de l'espèce Virginica")
	st.image(load_image('imgs/iris_virginica.jpg'))


# Afficher l'image
if st.checkbox("Afficher / Cacher l'image"):
	my_image = load_image('./imgs/iris_setosa.jpg')
	enh = ImageEnhance.Contrast(my_image)
	num = st.slider("Ajuster le contraste",1.0,3.0)
	img_width = st.slider("Ajuster la taille de l'image",300,500)
	st.image(enh.enhance(num),width=img_width)


# A propos

if st.button("A propos"):
	st.subheader("Analyse exploratoire des données d'Iris")
	st.text("Réalisée avec Streamlit")
	st.text("J@m sialorama-at-gmail-dot-com")
	
	
