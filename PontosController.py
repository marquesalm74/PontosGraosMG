from typing import List;
import services.database as db;
import models.Pontos as pts;
import pandas as pd;

def Incluir(pts):
    cursor = db.cursor.execute("""
    INSERT INTO tbl_ponto(code_muni,name_muni,data,latitude,longitude,cultura,altitude,temp_celsius,tp_safra)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
     (pts.codigo, pts.municipio,pts.data, pts.latitude, pts.longitude, pts.cultura, pts.altitude, pts.temperatura, pts.tpsafra)) #.rowcount
    db.connection.commit()
    return db.cursor.rowcount

def SelecionarTodos(pts):
    db.cursor.execute("SELECT * FROM tbl_ponto")
    consultaList = []

    for row in db.cursor.fetchall():
        consultaList.append(pts.Pontos(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

    return consultaList