import json
from flask import Flask, request, jsonify
import streamlit as st

# Configuración de Flask
app = Flask(__name__)

# Ruta para cargar la base de datos
def cargar_db():
    with open('db.json', 'r') as f:
        return json.load(f)

# Ruta para guardar en la base de datos
def guardar_db(data):
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)

# Endpoint para buscar
@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('query', '')
    data = cargar_db()
    resultados = [item for item in data if query.lower() in item['parroquia'].lower()]
    return jsonify(resultados)

# Endpoint para crear nuevo registro
@app.route('/crear', methods=['POST'])
def crear():
    password = request.json.get('password', '')
    if password != 'contraseña_segura':  # Cambia por tu contraseña segura
        return jsonify({"error": "Contraseña incorrecta"}), 403
    
    nuevo_registro = request.json.get('registro', {})
    data = cargar_db()
    data.append(nuevo_registro)
    guardar_db(data)
    return jsonify({"mensaje": "Registro creado exitosamente"})

# Endpoint para actualizar registro
@app.route('/actualizar', methods=['PUT'])
def actualizar():
    id_registro = request.json.get('id', None)
    nuevos_datos = request.json.get('registro', {})
    data = cargar_db()

    for item in data:
        if item['id'] == id_registro:
            item.update(nuevos_datos)
            guardar_db(data)
            return jsonify({"mensaje": "Registro actualizado exitosamente"})

    return jsonify({"error": "Registro no encontrado"}), 404

# Endpoint para borrar registro
@app.route('/borrar', methods=['DELETE'])
def borrar():
    id_registro = request.json.get('id', None)
    data = cargar_db()

    data = [item for item in data if item['id'] != id_registro]
    guardar_db(data)
    return jsonify({"mensaje": "Registro eliminado exitosamente"})


if __name__ == '__main__':
    app.run()
