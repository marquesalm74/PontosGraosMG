import streamlit as st;
from decimal import Decimal;
from sqlmodel import Field, SQLModel;
import Controllers.PontosController as PontosController;
import models.Pontos as pts;
import streamlit.components.v1 as componets;
import pandas as pd;

def Incluir():
    st.title('QUESTIONÁRIO SUBJETIVO')
    with st.form(key="include_pontos") :
        input_code = st.text_input(label='Insira o Codigo do Município') # type: ignore
        input_name = st.text_input(label='Insira o nome do Município') # type: ignore
        input_date = st.date_input(label="Insira a Data do Registro", format="DD/MM/YYYY") # type: ignore
        input_lat =  st.number_input(label="Insira a Latitude", format='%3f') # type: ignore
        input_long = st.number_input(label="Insira a Longitude", format='%3f') # type: ignore
        input_tpsafra = st.selectbox("Selecione o Tipo de Safra", ['Safra Verão','Safrinha']) # type: ignore
        input_cultura = st.selectbox("Selecione a Cultura", ['','Algodão','Amendoim','Arroz','Feijão 1','Feijão 2','Feijão 3','Girassol','Milho 1','Milho 2','Soja','Sorgo','Trigo']) # type: ignore
        input_altitude = st.number_input("Insira a Altitude", format='%d', step=1) # type: ignore
        input_temp = st.number_input("Digite a Temperatura Celsius") # type: ignore
        input_button_submit = st.form_submit_button('Enviar Dados')