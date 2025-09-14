def format_prompt(role: str, task: str, input_text: str) -> str:
    return (
        f"You are a {role}.\n\n"
        f"Task: {task}\n\n"
        f"Input:\n{input_text}\n\n"
        f"Answer:"
    )
