
class DiscordService:
    def __init__(self, client, assistant):
        self.client = client
        self.assistant = assistant


    async def handle_ready(self):
        print(f'{self.client.user.name} has connected to Discord!')

    async def handle_message(self, message):
        channel = message.channel

        if message.author == self.client.user:
            return

        await channel.send(f'Cevabinizi dusunuyorum!')
        gpt_answer = self.assistant.process_message(message)  # Bu satırı değiştirdim.
        await channel.send(gpt_answer)

