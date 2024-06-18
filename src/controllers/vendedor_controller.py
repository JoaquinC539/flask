from flask import Blueprint, jsonify,request
from src.config.db import get_db_connection


vendedor_bp=Blueprint("vendedor",__name__)

@vendedor_bp.route("/vendedor",methods=["GET"])
def index():
    try:    
        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM vendedores ORDER BY _id DESC")
        vendedores=cursor.fetchall()
        cursor.close()
        conn.close()
        response=jsonify(vendedores)
        response.status_code=201
        return response
    except Exception as error:
        return error
@vendedor_bp.route("/vendedor",methods=["POST"])
def save():
    
    data=request.get_json()
    nombre=data["nombre"]
    apellido=data["apellido"]
    edad=data["edad"]
    correo_electronico=data["correo_electronico"]
    activo=data["activo"] if data["activo"] is not None else True 
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO vendedores (nombre,apellido,edad,correo_electronico,activo) VALUES (%s,%s,%s,%s,%s) RETURNING *",(nombre,apellido,edad,correo_electronico,activo) )
    vendedor=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(vendedor)
