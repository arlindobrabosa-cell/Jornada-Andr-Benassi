import streamlit as st

# Forçar a limpeza de qualquer lixo de memória anterior
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

def mudar_passo(proximo):
    st.session_state.step = proximo

st.title("🌱 Jornada: Encontrando Meu Propósito")
st.write("---")

# DIA 1
if st.session_state.step == 1:
    st.header("Dia 1: O Que Te Move")
    resp1 = st.text_area("O que ou quem é o seu grande motivo para viver hoje?", key="d1")
    if st.button("Salvar e Continuar"):
        if resp1:
            st.session_state.respostas['motivo'] = resp1
            mudar_passo(2)
            st.rerun()

# DIA 2 - DINÂMICO
elif st.session_state.step == 2:
    motivo = st.session_state.respostas.get('motivo', 'o que você citou')
    st.header("Dia 2: Além do Óbvio")
    st.write(f"Você nos contou que **'{motivo}'** é o que te move hoje.")
    
    # Pergunta adaptável:
    q2_texto = f"Além de '{motivo}', o que mais traz sentido ou alegria para o seu dia a dia?"
    resp2 = st.text_area(q2_texto, key="d2")
    
    if st.button("Avançar para o Dia 3"):
        st.session_state.respostas['alem_do_obvio'] = resp2
        mudar_passo(3)
        st.rerun()

# DIA 3
elif st.session_state.step == 3:
    st.header("Dia 3: Valores Profundos")
    valores = st.multiselect("Quais valores são fundamentais para você?", ["Família", "Amor", "Paz", "Liberdade", "Saúde", "Trabalho"])
    resp3 = st.text_area("Como esses valores aparecem na sua vida?", key="d3")
    if st.button("Avançar para o Dia 4"):
        st.session_state.respostas['valores'] = ", ".join(valores)
        st.session_state.respostas['obs_valores'] = resp3
        mudar_passo(4)
        st.rerun()

# DIA 4
elif st.session_state.step == 4:
    st.header("Dia 4: Sua Força")
    st.write("Toda dificuldade nos ensina algo sobre nossa própria força.")
    resp4 = st.text_area("O que você aprendeu sobre si mesmo nos momentos difíceis?", key="d4")
    if st.button("Avançar para o Dia 5"):
        st.session_state.respostas['forca'] = resp4
        mudar_passo(5)
        st.rerun()

# DIA 5
elif st.session_state.step == 5:
    st.header("Dia 5: Seu Propósito")
    resp5 = st.text_input("Em uma frase, qual é o seu propósito hoje?", key="d5")
    passo = st.text_input("Qual o primeiro pequeno passo que você dará amanhã?", key="p1")
    if st.button("Finalizar Jornada"):
        st.session_state.respostas['proposito'] = resp5
        st.session_state.respostas['primeiro_passo'] = passo
        mudar_passo(6)
        st.rerun()

# RELATÓRIO FINAL
elif st.session_state.step == 6:
    st.balloons()
    st.header("🎯 Jornada Concluída!")
    
    texto_relatorio = f"""
    📝 RELATÓRIO DE PROPÓSITO - ANDRÉ
    
    1. Motivo atual: {st.session_state.respostas.get('motivo')}
    2. Outras fontes de sentido: {st.session_state.respostas.get('alem_do_obvio')}
    3. Valores: {st.session_state.respostas.get('valores')}
    4. Força interna: {st.session_state.respostas.get('forca')}
    5. PROPÓSITO: {st.session_state.respostas.get('proposito')}
    6. PRIMEIRO PASSO: {st.session_state.respostas.get('primeiro_passo')}
    """
    
    st.subheader("Seu resumo está pronto:")
    st.code(texto_relatorio, language="text")
    st.info("Copie o texto acima e envie para seu terapeuta no WhatsApp.")
    
    if st.button("Reiniciar Teste"):
        st.session_state.step = 1
        st.session_state.respostas = {}
        st.rerun()
