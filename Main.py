import streamlit as st
import pandas as pd

dados = [
    ["Alexandre Guimarães Didier", 10, 10, 8, 10, 7, 8.25, "Bom"],
    ["Almir Vinicius Rodrigues Barbosa", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Ane Gabriele Andrade Reis", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Bruna Fernandes de Oliveira", 10, 10, 10, 10, 6, 8, "Bom"],
    ["Camila de Lima Silva", 0, 10, 0, 10, 5, 5, "Ainda não suficiente"],
    ["Cíntia H de Souza", 10, 10, 10, 10, 4, 7, "Bom"],
    ["Cristiane Rodrigues da Costa Araújo", 10, 10, 9, 10, 2, 5.875, "Ainda não suficiente"],
    ["Daiane Maria da Silva", 10, 10, 10, 10, 7, 8.5, "Ótimo"],
    ["Danilo Elisio da Costa", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Edvaldo Alves Carvalho Filho", 10, 10, 10, 10, 6, 8, "Bom"],
    ["Emerson de Andrade", 10, 10, 10, 10, 6, 8, "Bom"],
    ["Emerson Radamés Ramos de Alencar", 0, 0, 0, 0, 0, 0, "Insuficiente"],
    ["Fabíola Gomes Pereira de Lima", 10, 10, 10, 10, 7, 8.5, "Ótimo"],
    ["Hugo Alessandro Menezes de Oliveira", 10, 0, 0, 0, 0, 1.25, "Insuficiente"],
    ["Hugo Marques Araújo Silva", 0, 0, 0, 0, 7, 3.5, "Insuficiente"],
    ["Iale Conceição de Sales", 10, 0, 10, 0, 6, 5.5, "Ainda não suficiente"],
    ["Ísis Noemia Gomes de Lima", 10, 10, 10, 10, 4, 7, "Bom"],
    ["Jakeane da Silva Siqueira", 10, 10, 10, 0, 3, 5.25, "Ainda não suficiente"],
    ["Jefferson Tude de Lima", 10, 10, 10, 10, 9, 9.5, "Excelente"],
    ["João Paulo da Cruz Souto Maior", 0, 0, 0, 0, 6, 3, "Insuficiente"],
    ["João Victor Araújo de Lima", 0, 10, 0, 10, 8, 6.5, "Ainda não suficiente"],
    ["Joselia Xavier de Freitas", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Karina Maria da Silva", 10, 10, 10, 10, 6, 8, "Bom"],
    ["Luciana Rocha Falcão", 10, 10, 10, 10, 5, 7.5, "Bom"],
    ["Lucrecia de Lira Gomes", 0, 0, 0, 0, 0, 0, "Insuficiente"],
    ["Luiza de Oliveira Pontes Pessoa", 10, 10, 10, 10, 7, 8.5, "Ótimo"],
    ["Luiza Ramos Pontual", 10, 10, 10, 10, 7, 8.5, "Ótimo"],
    ["Maria das Graças Batista da Silva", 10, 10, 10, 10, 9, 9.5, "Excelente"],
    ["Maria do Carmo de Oliveira", 10, 10, 10, 10, 9, 9.5, "Excelente"],
    ["Maria Eduarda Tavares de Freitas", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Mariana Claudino Pereira Sabino", 10, 10, 10, 10, 4, 7, "Bom"],
    ["Marlon Pereira da Silva", 10, 10, 10, 10, 4, 7, "Bom"],
    ["Paula Brito Smethurst", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Priscilla Rebeka Alves da Silva", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Rafael Moraes de Araújo", 10, 10, 10, 10, 6, 8, "Bom"],
    ["Ricardo Antônio Ferreira dos Santos", 10, 0, 10, 0, 9, 7, "Bom"],
    ["Sheylanne Gomes do Nascimento", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Soraya Magno Bezerra da Silva", 10, 10, 10, 10, 5, 7.5, "Bom"],
    ["Soraia Pereira de Carvalho", 0, 0, 0, 0, 0, 0, "Insuficiente"],
    ["Steven Ramos Bonfim", 10, 10, 10, 0, 6, 6.75, "Bom"],
    ["Tayná Mendes Chagas", 10, 10, 10, 10, 4, 7, "Bom"],
    ["Thais de Freitas Lima", 10, 10, 10, 10, 5, 7.5, "Bom"],
    ["Vanderlucia Cavalcanti de França Freitas", 10, 10, 10, 10, 4, 7, "Bom"],
    ["Vinicius Matheus da Silva Cabral", 0, 0, 0, 0, 6, 3, "Insuficiente"],
    ["Vitória Caroline Sales", 10, 10, 10, 10, 8, 9, "Ótimo"],
    ["Melquisedeque", 10, 0, 0, 0, 5, 3.75, "Insuficiente"],
    ["Jozias Ferreira da Silva", 0, 10, 0, 0, 7, 4.75, "Insuficiente"],
    ["Josias Florêncio Costa Filho", 10, 0, 0, 0, 9, 5.75, "Insuficiente"]
]

colunas = [
    "Nome",
    "Tarefa 1",
    "Fórum 1",
    "Tarefa 2",
    "Fórum 2",
    "Teste",
    "NF",
    "Menção"]

df = pd.DataFrame(dados, columns=colunas)

# Transformar coluna Nome em maiúsculo
df["Nome"] = df["Nome"].astype(str).str.upper().str.strip()

st.title("Consulta de Notas")

# Campo de busca
nome = st.text_input("Digite seu nome completo")

if nome:

    # Converter entrada do usuário para maiúsculo
    nome = nome.upper().strip()

    # Buscar aluno
    resultado = df[df["Nome"] == nome]

    if not resultado.empty:

        st.success("Aluno encontrado!")

        # Mostrar linha inteira
        st.dataframe(
            resultado,
            use_container_width=True
        )

    else:
        st.error("Nome não encontrado.")
