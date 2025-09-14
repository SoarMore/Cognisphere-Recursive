import streamlit as st
from agents.research_manager import ResearchManager

st.set_page_config(page_title="Cognisphere", layout="wide")

st.title("🧠 Cognisphere: Autonomous Knowledge Engine")

tabs = st.tabs(["Agentic Flow", "Agent Logs"])

with tabs[0]:
    query = st.text_input("Enter a research query:", "")
    if st.button("Run Cognisphere"):
        manager = ResearchManager()
        outputs = manager.handle_query(query)

        for label in ["📚 Raw Research", "📝 Summary", "🔍 Critique", "🧭 Reflection"]:
            st.subheader(label)
            st.markdown(outputs.get(label, "⚠️ No output"))

with tabs[1]:
    st.header("🛠️ Debug Logs")
    if query:
        for label, content in outputs.items():
            st.subheader(label)
            st.code(content if content else "⚠️ No output", language="markdown")
