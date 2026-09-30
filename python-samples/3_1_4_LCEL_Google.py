import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
 
# .envファイルの読み込み
load_dotenv()
 
# API-KEYを環境変数に設定
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

prompt_template = "{adjective}ジョークを教えてください"
prompt = PromptTemplate(
    input_variables=["adjective"], template=prompt_template
)
chat = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

chain = prompt | chat
result = chain.invoke({"adjective": "美しい"})
print(result.text)