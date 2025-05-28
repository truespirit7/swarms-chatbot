
from swarm_models.huggingface import HuggingfaceLLM

# Get the OpenAI API key from the environment variable
# api_key = os.getenv("HF_TOKEN")
# Initialize the HuggingfaceLLM instance with a model ID
# model_id = "mistralai/Mistral-7B-Instruct-v0.3"
# model_id = "mistralai/Mistral-7B-Instruct-v0.3"
model_id = "NousResearch/Nous-Hermes-2-Vision-Alpha"

hugging_face_model = HuggingfaceLLM(model_id=model_id)


prompt = "Once upon a time"
generated_text = hugging_face_model.run(prompt)
print(generated_text)