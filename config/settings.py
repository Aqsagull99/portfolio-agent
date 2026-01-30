# from dotenv import load_dotenv
# import os
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel
# from agents.run import RunConfig

# load_dotenv()

# gemini_api_key = os.getenv("GEMIMI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is missing")

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client,
# )

# config = RunConfig(model=model, model_provider=external_client)



#with open router key 
from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing")

# OpenRouter client
external_client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

# LiquidAI free model
model = OpenAIChatCompletionsModel(
    model="liquid/lfm-2.5-1.2b-instruct:free",
    openai_client=external_client,
)

# Run config
config = RunConfig(model=model, model_provider=external_client)  # <-- this is important




