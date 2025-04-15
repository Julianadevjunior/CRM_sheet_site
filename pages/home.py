import streamlit as st
import function
import datetime
import pandas as pd

st.markdown("<h2 style='text-align:center; font-sizer:30px; padding: 0px 0px'><b>🏠</b></h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#3e9be9'><b>List Lead</b></h2>", unsafe_allow_html=True)

for item in function.tabela().values:
    id, nome, telefone, email, valor, quartos, bairro, visita, data, upload, nota = item


    if "dia" in function.tempo_restante(upload)[0]:
        aviso = "#46ff5ac9"

    if "dia" not in function.tempo_restante(upload)[0]:
        aviso = "#fffc46c9"

    if function.tempo_restante(upload) == "passou":
        aviso = "#ff4646c9"

    if visita == "excluir":
        aviso = "#dedede"


    with st.container(border=True):
        st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0; background:{aviso}; border-radius:25px'>
        <div>👤<b>ID</b>: {id}</div>
        <div><b>Data de retorno</b>: {upload}</div>
        </div>
        <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0;'>
            <div><b>Nome</b>: {nome}</div>
            <div><b>Telefone</b>: {telefone}</div>
        </div>
            <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0;'>
            <div><b>Bairro</b>: {bairro}</div>
            <div><b>Valor</b>: R${float(valor):.2f}</div>
        </div>       
        """, unsafe_allow_html=True)
        if st.button("Detalhes", key=f"lead_{id}", use_container_width=True):
            st.session_state["id_select"] = id
            st.switch_page(st.Page("pages/read.py"))



