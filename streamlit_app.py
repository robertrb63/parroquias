import requests
import streamlit as st

# Encabezado
st.title("Obispado Barbastro Monzón")

# Buscar registros
st.header("Buscar registros")
query = st.text_input("Nombre a buscar:")
if st.button("Buscar"):
    response = requests.get('https://github.com/robertrb63/parroquias/blob/main/streamlit_app.py/buscar', params={'query': query})
    resultados = response.json()
    st.write(resultados)

# Crear registros
st.header("Crear registros")
password = st.text_input("Contrasena:", type="password")
nombre = st.text_input("Nombre:")
telefono = st.text_input("Teléfono:")
email = st.text_input("Email:")
# Agrega aquí más campos según tu base de datos
if st.button("Crear"):
    nuevo_registro = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        # Agrega más campos
    }
    response = requests.post('https://github.com/robertrb63/parroquias/blob/main/streamlit_app.py/crear', json={"password": password, "registro": nuevo_registro})
    st.write(response.json())

# Actualizar y borrar registros
st.header("Actualizar y borrar registros")
# Implementa estas páginas según tus necesidades.
