import gradio as gr
import ai_gradio

# Create and launch a Swarms Chat interface
gr.load(
    name='huggingface:mistralai/Mistral-7B-Instruct-v0.3',  # Model identifier (supports OpenAI and others)
    src=ai_gradio.registry,      # Source module for model configurations
    # agent_name="Stock-Analysis-Agent",  # Example agent from Finance category
    agent_name="HealthScoreGatekeeper",
    title='Swarms Chat',
    description='Chat with an AI agent powered by Swarms',
    saved_state_path="orthodox-agent-state.json"
).launch()
