from logging import getLogger

from openai import AsyncAzureOpenAI

from workshop_azure_iot.settings.ai_services import Settings

logger = getLogger(__name__)


class Client:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.azure_openai = AsyncAzureOpenAI(
            api_key=self.settings.ai_services_api_key,
            api_version=self.settings.ai_services_api_version,
            azure_endpoint=self.settings.ai_services_endpoint,
        )

    async def chat_completions(self, messages: list) -> dict:
        response = await self.azure_openai.chat.completions.create(
            model=self.settings.ai_services_model_gpt,
            messages=messages,
        )
        return response.model_dump()
