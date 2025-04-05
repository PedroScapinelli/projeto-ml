import pandas as pd
import streamlit as st
from sklearn.linear_model import linearRegression

df =pd.read_csv("pizzas.csv")

modelo = linearRegression()
x = df[["diametro"]]
y = df[["preco"]]

st.title("Calculadora de preço de pizzas")
