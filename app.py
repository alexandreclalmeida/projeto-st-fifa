from datetime import datetime as dt

import pandas as pd
import streamlit as st

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= dt.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.set_page_config(layout="wide")

home_page = st.Page("pages/home.py", title="Home", icon="🏠")
players_page = st.Page("pages/players.py", title="Players", icon="🏃")
teams_page = st.Page("pages/teams.py", title="Teams", icon="⚽️")

pg = st.navigation([home_page, players_page, teams_page])
pg.run()
