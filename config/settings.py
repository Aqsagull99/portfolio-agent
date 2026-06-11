from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="liquid/lfm-2.5-1.2b-instruct:free",
    openai_client=external_client,
)

config = RunConfig(model=model, model_provider=external_client)
