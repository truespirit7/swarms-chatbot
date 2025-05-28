from swarms import Agent
import litellm
from litellm import completion
import gradio as gr
import ai_gradio

agent = Agent(
    agent_name="Custom-Agent",
    model_name="mistral/mistral-small",
    temperature=0.7,  # Controls randomness (0.0 to 1.0)
    max_tokens=2000,  # Maximum tokens in response
    top_p=0.9,       # Nucleus sampling parameter
    frequency_penalty=0.0,  # Reduces repetition
    presence_penalty=0.0,   # Encourages new topics
    # ... other parameters
)
litellm._turn_on_debug()
# agent.run("Hello, how are you?")
def chat_with_agent(message, history):
    response = agent.run(message)
    return response

# Создаем Gradio интерфейс
gr.ChatInterface(
    fn=chat_with_agent,
    title="Swarms Orthodox Assistant",
    description="Chat with an AI assistant powered by Swarms and Mistral-7B"
).launch()

# gr.load(
#     # name='mistral/mistral-small',  # Model identifier (supports OpenAI and others)
#     name='huggingface:mistralai/Mistral-7B-Instruct-v0.3',  # Model identifier (supports OpenAI and others)
#     src=ai_gradio.registry,      # Source module for model configurations
#     title='Swarms Chat',
#     description='Chat with an AI agent powered by Swarms',
#     saved_state_path="orthodox-agent-state.json"
# ).launch()
