import streamlit as st

# Versão 3.0 - Totalmente Dinâmica e Adaptável
st.set_page_config(page_title="Minha Jornada", page_icon="🌱")

def reset_jornada():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

st.title("🌱 Jornada de Descoberta")

# --- FLUXO DOS DIAS ---

if st.session_state.step == 1:
    st.header("Dia 1: O Que Te Move")
    st.write("Para começar, pense no que hoje faz você se levantar.")
    q1 = st.text_area("O que ou quem é o seu principal motivo para viver hoje?", key="input_d1")
    if st.button("Salvar e Avançar"):
        if q1:
            st.session_state.answers['Motivo Principal'] = q1
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("Por favor, escreva algo para continuarmos.")

elif st.session_state.step == 2:
    # PEGA A RESPOSTA DO DIA 1 PARA USAR AQUI
    motivo_anterior = st.session_state.answers.get('Motivo Principal', 'o que você mencionou')
    
    st.header("Dia 2: Expandindo o Olhar")
    # Texto dinâmico: Se ele escreveu "Sol", aqui aparecerá "Sol".
    st.write(f"Você nos contou que **'{motivo_anterior}'** é o que te move hoje.")
    st.write("Isso é valioso. Agora, tente olhar um pouco além...")
    
    q2 = st.text_area(f"Além de '{motivo_anterior}', o que mais você gostaria de cultivar ou realizar na sua vida?", key="input_d2")
    
    if st.button("Ir para o Dia 3"):
        st.session_state.answers['Outros Interesses'] = q2
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("Dia 3: Seus Valores")
    valores = st.multiselect("Quais valores são inegociáveis para você?", ["Família", "Liberdade", "Conhecimento", "Paz", "Resiliência", "Amor"])
    q3 = st.text_area("Como esses valores guiam suas decisões?", key="input_d3")
    if st.button("Ir para o Dia 4"):
        st.session_state.answers['Valores'] = ", ".join(valores)
        st.session_state.answers['Sobre Valores'] = q3
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.header("Dia 4: Transformação")
    st.write("A Logoterapia nos ensina que toda dificuldade traz um aprendizado.")
    q4 = st.text_area("Olhando para sua história, qual força você descobriu que tem?", key="input_d4")
    if st.button("Ir para o Dia 5"):
        st.session_state.answers['Força Descoberta'] = q4
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.header("Dia 5: Definindo o Propósito")
    st.write("Chegamos ao final desta etapa.")
    q5 = st.text_input("Se você pudesse resumir seu propósito em uma frase, qual seria?", key="input_d5")
    if st.button("Finalizar e Ver Resumo"):
        st.session_state.answers['Propósito Definido'] = q5
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    st.balloons()
    st.header("🎯 Jornada Concluída!")
    
    # Relatório formatado para o terapeuta
    relatorio = "📝 MEU RELATÓRIO DE DESCOBERTA\n\n"
    for k, v in st.session_state.answers.items():
        relatorio += f"🔹 {k}: {v}\n"
    
    st.code(relatorio, language="text")
    st.info("André, copie o texto acima e envie para mim no WhatsApp para conversarmos na próxima sessão.")
    
    if st.button("Reiniciar (Limpar tudo para um novo teste)"):
        reset_jornada()
