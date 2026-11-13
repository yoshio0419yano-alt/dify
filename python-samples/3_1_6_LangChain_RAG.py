# RAG完全版
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# PDF読み込み
documents = PyPDFLoader("モデル就業規則.pdf").load()

# テキスト分割
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=125
)
chunks = splitter.split_documents(documents)

# ベクトルDB作成
db = InMemoryVectorStore.from_documents(
    chunks, OllamaEmbeddings(model="embeddinggemma")
)

# LLM準備
llm = ChatOllama(model="yuiseki/sarashina2.2:1b", temperature=0)

# プロンプト入力
while True:
    question = input("\nプロンプト（exitで終了）> ")
    if question.lower() == "exit":
        break
    if not question.strip():
        continue

    # 関連文書を検索
    docs = db.similarity_search(question, k=3)
    context = "\n".join(doc.page_content for doc in docs)

    # 回答生成
    prompt = f"""以下の参考資料だけを根拠に日本語で回答してください。
資料に答えがなければ「わかりません」と回答してください。

参考資料:
{context}

質問: {question}"""

    answer = llm.invoke(prompt)
    print("\n回答:", answer.content)
