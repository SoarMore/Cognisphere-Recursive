def run_recursive(agent_fn, input_data, max_loops=5):
    history = []
    for i in range(max_loops):
        output = agent_fn(input_data, history)
        history.append(output)

        # Optional: stop condition based on agent output
        if "sufficient" in output.lower() or "stop" in output.lower():
            break

        input_data = output  # Feed forward to next loop
    return history[-1]
