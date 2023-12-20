import config
import openai
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain





class GptService:
    def __init__(self):
        openai.api_key = config.gpt
        #self.chat_history = []
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        
    

    def ask_gpt(self,message):
        self.memory.add({'content': message})
        try:
            
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.memory.messages + [
                    {"role": "system", "content": "Sen veri bilimci, veri analisti, veri mühendisi ve makine öğrenmesi \
                         konularında uzman bir eğitimcisin. Şuan MIUUL isimli veribilimi eğitimi veren bir kurumda,\
                             öğrencilerin sorularını ve karşılaştıkları  sorunlara çözüm bulan bir mentorsün.\
                                Eğer sana veri bilimi, python, makine öğrenmesi ve docker dışında bir soru sorulursa, sadece uzmanı olduğum \
                                    bu konular hakkında cevap verebileceğini nazik bir dille belirt."},
                    {"role": "user", "content": message}
                ],
                max_tokens=800,  ## yanıtın max token sayısı
                temperature=0.2,   #rastlege yanıt leveli
                stop="Umarım yardımcı olabilmişimdir. Daha detaylı bilgi için mentor arkadaşlarıma DM üzerinden de soru sormaya çekinmeyin lütfen" ,   # yanıtın durmasını istediğimiz cümle
                n=1,  # 1 den fazla yanıt için
                frequency_penalty=0.9,  # kelime tekrarından kaçınması için artırdım çok yüksek değer anlamı bozar 
                                        # cevap saçma olabilir.
                presence_penalty=0.0  ## önceki mesajların yanıtları, vereceği yanıtı etkilemesin
            )
            self.memory.add({'role': 'system', 'content': response})
            print(response)
            
            answer = response["choices"][0]["message"]["content"]
            return answer
        except Exception as e:
            print(e)
            return "Something went wrong..."

        
