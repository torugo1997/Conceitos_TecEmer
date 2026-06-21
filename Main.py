import streamlit as st
import pandas as pd
import unicodedata

Parte1=[['NOME DO ALUNO (A)', 'Tarefa 1', 'Fórum1', 'Tarefa 2', 'Fórum 2', 'Teste', 'NF', 'Conceito'],
['Alexandre Guimarães Didier', 10, 10, 8, 10, 7, 8.25, 'Bom'],
['Almir Vinicius Rodrigues Barbosa', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Ane Gabriele Andrade Reis', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Bruna Fernandes de Oliveira', 10, 10, 10, 10, 6, 8, 'Bom'],
['Camila de Lima Silva', 0, 10, 0, 10, 5, 5, 'Ainda não suficiente'],
['Cíntia H de Souza', 10, 10, 10, 10, 4, 7, 'Bom'],
['Cristiane Rodrigues da Costa Araújo', 10, 10, 9, 10, 2, 5.875, 'Ainda não suficiente'],
['Daiane Maria da Silva', 10, 10, 10, 10, 7, 8.5, 'Ótimo'],
['Danilo Elisio da Costa', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Edvaldo Alves Carvalho Filho', 10, 10, 10, 10, 6, 8, 'Bom'],
['Emerson de Andrade', 10, 10, 10, 10, 6, 8, 'Bom'],
['Emerson Radamés Ramos de Alencar', 0, 0, 0, 0, 0, 0, 'Insuficiente'],
['Fabíola Gomes Pereira de Lima', 10, 10, 10, 10, 7, 8.5, 'Ótimo'],
['Hugo Alessandro Menezes de Oliveira', 10, 0, 0, 0, 0, 1.25, 'Insuficiente'],
['Hugo Marques Araújo Silva', 0, 0, 0, 0, 7, 3.5, 'Insuficiente'],
['Iale Conceição de Sales', 10, 0, 10, 0, 6, 5.5, 'Ainda não suficiente'],
['Ísis Noemia Gomes de Lima', 10, 10, 10, 10, 4, 7, 'Bom'],
['Jakeane da Silva Siqueira', 10, 10, 10, 0, 3, 5.25, 'Ainda não suficiente'],
['Jefferson Tude de Lima', 10, 10, 10, 10, 9, 9.5, 'Excelente'],
['João Paulo da Cruz Souto Maior', 0, 0, 0, 0, 6, 3, 'Insuficiente'],
['João Victor Araújo de Lima', 0, 10, 0, 10, 8, 6.5, 'Ainda não suficiente'],
['Joselia Xavier de Freitas', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Karina Maria da Silva', 10, 10, 10, 10, 6, 8, 'Bom'],
['Luciana Rocha Falcão', 10, 10, 10, 10, 5, 7.5, 'Bom'],
['Luiza de Oliveira Pontes Pessoa', 10, 10, 10, 10, 7, 8.5, 'Ótimo'],
['Luiza Ramos Pontual', 10, 10, 10, 10, 7, 8.5, 'Ótimo'],
['Maria das Graças Batista da Silva', 10, 10, 10, 10, 9, 9.5, 'Excelente'],
['Maria do Carmo de Oliveira', 10, 10, 10, 10, 9, 9.5, 'Excelente'],
['Maria Eduarda Tavares de Freitas', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Mariana Claudino Pereira Sabino', 10, 10, 10, 10, 4, 7, 'Bom'],
['Marlon Pereira da Silva', 10, 10, 10, 10, 4, 7, 'Bom'],
['Paula Brito Smethurst', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Priscilla Rebeka Alves da Silva', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Rafael Moraes de Araújo', 10, 10, 10, 10, 6, 8, 'Bom'],
['Ricardo Antônio Ferreira dos Santos', 10, 0, 10, 0, 9, 7, 'Bom'],
['Sheylanne Gomes do Nascimento', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Soraya Magno Bezerra da Silva', 10, 10, 10, 10, 5, 7.5, 'Bom'],
['Steven Ramos Bonfim', 10, 10, 10, 0, 6, 6.75, 'Bom'],
['Tayná Mendes Chagas', 10, 10, 10, 10, 4, 7, 'Bom'],
['Thais de Freitas Lima', 10, 10, 10, 10, 5, 7.5, 'Bom'],
['Vanderlucia Cavalcanti de França Freitas', 10, 10, 10, 10, 4, 7, 'Bom'],
['Vinicius Matheus da Silva Cabral', 0, 0, 0, 0, 6, 3, 'Insuficiente'],
['Vitória Caroline Sales', 10, 10, 10, 10, 8, 9, 'Ótimo'],
['Jozias Ferreira da Silva', 0, 10, 0, 0, 7, 4.75, 'Insuficiente'],
['Josias Florêncio Costa Filho', 10, 0, 0, 0, 9, 5.75, 'Insuficiente']]

Parte2=[['NOME DO ALUNO (A)', 'Apresentação PI', 'Fórum1', 'Fórum 2', 'Fórum 3', 'Tarefa 1', 'Tarefa 2', 'Tarefa 3', 'Tarefa 4', 'NF'],
['Alexandre Guimarães Didier', 8, 0, 10, 0, 10, 10, 10, 8, 6.94375],
['Almir Vinicius Rodrigues Barbosa', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Ane Gabriele Andrade Reis', 10, 0, 10, 0, 10, 10, 10, 0, 6.94375],
['Bruna Fernandes de Oliveira', 10, 0, 10, 0, 10, 10, 10, 8, 7.61035],
['Camila de Lima Silva', 10, 10, 10, 0, 10, 0, 10, 0, 7.2215],
['Cíntia H de Souza', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Cristiane Rodrigues da Costa Araújo', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Daiane Maria da Silva', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Danilo Elisio da Costa', 10, 0, 10, 0, 10, 10, 10, 0, 6.94375],
['Edvaldo Alves Carvalho Filho', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Emerson de Andrade', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Emerson Radamés Ramos de Alencar', 10, 10, 10, 0, 10, 0, 0, 8, 7.05485],
['Fabíola Gomes Pereira de Lima', 10, 0, 10, 0, 10, 0, 0, 10, 6.1105],
['Hugo Alessandro Menezes de Oliveira', 10, 0, 10, 0, 10, 0, 0, 0, 5.27725],
['Hugo Marques Araújo Silva', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Iale Conceição de Sales', 10, 10, 10, 10, 10, 10, 10, 10, 9.999],
['Ísis Noemia Gomes de Lima', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Jakeane da Silva Siqueira', 10, 0, 10, 0, 8, 10, 10, 10, 7.61035],
['Jefferson Tude de Lima', 10, 10, 10, 0, 10, 10, 10, 0, 8.05475],
['João Paulo da Cruz Souto Maior', 10, 0, 10, 0, 0, 0, 10, 0, 5.27725],
['João Victor Araújo de Lima', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Joselia Xavier de Freitas', 10, 0, 10, 0, 10, 10, 0, 10, 6.94375],
['Karina Maria da Silva', 10, 10, 10, 10, 10, 10, 10, 10, 9.999],
['Luciana Rocha Falcão', 10, 0, 10, 0, 10, 10, 10, 0, 6.94375],
['Luiza de Oliveira Pontes Pessoa', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Luiza Ramos Pontual', 8, 10, 10, 10, 10, 10, 10, 10, 9.3324],
['Maria das Graças Batista da Silva', 8, 10, 10, 10, 10, 10, 10, 10, 9.3324],
['Maria do Carmo de Oliveira', 8, 10, 10, 10, 10, 10, 10, 10, 9.3324],
['Maria Eduarda Tavares de Freitas', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Mariana Claudino Pereira Sabino', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Marlon Pereira da Silva', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Paula Brito Smethurst', 10, 0, 10, 0, 10, 0, 10, 10, 6.94375],
['Priscilla Rebeka Alves da Silva', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Rafael Moraes de Araújo', 10, 10, 10, 0, 10, 10, 10, 0, 8.05475],
['Ricardo Antônio Ferreira dos Santos', 10, 0, 10, 0, 10, 10, 10, 0, 6.94375],
['Sheylanne Gomes do Nascimento', 10, 0, 10, 0, 10, 0, 0, 10, 6.1105],
['Soraya Magno Bezerra da Silva', 8, 0, 10, 10, 10, 10, 10, 9, 8.138075],
['Steven Ramos Bonfim', 10, 10, 10, 0, 10, 10, 10, 0, 9.16575],
['Tayná Mendes Chagas', 10, 10, 10, 10, 10, 10, 10, 10, 9.999],
['Thais de Freitas Lima', 10, 0, 10, 0, 10, 10, 10, 8, 7.61035],
['Vanderlucia Cavalcanti de França Freitas', 10, 0, 10, 0, 10, 10, 0, 10, 6.94375],
['Vinicius Matheus da Silva Cabral', 10, 0, 10, 0, 10, 0, 10, 0, 6.1105],
['Vitória Caroline Sales', 10, 0, 10, 0, 10, 10, 10, 10, 7.777],
['Jozias Ferreira da Silva', 10, 0, 10, 0, 10, 0, 0, 0, 5.27725],
['Josias Florêncio Costa Filho', 10, 0, 10, 0, 10, 10, 0, 10, 6.94375]]

def normalizar(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).strip().lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto

st.set_page_config(page_title="Tecnologias Emergentes Aplicadas à Gestão", layout="wide")

col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/86/Senac_logo.svg", width=180)

with col2:
    st.title("Tecnologias Emergentes Aplicadas à Gestão")
    st.markdown("Consulta de notas")

nome_usuario = st.text_input("Digite seu nome completo")


if nome_usuario:
    nome_busca = normalizar(nome_usuario)
    for i in range(1,len(Parte1),1):
        if (normalizar(Parte1[i][0])==normalizar(nome_busca)):
            break

    if i>=len(Parte1):
        st.error("Nome não encontrado.")
    else:
        st.success("Aluno encontrado!")
        st.subheader("Parte 1")
        c1,c2,c3,c4,c5,c6,c7=st.columns(7)
        with c1:
            st.write("Tarefa 1")
            st.write(Parte1[i][1])
        with c2:
            st.write("Fórum 1")
            st.write(Parte1[i][2])
        with c3:
            st.write("Tarefa 2")
            st.write(Parte1[i][3])
        with c4:
            st.write("Fórum 2")
            st.write(Parte1[i][4])
        with c5:
            st.write("Teste")
            st.write(Parte1[i][5])
        with c6:
            st.write("Nota Final")
            st.write(Parte1[i][6])
        with c7:
            st.write("Conceito")
            st.write(Parte1[i][7])    
        st.subheader("Parte 2")
        c0,c1,c2,c3,c4,c5,c6,c7,c8,c9=st.columns(10)
        with c0:
            st.write("Apresentação PI")
            st.write(Parte2[i][1])
        with c1:
            st.write("Fórum 1")
            st.write(Parte2[i][2])
        with c2:
            st.write("Fórum 2")
            st.write(Parte2[i][3])
        with c3:
            st.write("Fórum 3")
            st.write(Parte2[i][4])
        with c4:
            st.write("Tarefa 1")
            st.write(Parte2[i][5])
        with c5:
            st.write("Tarefa 2")
            st.write(Parte2[i][6])
        with c6:
            st.write("Tarefa 3")
            st.write(Parte2[i][7])
        with c7:
            st.write("Tarefa 4")
            st.write(Parte2[i][8])
        with c8:
            st.write("NF")
            st.write(Parte2[i][9])
        with c9:
            if Parte2[i][9]<4.99:
                Conceito="Insuficiente"
            else:
                if Parte2[i][9]<6.99:
                    Conceito="Ainda não Suficiente"
                else:
                    if Parte2[i][9]<8.49:
                        Conceito="Bom"
                    else:
                        if Parte2[i][9]<9.49:
                            Conceito="Ótimo"
                        else:
                            Conceito="Excelente"
            st.write("Conceito")
            st.write(Conceito)
        st.subheader("Conceito Final")
        st.write(0.5*Parte1[i][6]+0.5*Parte2[i][9])
