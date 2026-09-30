import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
 
# .envファイルの読み込み
load_dotenv()
 
# API-KEYを環境変数に設定
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")
prompt = template.format(keyword="生成AI")

chat = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
result = chat.invoke(prompt)
print(result.text)