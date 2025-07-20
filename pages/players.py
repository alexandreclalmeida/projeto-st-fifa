import streamlit as st

df = st.session_state["data"]

clubes = df["Club"].unique()
clube = st.sidebar.selectbox("Clube", clubes)

df_players = df[df["Club"] == clube]
jogadores = df_players["Name"].unique()
jogador = st.sidebar.selectbox("Jogador", jogadores)

jogador_stats = df[df["Name"] == jogador].iloc[0]

st.image(jogador_stats["Photo"])
st.title(jogador_stats["Name"])

st.markdown(f"**Clube:** {jogador_stats['Club']}")
st.markdown(f"**Posição:** {jogador_stats['Position']}")

col1, col2, col3 = st.columns(3)
col1.markdown(f"**Idade:** {jogador_stats['Age']}")
col2.markdown(f"**Altura:** {jogador_stats['Height(cm.)'] / 100:.2f}")
col3.markdown(f"**Peso:** {jogador_stats['Weight(lbs.)'] * 0.453:.2f}")

st.divider()

st.subheader(f"Overall {jogador_stats['Overall']}")
st.progress(int(jogador_stats["Overall"]))

# Podemos usar a definição de colunas com 'with'
col1, col2, col3 = st.columns(3)
with col1:
    # Para formatar o milhar no texto, usei :,
    st.metric(label="Valor de mercado", value=f"£ {jogador_stats['Value(£)']:,}")
with col2:
    st.metric(label="Remnueração semanal", value=f"£ {jogador_stats['Wage(£)']:,}")
with col3:
    st.metric(
        label="Cláusula de rescisão", value=f"£ {jogador_stats['Release Clause(£)']:,}"
    )
