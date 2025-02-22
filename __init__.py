from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') 

key = Fernet.generate_key() #sss
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
  
@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes)  # Décrypte le token
        return f"Valeur décryptée : {valeur.decode()}"  # Retourne la valeur en str
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
  
@app.route('/exercice1')
def exercice1():
    return render_template('exercice1.html')


@app.route('/exercice2')
def exercice2():
    return render_template('exercice2.html')


@app.route('/exercice3')
def exercice3():
    return render_template('exercice3.html')


@app.route('/exercice4')
def exercice4():
    return render_template('exercice4.html')

@app.route('/exercice5')
def exercice5():
    return render_template('exercice5.html')

@app.route('/exemple')
def exemple():
    return render_template('Exemple_Base_SVG.html')
  
@app.route('/maison')
def maison():
    return render_template('maison.html')

@app.route('/trefle')
def trefle():
    return render_template('jack.svg')
  
@app.route('/chenille')
def chenille():
    return render_template('chenille.html')
  
@app.route('/jeu_de_des')
def jeu():
    return render_template('Jeu_Des_Base.html')

@app.route('/bibliotheque_images')
def img():
    return render_template('Outils_JS.html')
  
@app.route('/russe')
def russe():
    return render_template('Roulette_Russe_Etape_1_Barillet_Vide.html')

  

