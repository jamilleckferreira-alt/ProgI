import streamlit as st

# configuração da página inicial:
# título e layout
st.set_page_config(page_title="Meu Aplicativo")

# título da página (H1)
st.title("Página Inicial")
# texto mostrado na página
st.write("Bem-vindo ao meu aplicativo Streamlit!")

# texto usando markdown
st.markdown("""
Este é um exemplo de aplicação com três páginas.

Utilize o menu lateral para navegar entre elas:
- Página 1: apresentação de dados.
- Página 2: interação com o usuário.
""")

# texto de informação
st.info("Selecione uma página no menu lateral para começar.")