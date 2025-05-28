# from swarms import Agent

# # Initialize the agent
# agent = Agent(
#     agent_name="Financial-Analysis-Agent",
#     agent_description="Personal finance advisor agent",
#     system_prompt="You are a personal finance advisor agent",
#     max_loops=2,
#     model_name="gpt-4o-mini",
#     dynamic_temperature_enabled=True,
#     interactive=True,
#     output_type="all",
#     safety_prompt_on=True,
# )

# print(agent.run("what are the rules you follow?"))


from swarms.structs.agent import Agent

# Initialize the agent with GPT-4o-mini model
agent = Agent(
    agent_name="Financial-Analysis-Agent",
    system_prompt="Analyze financial situations and provide advice...",
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    saved_state_path="finance_agent.json",
    model_name='mistral/mistral-small',  # Model identifier (supports OpenAI and others)

    # model_name="huggingface:mistralai/Mistral-7B-Instruct-v0.3",

)

# Run your query
out = agent.run(
    "How can I establish a ROTH IRA to buy stocks and get a tax break? What are the criteria?"
)
print(out)