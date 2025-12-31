import streamlit as st

# Configuração Básica
st.set_page_config(page_title="Encontrando Meu Propósito", page_icon="🌱")

# Estado do App
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Título
st.title("🌱 Encontrando Meu Propósito")
st.write(f"Olá, André! Vamos caminhar juntos nesta jornada.")

# Lógica de Navegação
if st.session_state.step == 1:
    st.header("Dia 1: O Que Te Move")
    q1 = st.text_area("O que te faz sair da cama de manhã?")
    if st.button("Salvar e Continuar"):
        if q1:
            st.session_state.answers['dia1'] = q1
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.header("Dia 2: Além do Óbvio")
    st.write(f"Ontem você disse: {st.session_state.answers.get('dia1')}")
    q2 = st.text_area("Além do seu filho, o que mais traz cor à sua vida?")
    if st.button("Avançar"):
        st.session_state.answers['dia2'] = q2
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("Dia 3: Conclusão")
    st.success("Você está indo muito bem, André!")
    st.write("Em breve teremos mais passos nesta jornada.")
    if st.button("Reiniciar"):
        st.session_state.step = 1
        st.rerun()
