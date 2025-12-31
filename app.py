import streamlit as st

# Versão Imersão Terapêutica - Sem restrição de dias
st.set_page_config(page_title="Jornada de Propósito", page_icon="✨")

if 'step' not in st.session_state:
    st.session_state.step = 0 # Começa na Introdução
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

def avançar():
    st.session_state.step += 1

st.title("🌱 Jornada: Encontrando Meu Propósito")

# PASSO 0: INTRODUÇÃO
if st.session_state.step == 0:
    st.header("Bem-vindo, André")
    st.write("""
    Esta é uma jornada de imersão desenhada especialmente para você. 
    Não é um teste, mas um encontro com as suas próprias respostas.
    
    Reserve cerca de 20 minutos, sinta-se confortável e responda com o que vier ao seu coração.
    Suas respostas nos ajudarão a construir um mapa para o seu futuro.
    """)
    if st.button("Iniciar Minha Jornada"):
        avançar()
        st.rerun()

# PERGUNTA 1
elif st.session_state.step == 1:
    st.subheader("Pergunta 1 de 8")
    resp = st.text_area("O que ou quem é o seu principal motivo para viver hoje?")
    if st.button("Avançar"):
        if resp:
            st.session_state.respostas['Motivo Inicial'] = resp
            avançar()
            st.rerun()

# PERGUNTA 2 (DINÂMICA)
elif st.session_state.step == 2:
    motivo = st.session_state.respostas.get('Motivo Inicial')
    st.subheader("Pergunta 2 de 8")
    st.write(f"Você mencionou: **'{motivo}'**. Isso é muito forte.")
    resp = st.text_area(f"Além de '{motivo}', que outras coisas, por menores que sejam, trazem um brilho de cor ao seu dia?")
    if st.button("Avançar"):
        st.session_state.respostas['Outras Fontes'] = resp
        avançar()
        st.rerun()

# PERGUNTA 3 (LEGADO)
elif st.session_state.step == 3:
    st.subheader("Pergunta 3 de 8")
    resp = st.text_area("Se você pudesse deixar uma marca no mundo, uma qualidade pela qual ser lembrado, qual seria?")
    if st.button("Avançar"):
        st.session_state.respostas['Legado'] = resp
        avançar()
        st.rerun()

# PERGUNTA 4 (VALORES)
elif st.session_state.step == 4:
    st.subheader("Pergunta 4 de 8")
    valores = st.multiselect("Quais valores definem quem você quer ser?", ["Amor", "Justiça", "Coragem", "Paz", "Liberdade", "Resiliência"])
    if st.button("Avançar"):
        st.session_state.respostas['Valores'] = ", ".join(valores)
        avançar()
        st.rerun()

# PERGUNTA 5 (CONTRIBUIÇÃO)
elif st.session_state.step == 5:
    st.subheader("Pergunta 5 de 8")
    resp = st.text_area("Existe algo que você saiba fazer ou alguma experiência que você viveu que poderia ajudar alguém que está sofrendo hoje?")
    if st.button("Avançar"):
        st.session_state.respostas['Contribuição'] = resp
        avançar()
        st.rerun()

# PERGUNTA 6 (FORÇA NA DOR)
elif st.session_state.step == 6:
    st.subheader("Pergunta 6 de 8")
    st.info("Logoterapia: 'A dor pode ser transformada em conquista'.")
    resp = st.text_area("O que você aprendeu sobre sua própria força nos momentos de maior escuridão?")
    if st.button("Avançar"):
        st.session_state.respostas['Força'] = resp
        avançar()
        st.rerun()

# PERGUNTA 7 (SÍNTESE)
elif st.session_state.step == 7:
    st.subheader("Pergunta 7 de 8")
    resp = st.text_input("Diante de tudo o que refletimos, como você descreveria seu propósito em uma frase?")
    if st.button("Avançar para o Passo Final"):
        st.session_state.respostas['Propósito'] = resp
        avançar()
        st.rerun()

# PERGUNTA 8 (AÇÃO)
elif st.session_state.step == 8:
    st.subheader("Pergunta 8 de 8")
    resp = st.text_input("Qual o primeiro pequeno passo que você dará amanhã para honrar esse propósito?")
    if st.button("Finalizar Imersão"):
        st.session_state.respostas['Primeiro Passo'] = resp
        st.session_state.step = 9
        st.rerun()

# CONCLUSÃO
elif st.session_state.step == 9:
    st.balloons()
    st.header("🎯 Jornada Concluída!")
    
    relatorio = "📝 MEU MAPA DE PROPÓSITO\n\n"
    for k, v in st.session_state.respostas.items():
        relatorio += f"🔹 {k}: {v}\n"
    
    st.code(relatorio, language="text")
    st.success("André, essa jornada é o começo de uma nova etapa. Copie o texto acima e envie para mim.")
    
    if st.button("Reiniciar"):
        st.session_state.step = 0
        st.session_state.respostas = {}
        st.rerun()
