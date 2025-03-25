import openai
import time
# API 키 설정
openai.api_key = "sk-B_IVyeg-cbrrYLjVyMJActzLtIbT0eKtIWKsYKDBbFT3BlbkFJOcPcz9yE7-URszaQ2_GKoFQ5g9pWpl3jQU3CnuL7cA"

def analyze_emotions(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant for analyzing emotions."},
                {"role": "user", "content": f"Analyze the emotions in this text: '{text}'. Rate happiness, sadness, fear, anger, surprise, and disgust from 0 to 10."}
            ],
            temperature=0.7  # 응답의 창의성 조절
        )
        return response.choices[0].message.content.strip()
    except openai.error.AuthenticationError:
        return "API 키 인증 오류가 발생했습니다. API 키를 확인해주세요."
    except openai.error.RateLimitError:
        return "API 사용량 제한에 도달했습니다. 잠시 후 다시 시도해주세요."
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

text = "나는 오늘 시험을 잘봐서 아주 뿌듯하고 행복한 하루였어"
analysis = analyze_emotions(text)
if analysis:
    print(analysis)