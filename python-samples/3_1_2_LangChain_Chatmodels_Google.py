import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
 
# .envファイルの読み込み
load_dotenv()

# API-KEYを環境変数に設定
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
result = llm.invoke("こんにちは。あなたは誰？")
print(result.text)