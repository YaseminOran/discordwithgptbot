import config
import openai

class GptService:
    def __init__(self):
        openai.api_key = config.gpt

    def ask_gpt(self,message):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": "sen miuul şirkletinde data scientist, data engineer, data analyst bootcamplerinde soru cevaplayan bir mentörsün.Python dili kullanılmakta.Cevaplar yeterli gelmediyse  mentör desteğinin yardımcı olabileceğini belirt"},
                    {"role": "user", "content": message}
                ],
                max_tokens=1000,
                temperature=0,

            )
            print(response)
            answer = response["choices"][0]["message"]["content"]
            return answer
        except Exception as e:
            print(e)
            return "Something went wrong..."