import asyncio

class DiscordService:
    def __init__(self, client, assistant):
        self.client = client
        self.assistant = assistant

    async def handle_ready(self):
        print(f'{self.client.user.name} has connected to Discord!')

   
    from anahtar_kelimeler import A

    async def handle_message(self, message):
        channel = message.channel

        if message.author == self.client.user:
            return
        
        content = message.content.lower()
        
        if "fiyat" in content or "ücret" in content or "miuul" in content:
            await channel.send("Miuul Eğitimleri ile ilgili mentorlerimize direct mesaj yoluyla danışabilirsiniz :)")
            await asyncio.sleep(2)
            await channel.send("\n Detaylı bilgi için Miuul Bootcamp kataloğunu inceleyebilirsiniz : [Miuul Katalog](https://miuul.com/katalog?tur=bootcamp)")

        #elif "anlamadım" in content or "anlayamadım" in content:
           # await channel.send("Anlayamadığınız bölümü detaylı belirtirseniz size daha iyi yardımcı olabilirim :) ")
            
       
        elif "path" in content and "bootcamp" in content:
            await channel.send("Bootcamp programında program öncesi ön hazırlık eğitimi, canlı mentor desteği, Vahit Keskin ile birlikte haftalık recap, takım çalışması ve IK ve teknik mülakatlar gibi içerikler mevcuttur. Path programında ise eğitimleri kendi öğrenme hızınıza göre takip ediyor olacaksınız. Tüm içeriklere 1 yıl erişim hakkınız bulunmaktadır. Sorularınız olması durumunda da mentorlarımız ile 7/24 iletişim kurarak süreci ilerletiyor olacaksınız. :)")
            await asyncio.sleep(2)
            await channel.send("[MIUUL](https://www.miuul.com/)'a tıklayarak tüm detaylara ulaşabilirsiniz. Daha detaylı bilgiler için mentorlerimizden de destek alabilirsiniz :)")
        
        elif "bootcamp" in content:
            await channel.send("Bootcamp programında program öncesi ön hazırlık eğitimi, canlı mentor desteği, Vahit Keskin ile birlikte haftalık recap, takım çalışması ve IK ve teknik mülakatlar gibi içerikler mevcuttur.")
            await asyncio.sleep(2)
            await channel.send("\n  Miuul Bootcamp kataloğunu inceleyebilirsiniz  : [Miuul Bootcamp Kataloğu](https://miuul.com/katalog?tur=bootcamp)")


        elif "path" in content:
            await channel.send("Path programında eğitimler tekildir ve kendi öğrenme hızınıza göre takip ediyor olacaksınız. Tüm içeriklere 1 yıl erişim hakkınız bulunmaktadır. Sorularınız olması durumunda da mentorlarımız ile 7/24 iletişim kurarak süreci ilerletiyor olacaksınız.")
            await asyncio.sleep(2)
            await channel.send("\n Bu linkten Miuul Path kataloğunu inceleyebilirsiniz: [Miuul Path Kataloğu](https://www.miuul.com/katalog?tur=kariyer&gclid=CjwKCAjw9-6oBhBaEiwAHv1QvKewPIfjJ78iUKuZGDVMbO5MZDFINlIG62Yssx8rcEmw0jiqH1Tv1RoC24QQAvD_BwE)")

        
        elif "teşekkür" in content:
            await channel.send("Ne demek, rica ederim. İyi çalışmalar! :)")

        
        elif "selam" in content or "naber" in content or "merhaba" in content:
            await channel.send("Merhaba! Ben Miuul yapay zeka botuyum. Size nasıl yardımcı olabilirim :) ")

        elif any(kelime.lower() in message.content.lower() for kelime in self.A):
            await channel.send(f'Cevabınızı düşünüyorum!')
            gpt_answer = self.assistant.process_message(message)
            await channel.send(gpt_answer)
        
        
        else: 
            await channel.send("Ben miuul path yapay zeka botuyum. Bu konularda sorunuz varsa size yardımcı olmayı çok isterim. Başka konularda yardımcı olabilecek yetkilendirmem bulunmamakta :)")


        