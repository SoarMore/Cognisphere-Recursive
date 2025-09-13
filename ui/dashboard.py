import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.meta_agent import MetaAgent
import streamlit as st

st.title("Cognisphere Agent Dashboard")

# Input field
task = st.text_input("Enter a high-level task:")

# Button to trigger agent execution
if st.button("Run Cognisphere") and task:
    agent = MetaAgent(task)
    result = agent.execute()

    # Agent Invocation Log
    st.subheader("🔧 Agent Invocation Log")
    st.markdown("🧠 **MetaAgent** → Task received")
    st.markdown("🔧 **PlannerAgent** → Subtasks generated")

    for subtask in result["context"]:
        st.markdown(f"🔍 **ResearchAgent** → Collected data for: `{subtask}`")
        st.markdown(f"📝 **SummarizerAgent** → Summary created for: `{subtask}`")
        st.markdown(f"📌 **TaskManagerAgent** → Execution assigned for: `{subtask}`")

    st.markdown("📊 **EvaluatorAgent** → Output scored")
    st.metric("Quality Score", result["score"]["quality"])
    st.write(f"💬 Feedback: {result['score']['feedback']}")

    # Final JSON Output
    st.subheader("🧠 Final Output")
    st.json(result)
