import streamlit as st

df = st.session_state["data"]

clubes = df["Club"].unique()
clube = st.sidebar.selectbox("Clube", clubes)

df_teams = df[df["Club"] == clube].set_index("Name")

st.image(df_teams.iloc[0]["Club Logo"])
st.markdown(f"## {clube}")

columns = [
    "Age",
    "Photo",
    "Flag",
    "Overall",
    "Value(£)",
    "Wage(£)",
    "Joined",
    "Height(cm.)",
    "Weight(lbs.)",
    "Contract Valid Until",
    "Release Clause(£)",
]

st.dataframe(
    df_teams[columns],
    column_config={
        "Overall": st.column_config.ProgressColumn("Overall", format="%d"),
        "Wage(£)": st.column_config.ProgressColumn(
            "Weekly Wage",
            format="£%f",
            min_value=0,
            max_value=df_teams["Wage(£)"].max(),
        ),
        "Photo": st.column_config.ImageColumn(width="small"),
        "Flag": st.column_config.ImageColumn("Country", width="small"),
    },
)
