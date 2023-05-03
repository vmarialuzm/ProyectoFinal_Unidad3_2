from flask import Blueprint,render_template,flash,redirect,url_for
from app.models.character import Character
from app.db import db
import requests

character_router = Blueprint("character_router",__name__)

@character_router.route("/")
def principal():
    return render_template("principal.html")

#------------------------------------------------------------
@character_router.route("/listar")
def listar():
    characters = db.coleccion_character.find()

    return render_template("listar.html", characters=characters)

#------------------------------------------------------------

@character_router.route("/perfil/<id>")
def perfil(id):
    perfi_character = db.coleccion_character.find_one({"name": id})
    return render_template("perfil.html",perfi_character=perfi_character)

#------------------------------------------------------------
url="https://rickandmortyapi.com/api/character?page="

@character_router.route("/cargar",methods=['GET', 'POST'])
def cargar_json_bd():
    for num in range(1,22):
        response=requests.get(url+str(num))

        if response.status_code==200:
            response_json=response.json()
            
            for result in response_json["results"]:
                lista_character=Character(
                result["name"],
                result["status"],
                result["species"],
                result["origin"]["name"],
                result["location"]["name"],
                result["image"]
                )

            # vamos a insertar todos los documentos en la coleccion_character
                db.coleccion_character.insert_one(lista_character.to_json())

    flash("Carga exitosa","success")

    return render_template("principal.html")
        
#------------------------------------------------------------
@character_router.route("/delete")
def eliminar_coleccion():
    db.coleccion_character.drop()
    
    flash("Eliminado correctamente","success")
    return render_template("principal.html")

