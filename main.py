
from discord.ext import commands
import openai
import config
from services.gpt import GptService
from services.discordservices import DiscordService
import discord


class AiAssistant:
    def __init__(self):
        self.gpt_service = GptService()

    def process_message(self, message):
        content = message.content
        gpt_answer = self.gpt_service.ask_gpt(content)
        return gpt_answer


class MiuulBot:
    def __init__(self, api_token, gpt_token, bot_prefix='!'):
        #config values
        self.API_TOKEN = api_token
        self.BOT_PREFIX = bot_prefix
        self.GPT_TOKEN = gpt_token

        #Setting up intents
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.intents.reactions = True

        self.client = discord.Client(intents=self.intents)
        self.bot = commands.Bot(command_prefix=self.BOT_PREFIX, intents=self.intents)
        self.assistant = AiAssistant()
        self.discord_service = DiscordService(self.client, self.assistant)

        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        await self.discord_service.handle_ready()

    async def on_message(self, message):
        await self.discord_service.handle_message(message)

    def run(self):
        self.client.run(self.API_TOKEN)

if __name__ == "__main__":
    bot = MiuulBot(api_token=config.api_token, gpt_token=config.gpt)
    bot.run()








