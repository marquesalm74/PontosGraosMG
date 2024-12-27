import streamlit as st;
from decimal import Decimal;
from sqlmodel import Field, SQLModel;
import Controllers.PontosController as PontosController;
import models.Pontos as pts;
import streamlit.components.v1 as componets;
import pandas as pd;

def List():
    st.title('PONTOS')
    consultaList = []

    for item in PontosController.SelecionarTodos(pts):
        consultaList.append([item.codigo,item.municipio,item.data,item.latitude,item.longitude,item.cultura,item.altitude,item.temperatura,item.tpsafra])

    df = pd.DataFrame(
        consultaList,
        columns= ['codigo','municipio','data','latitude','longitude','cultura','altitude','temperatura','tp_safra',]
    )

    st.table(df)