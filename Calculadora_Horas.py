import streamlit as st

st.set_page_config(page_title="Calculadora de Horas", layout="centered")

st.title("Calculadora de Horas - Sulan Educ")
st.write("Digite cada hora em uma linha (formato HH:MM) e clique em Calcular:")

horas_texto = st.text_area("Horas", height=200, placeholder="Exemplo:\n2:30\n1:45\n0:50")

if st.button("Calcular Total"):
    linhas = horas_texto.strip().split('\n')
    total_minutos = 0
    erro = False
    for linha in linhas:
        if not linha.strip():
            continue
        try:
            partes = linha.replace(" ", "").split(":")
            if len(partes) != 2:
                raise ValueError
            horas = int(partes[0])
            minutos = int(partes[1])
            total_minutos += horas * 60 + minutos
        except Exception:
            st.error(f"Entrada inválida: '{linha}'. Use o formato HH:MM.")
            erro = True
            break
    if not erro:
        total_horas = total_minutos // 60
        resto_minutos = total_minutos % 60
        st.success(f"**Total: {total_horas}:{resto_minutos:02d}**")

st.caption("Feito por Sulan Thronix 🕒")