import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da Página
st.set_page_config(page_title="Encontrando Meu Propósito", page_icon="🌱", layout="centered")

# Estilização
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background-color: #4A90E2; color: white; border-radius: 20px; width: 100%; }
    .stProgress > div > div > div > div { background-color: #7ED321; }
    .card { background-color: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_stdio=True)

# Estado do App
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'points' not in st.session_state:
    st.session_state.points = 0

def next_step():
    st.session_state.step += 1
    st.session_state.points += 20

# Interface
st.title("🌱 Encontrando Meu Propósito")
st.write(f"Olá, André! Vamos caminhar juntos nesta jornada.")

# Barra de Progresso
progress = (st.session_state.step - 1) / 5
st.progress(progress)
badges = ["", "Explorador 🧭", "Investigador 🔍", "Descobridor 💡", "Visionário 🔭", "Arquiteto 🏗️"]
st.write(f"**Status:** {badges[st.session_state.step if st.session_state.step <= 5 else 5]} | **Pontos:** {st.session_state.points}")

# --- TELAS ---

if st.session_state.step == 1:
    st.header("Dia 1: O Que Te Move")
    q1 = st.text_area("O que te faz sair da cama de manhã?", placeholder="Ex: Meu filho, meu trabalho, um desejo...")
    q2 = st.multiselect("Como você se sente quando pensa nisso?", ["Amor", "Esperança", "Paz", "Força", "Dever", "Alegria"])
    if st.button("Salvar e Continuar"):
        if q1:
            st.session_state.answers['dia1_q1'] = q1
            st.session_state.answers['dia1_q2'] = q2
            next_step()
            st.rerun()

elif st.session_state.step == 2:
    st.header("Dia 2: Além do Óbvio")
    st.write(f"Ontem você mencionou: *'{st.session_state.answers.get('dia1_q1')}'*")
    q3 = st.text_area("Além disso, o que mais você gostaria de vivenciar ou realizar?", help="Pense em algo só seu.")
    q4 = st.text_area("O que você gostaria que as pessoas lembrassem sobre você no futuro?")
    if st.button("Avançar na Jornada"):
        st.session_state.answers['dia2_q1'] = q3
        st.session_state.answers['dia2_q2'] = q4
        next_step()
        st.rerun()

elif st.session_state.step == 3:
    st.header("Dia 3: Seus Valores")
    v = st.multiselect("Escolha seus 3 valores principais:", ["Família", "Liberdade", "Justiça", "Saúde", "Espiritualidade", "Aprendizado", "Coragem"])
    q5 = st.text_area("Como esses valores aparecem na sua vida hoje?")
    if st.button("Confirmar Valores"):
        st.session_state.answers['dia3_v'] = v
        st.session_state.answers['dia3_q'] = q5
        next_step()
        st.rerun()

elif st.session_state.step == 4:
    st.header("Dia 4: Transformando a Dor")
    st.write("Frankl dizia que o sofrimento deixa de ser sofrimento no momento em que encontra um sentido.")
    q6 = st.text_area("Qual aprendizado você tirou dos seus dias mais difíceis?")
    q7 = st.text_area("Como esse aprendizado poderia ajudar outra pessoa?")
    if st.button("Transformar e Seguir"):
        st.session_state.answers['dia4_q1'] = q6
        st.session_state.answers['dia4_q2'] = q7
        next_step()
        st.rerun()

elif st.session_state.step == 5:
    st.header("Dia 5: Seu Propósito")
    st.write("Chegamos ao momento de síntese.")
    prop = st.text_input("Defina seu propósito em uma frase curta:", placeholder="Ex: Ser um farol de amor para minha família e aprender algo novo todo dia.")
    passo = st.text_input("Qual o primeiro pequeno passo para viver isso amanhã?")
    if st.button("Finalizar Minha Jornada"):
        st.session_state.answers['proposito'] = prop
        st.session_state.answers['passo'] = passo
        next_step()
        st.rerun()

elif st.session_state.step > 5:
    st.balloons()
    st.header("🎉 Jornada Concluída!")
    st.success(f"Parabéns, André! Você completou o desafio com {st.session_state.points} pontos.")
    
    st.subheader("Resumo do seu Propósito:")
    st.info(f"✨ {st.session_state.answers.get('proposito')}")
    
    # Exibir Relatório Simples
    with st.expander("Ver meu relatório completo"):
        for k, v in st.session_state.answers.items():
            st.write(f"**{k}:** {v}")
    
    if st.button("Reiniciar"):
        st.session_state.step = 1
        st.rerun()
