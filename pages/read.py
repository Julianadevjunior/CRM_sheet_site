import datetime
import streamlit as st
import function

st.markdown("<h2 style='text-align:center; font-sizer:30px; padding: 0px 0px'><b>✍🔎</b></h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#3e9be9'><b>Dados Lead</b></h2>", unsafe_allow_html=True)
idx = st.session_state["id_select"]

function.voltar("page_read")
id, nome, telefone, email, valor, quartos, bairro, visita, data, upload, nota = list(function.tabela().loc[idx])

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
        <div><b>E-mail</b>: {email}</div>
    </div>
        <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0;'>
        <div><b>Bairro</b>: {bairro}</div>
        <div><b>Valor</b>: R${float(valor):.2f}</div>
        <div><b>Quartos</b>: {quartos}</div>
    </div>
        </div>
        <div style='border:2px solid #ccc; border-radius: 8px; padding: 30px; display: flex; justify-content: space-between; align-items: center; padding: 10px 0; padding: 10px;'>
        <div><b>Anotações</b>: {nota}</div>
    </div>
        </div>
        <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px 0;'>
        <div><b>Data de entrada</b>: {data}</div>
    """, unsafe_allow_html=True)
    linha = idx + 2

    with st.expander(label="Atualizar informações"):
        with st.form(border=True, key="formulario_atualizacao", clear_on_submit=True):
            bairros_praia_grande = [
                bairro,
                "Anhanguera",
                "Antártica",
                "Balneário Flórida",
                "Balneário Maracanã",
                "Balneário Monte Carlo",
                "Balneário São Jorge",
                "Boqueirão",
                "Caiçara",
                "Canto do Forte",
                "Esmeralda",
                "Guilhermina",
                "Jardim Anhanguera",
                "Jardim Imperador",
                "Jardim Melvi",
                "Jardim Real",
                "Jardim Ribeirópolis",
                "Jardim Samambaia",
                "Jardim Solemar",
                "Jardim Trevo",
                "Maracanã",
                "Mirim",
                "Nova Mirim",
                "Ocian",
                "Quietude",
                "Real",
                "Ribeirópolis",
                "Samambaia",
                "Solemar",
                "Tupi",
                "Vila Antártica",
                "Vila Caicara",
                "Vila Guilhermina",
                "Vila Mirim",
                "Vila Sônia"
            ]

            data_convertida = datetime.datetime.strptime(upload, "%d-%m-%Y %H:%M")

            st.markdown("<h3 style='text-align:center; color:#3e9be9'><b>Digite as informações que você deseja mudar</b></h3>", unsafe_allow_html=True)
            col4, col5 = st.columns([1, 1])
            with col4:
                new_nome = st.text_input("Insira o novo nome")
                new_valor = st.text_input("Insira o novo valor")
                new_email = st.text_input("Insira o novo e-mail")
                nova_dia = st.date_input("Insira a data", value=data_convertida, format="DD/MM/YYYY")


            with col5:
                new_telefone = st.text_input("Insira o novo telefone")
                new_quarto = st.radio("Quartos", options=[quartos, 1, 2, 3, 4, 5], horizontal=True)
                new_bairro = st.selectbox("Bairros", options=bairros_praia_grande)
                nova_hora = st.time_input(label="Insira a hora", value=data_convertida)
            new_anotacoes = st.text_area("Insira o nova anotação")
            col6, col7 = st.columns([1, 1])
            with col6:
                new_visita = st.checkbox("Agendou visita")
            with col7:
                new_excluir = st.checkbox("Lead não qualificado")
            new_data = f"{nova_dia.strftime("%d-%m-%Y")} {nova_hora.strftime("%H:%M")}"

            dados_form = [id, new_nome, new_telefone, new_email, new_valor, new_quarto, new_bairro, new_visita, data, new_data, new_anotacoes]
            dados = [id, nome, telefone, email, valor, quartos, bairro, visita, data, upload, nota]
            cont = 0
            if st.form_submit_button("Atualizar"):
                for coluna, dado in enumerate(dados_form):
                    if dado == "":
                        pass
                    else:
                        dados[coluna] = dado
                if new_excluir == True:
                    dados[7] = "excluir"

                valores_limpos = function.limpar_lista(dados)
                function.update_row(linha, valores_limpos)
                st.success("Atualizado com sucesso!!!")
                st.rerun()




    # id 1
    # nome 2
    # telefone 3
    # email 4
    # valor 5
    # quarto 6
    # bairro 7
    # visita 8
    # entrada 9
    # update 10
    # anotações 11


