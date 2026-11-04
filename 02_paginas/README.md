# Aplicação multipáginas com Streamlit

Exemplo de aplicação web feita com Streamlit para demonstrar a organização e a navegação entre páginas. 
A página inicial apresenta o aplicativo, e o menu lateral permite acessar as páginas de listagem de dados e de interação com o usuário.

## Requisitos

- Python 3.12 ou superior
- [uv](https://docs.astral.sh/uv/) instalado

## Como executar

No diretório deste projeto, execute:

```bash
uv run streamlit run Inicio.py
```

O `uv` instala e gerencia as dependências definidas em `pyproject.toml`. Depois que o servidor iniciar, acesse o endereço exibido no terminal — normalmente `http://localhost:8501`.

## Páginas

- **Página Inicial** (`Inicio.py`): apresenta o aplicativo e orienta a navegação.
- **Página de Listagem de Dados** (`pages/1_Listagem_de_Dados.py`): exibe uma tabela de exemplo com nomes e idades e oferece um botão para voltar ao início.
- **Página de Solicitação de Nome** (`pages/2_Informe_seu_nome.py`): recebe um nome e exibe uma saudação; se o campo estiver vazio, solicita o preenchimento.

As páginas dentro da pasta `pages/` são disponibilizadas no menu lateral do Streamlit.