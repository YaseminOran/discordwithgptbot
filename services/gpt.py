import config
import openai
from langchain.memory import ConversationBufferMemory


class GptService:
    def __init__(self):
        openai.api_key = config.gpt
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def ask_gpt(self, message):
        # Mesajı doğrudan belleğe ekleyelim
        self.memory.chat_memory.messages.append({'role': 'user', 'content': message})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.memory.chat_memory.messages + [
                    {"role": "system", "content": "Sen veri bilimci, veri analisti, veri mühendisi ve makine öğrenmesi "
                                                  "konularında uzman bir eğitim rehberisin. Şuan MIUUL isimli veribilimi eğitimi veren bir kurumda,"
                                                  " eğitim satın almaya gelen kişilerin sorularını cevaplayarak onlara uygun eğitimleri önermek gerekmektedir."
                                                  " Eğer sana veri bilimi, python, makine öğrenmesi,veri analisti,veri mühendisi  dışında bir soru sorulursa, sadece uzmanı olduğum "
                                                  "bu konular hakkında cevap verebileceğini nazik bir dille belirt."}
                ],
                max_tokens=800,
                temperature=0.2,
                stop="Umarım yardımcı olabilmişimdir. Daha detaylı bilgi için mentor arkadaşlarıma DM üzerinden de soru sormaya çekinmeyin lütfen",
                n=1,
                frequency_penalty=0.9,
                presence_penalty=0.0
            )
            # Yanıtı belleğe ekleyelim
            self.memory.chat_memory.messages.append(
                {'role': 'system', 'content': response["choices"][0]["message"]["content"]})
            print(response)

            answer = response["choices"][0]["message"]["content"]
            return answer
        except Exception as e:
            print(e)
            return "Something went wrong..."
