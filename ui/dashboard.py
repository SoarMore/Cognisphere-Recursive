import streamlit as st
from agents.meta_agent import MetaAgent

st.title("Cognisphere Agent Dashboard")

task = st.text_input("Enter a high-level task:")
if st.button("Run Cognisphere"):
    agent = MetaAgent(task)
    result = agent.execute()
    st.json(result)
