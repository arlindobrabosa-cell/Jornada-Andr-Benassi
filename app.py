import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Encontrando Meu Propósito", page_icon="🌱")

# Inicialização do Estado
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'points' not in st.session_state:
    st.session_state.points = 0

# Título e Progresso
st.title("🌱 Encontrando Meu Propósito")
st.write(f"Olá, André! Esta é sua jornada de autodescoberta.")

progresso = (st.session_state.step - 1) / 5
st.progress(progresso)
st.sidebar.metric("Sua Pontuação", f"{st.session_state.points} pts")

# --- LÓGICA DOS DIAS ---

if st.session_state.step == 1:
    st.header("Dia 1: O Que Te Move")
    q1 = st.text_area("O que te faz sair da cama de manhã?", help="Pense em pessoas, tarefas ou sentimentos.")
    if st.button("Salvar Dia 1"):
        if q1:
            st.session_state.answers['dia1'] = q1
            st.session_state.points += 20
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.header("Dia 2: Além do Óbvio")
    st.write(f"Você mencionou que o que te move é: *{st.session_state.answers.get('dia1')}*")
    q2 = st.text_area("Além disso, que marca ou lembrança você gostaria de deixar no mundo?")
    if st.button("Salvar Dia 2"):
        st.session_state.answers['dia2'] = q2
        st.session_state.points += 20
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("Dia 3: Seus Valores")
    valores = st.multiselect("Quais são seus valores mais importantes?", ["Família", "Amor", "Liberdade", "Saúde", "Justiça", "Coragem"])
    q3 = st.text_area("Como esses valores se conectam com o seu filho ou com sua vida?")
    if st.button("Salvar Dia 3"):
        st.session_state.answers['dia3_valores'] = valores
        st.session_state.answers['dia3_texto'] = q3
        st.session_state.points += 20
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.header("Dia 4: Transformando a Dor")
    st.info("Na Logoterapia, aprendemos que nossa dor pode gerar um propósito.")
    q4 = st.text_area("O que você aprendeu com os desafios que enfrentou até hoje?")
    if st.button("Salvar Dia 4"):
        st.session_state.answers['dia4'] = q4
        st.session_state.points += 20
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.header("Dia 5: Sua Missão")
    q5 = st.text_input("Em uma frase, qual o seu propósito hoje?")
    passo = st.text_input("Qual o primeiro passo (mesmo que pequeno) você dará amanhã?")
    if st.button("Finalizar Jornada"):
        st.session_state.answers['proposito'] = q5
        st.session_state.answers['passo'] = passo
        st.session_state.points += 20
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    st.balloons()
    st.header("🎉 Jornada Completa!")
    st.success(f"Parabéns, André! Você atingiu {st.session_state.points} pontos.")
    
    st.subheader("Seu Relatório de Propósito:")
    st.write(f"**Seu Propósito:** {st.session_state.answers.get('proposito')}")
    st.write(f"**Seu próximo passo:** {st.session_state.answers.get('passo')}")
    
    with st.expander("Ver detalhes da sua evolução"):
        st.write(f"**O que te move:** {st.session_state.answers.get('dia1')}")
        st.write(f"**Valores:** {st.session_state.answers.get('dia3_valores')}")
        st.write(f"**Aprendizado da dor:** {st.session_state.answers.get('dia4')}")

    if st.button("Reiniciar Jornada"):
        st.session_state.step = 1
        st.session_state.points = 0
        st.rerun()
