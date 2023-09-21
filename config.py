import os
from os.path import join, dirname
from dotenv import load_dotenv

# Initialize env variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_token = os.environ.get('DISCORD_TOKEN')
gpt = os.environ.get('GPT_API_KEY')