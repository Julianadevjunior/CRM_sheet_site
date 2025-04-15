import streamlit as st
import function

if "login" not in st.session_state:
    st.session_state["login"] = False

if "id_select" not in st.session_state:
    st.session_state["id_select"] = None


lista_completa= [
    st.Page(page="pages/home.py", title="🏠 Home"),
    st.Page(page="pages/read.py", title="🔎 Informações"),
    st.Page(page="pages/creat.py", title="➕ Adicionar"),
]

with st.sidebar:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page(st.Page(page="pages/home.py"))
    if st.button("✍️ Adicionar", use_container_width=True):
        st.switch_page(st.Page(page="pages/creat.py"))



pg = st.navigation(pages=lista_completa, position="hidden")
pg.run()