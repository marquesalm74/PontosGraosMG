from os import write;
from numpy.core.fromnumeric import size;
import streamlit as st;
from decimal import Decimal;
from sqlmodel import Field, SQLModel;
import Controllers.PontosController as PontosController;
import models.Pontos as pts;
import streamlit.components.v1 as componets;
import pandas as pd;
import Pages.Ponto.Create as PageCreatePonto;
import Pages.Ponto.List as PageListPonto;


class Model(SQLModel):
    dec: Decimal = Field(max_digits=4, decimal_places=2)


st.sidebar.title('MENU')
Page_ponto = st.sidebar.selectbox("PONTOS",['Incluir', 'Consultar'])

st.sidebar.title('MENU')
Page_quest = st.sidebar.selectbox("QUESTIONÁRIO",['SUBJETIVO', 'OBJETIVO'])

###################################################################
# Consulta de pontos cadastrados com seus id's
###################################################################
if Page_ponto == "Consultar":
    PageListPonto.List()

###################################################################
#  Incluir os pontos para cadastrar no DB de Pontos
###################################################################
if Page_ponto == 'Incluir':
    PageCreatePonto.Incluir()

###################################################################
#  Deletar os dados a partir do ID
###################################################################



###################################################################
#  Alterar os dados a partir do ID
###################################################################