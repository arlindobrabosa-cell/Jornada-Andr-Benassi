import streamlit as st

# Versão 2.0 - Atualizada para limpeza de cache e relatório
st.set_page_config(page_title="Jornada do André", page_icon="🌱")

# Função para resetar tudo corretamente
def reset_jornada():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Inicialização do Estado
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

st.title("🌱 Jornada: Encontrando Meu Propósito")
st.write("---")

# LÓGICA DOS DIAS
if st.session_state.step == 1:
    st.header("Dia 1: O Que Te Move")
    q1 = st.text_area("O que te faz sair da cama de manhã?", key="input_d1")
    if st.button("Salvar e Ir para o Dia 2"):
        if q1:
            st.session_state.answers['Dia 1 (O que move)'] = q1
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.header("Dia 2: Além do Óbvio")
    st.write(f"Você disse que o que te move é: *{st.session_state.answers.get('Dia 1 (O que move)')}*")
    q2 = st.text_area("Se você pudesse realizar um sonho só seu, qual seria?", key="input_d2")
    if st.button("Salvar e Ir para o Dia 3"):
        st.session_state.answers['Dia 2 (Sonho Próprio)'] = q2
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("Dia 3: Seus Valores")
    valores = st.multiselect("Escolha seus valores:", ["Família", "Liberdade", "Paz", "Saúde", "Trabalho"])
    q3 = st.text_area("Por que esses valores são importantes?", key="input_d3")
    if st.button("Salvar e Ir para o Dia 4"):
        st.session_state.answers['Dia 3 (Valores)'] = ", ".join(valores)
        st.session_state.answers['Dia 3 (Explicação)'] = q3
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.header("Dia 4: Transformação")
    q4 = st.text_area("Qual a maior lição que você aprendeu com suas dificuldades?", key="input_d4")
    if st.button("Salvar e Ir para o Dia 5"):
        st.session_state.answers['Dia 4 (Lição)'] = q4
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.header("Dia 5: Seu Propósito")
    q5 = st.text_input("Defina seu propósito hoje em uma frase:", key="input_d5")
    if st.button("Finalizar e Gerar Relatório"):
        st.session_state.answers['Propósito Final'] = q5
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    st.balloons()
    st.header("🎯 Jornada Concluída!")
    
    # Montando o texto para o André copiar e te enviar
    relatorio_texto = "MEU RELATÓRIO DE PROPÓSITO\n\n"
    for key, value in st.session_state.answers.items():
        relatorio_texto += f"{key}: {value}\n\n"
    
    st.subheader("Aqui está o seu resumo:")
    st.code(relatorio_texto, language="text")
    
    st.info("André, copie o texto acima e envie para seu terapeuta no WhatsApp.")
    
    if st.button("Reiniciar do Zero (Limpar Tudo)"):
        reset_jornada()
