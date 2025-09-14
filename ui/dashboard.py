import streamlit as st
from agents.task_manager_agent import TaskManagerAgent
from agents.research_manager import ResearchManager  # You’ll define this

st.set_page_config(page_title="Cognisphere Dashboard", layout="wide")
st.title("🧠 Cognisphere: Recursive Multi-Agent Intelligence")

tab1, tab2 = st.tabs(["📚 Autonomous Research", "⚙️ Task Manager"])

# ------------------ Tab 1: Research System ------------------ #
with tab1:
    st.subheader("Autonomous Knowledge Collection & Summarization")
    query = st.text_area(
        "Enter a research query:",
        placeholder="e.g. How to build a local LLM-powered summarizer using Mistral 7B",
        height=150
    )

    if st.button("Run Research"):
        manager = ResearchManager()
        with st.spinner("Collecting and summarizing knowledge..."):
            outputs = manager.handle_query(query)
        st.success("✅ Research Complete")

        for label, key in [
            ("📚 Raw Research", "background"),
            ("📝 Summary", "summary"),
            ("🔍 Critique", "critique"),
            ("🧭 Reflection", "reflection"),
            ("🎯 Final Output", "final")
        ]:
            with st.expander(label, expanded=True):
                st.code(outputs.get(key, "No output."), language="markdown")

# ------------------ Tab 2: Task Manager ------------------ #
with tab2:
    st.subheader("Self-Governing Task Planning & Execution")
    task = st.text_area(
        "Enter a high-level task:",
        placeholder="e.g. Build a local app that summarizes PDFs using Mistral 7B",
        height=150
    )

    if st.button("Run Task Manager"):
        manager = TaskManagerAgent()
        with st.spinner("Planning and optimizing tasks..."):
            outputs = manager.handle_task(task)
        st.success("✅ Task Completed")

        for label, key in [
            ("🧠 Subtasks", "subtasks"),
            ("📝 Summary", "summary"),
            ("🔍 Critique", "critique"),
            ("🧭 Reflection", "reflection"),
            ("🎯 Final Output", "final")
        ]:
            with st.expander(label, expanded=True):
                st.code(outputs.get(key, "No output."), language="markdown")
