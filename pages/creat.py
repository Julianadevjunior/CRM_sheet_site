import streamlit as st
import function
import datetime
import pandas as pd

bairro = function.bairro()

function.voltar("page_creat")

idx = 0
lista_ids = list(function.tabela()["id"])

for item in range(0, 1000):
    if item not in lista_ids:
        idx = item
        break


st.markdown("<h2 style='text-align:center; font-sizer:30px; padding: 0px 0px'><b>✍️</b></h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#3e9be9'><b>New Lead</b></h2>", unsafe_allow_html=True)
with st.container(border=True):
    st.text(f"cod: {idx}")
    nome = st.text_input(label="Nome", placeholder="Digite o nome")
    telefone = st.text_input(label="Telefone", placeholder="Digite o Telefone")
    email = st.text_input(label="E-mail", placeholder="Digite o e-mail")
    valor = st.text_input(label="Valor", placeholder="Digite o valor")
    quarto = st.radio(label="Quartos", options=[1, 2, 3, 4, 5], horizontal=True)
    bairro = st.selectbox(label="Bairro", options=bairro)
    visita = st.checkbox(label="Agendou visita", value=["sim", "não"])
    entrada = datetime.datetime.now().today().strftime("%d-%m-%Y %H:%M")
    update = datetime.datetime.now().today().strftime("%d-%m-%Y %H:%M")
    nota = None

    if all([nome, telefone, email, valor, quarto, bairro]):
        if st.button("Cadastrar", key="Cadastrar", use_container_width=True):
            function.write_row([idx, nome, telefone, email, valor, quarto, bairro, visita, entrada, update, nota])
            st.success("completo")

