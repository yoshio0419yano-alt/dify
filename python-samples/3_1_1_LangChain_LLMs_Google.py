import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
 
# .envファイルの読み込み
load_dotenv()
 
# API-KEYの設定
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

llm = GoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=GOOGLE_API_KEY)
result = llm.invoke("こんにちは。あなたは誰？")
print(result)