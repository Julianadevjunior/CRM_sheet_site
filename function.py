import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st
from datetime import datetime
import numpy as np


# Escopos da API do Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# Corrigido: Usa os dados diretamente do st.secrets
service_account_info = st.secrets["credenciais_google_sheet"]
credentials = Credentials.from_service_account_info(service_account_info, scopes=scopes)
client = gspread.authorize(credentials)

# Pega o ID da planilha salvo nos secrets
SHEET_ID = st.secrets['credenciais_google_sheet']['sheet_id']
SHEET_NAME = "Página1"

def read_sheet():
    """Lê os dados da planilha do Google e retorna como DataFrame."""
    sheet = client.open_by_key(SHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def write_row(values):
    """Adiciona uma nova linha na planilha."""
    sheet = client.open_by_key(SHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)
    worksheet.append_row(values)

def delete_row(index):
    """Remove uma linha com base no índice (1-based)."""
    sheet = client.open_by_key(SHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)
    worksheet.delete_rows(index)


def update_row(row: int, values: list):
    """Atualiza uma linha inteira com base em uma lista de valores."""
    sheet = client.open_by_key(SHEET_ID)
    worksheet = sheet.worksheet(SHEET_NAME)

    # Define o range da linha (por exemplo, A2:K2)
    range_inicio = f"A{row}"
    range_fim = chr(ord("A") + len(values) - 1) + str(row)
    cell_range = f"{range_inicio}:{range_fim}"

    # Atualiza todas as células da linha
    worksheet.update(cell_range, [values])

def tabela():
    tabela = pd.DataFrame(read_sheet())
    return tabela

def tempo_restante(data_str):
    """Retorna o tempo restante até a data futura no formato '13-04-2025 21:54'."""
    try:
        data_futura = datetime.strptime(data_str, "%d-%m-%Y %H:%M")
        agora = datetime.now()
        delta = data_futura - agora

        if delta.total_seconds() < 0:
            return "passou"

        dias = delta.days
        horas, resto = divmod(delta.seconds, 3600)
        minutos, _ = divmod(resto, 60)

        partes = []
        if dias: partes.append(f"{dias} dia(s)")
        if horas: partes.append(f"{horas} hora(s)")
        if minutos: partes.append(f"{minutos} minuto(s)")

        return partes
    except Exception as e:
        return f"❌ Erro ao processar data: {e}"

def voltar(key):
    col1, col2 = st.columns([14.5, 3])
    with col2:
        if st.button("←voltar", key=key):
            st.switch_page(st.Page("pages/home.py"))

def bairro():
    bairros_praia_grande = [
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
    return bairros_praia_grande

def limpar_lista(valores):
    """Converte todos os itens da lista para tipos nativos do Python."""
    valores_limpos = []
    for v in valores:
        if isinstance(v, (np.integer, np.int64, np.int32)):
            valores_limpos.append(int(v))
        elif isinstance(v, (np.floating, np.float64, np.float32)):
            valores_limpos.append(float(v))
        elif isinstance(v, (bool, np.bool_)):
            valores_limpos.append(bool(v))
        else:
            valores_limpos.append(str(v))  # transforma em texto por segurança
    return valores_limpos