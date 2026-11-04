import streamlit as st

st.title("Página de Solicitação de Nome")
st.write("Esta é a segunda subpágina.")

nome = st.text_input("Digite seu nome:")

# se clicar no botão "Enviar"
if st.button("Enviar"):
    # se foi preenchido o nome
    if nome:
        st.success(f"Olá, {nome}! Seja bem-vindo.")
    else:
        st.warning("Por favor, digite seu nome.")

# se clicar no botão de "Voltar"...
if st.button("Voltar ao início"):
    # "vai" para a página inicial
    st.switch_page("Inicio.py")
