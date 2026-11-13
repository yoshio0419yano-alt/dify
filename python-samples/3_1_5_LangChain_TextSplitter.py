from langchain_text_splitters import RecursiveCharacterTextSplitter

long_text = """
ChatGPT GPT-5は、OpenAIがリリースした最新かつ最高性能の言語モデルで、
以前のモデルを統合し、高速な応答と深い推論能力を両立させています。
文章作成、コーディング、医療、画像認識など、多くの分野で精度が向上し、
事実と異なる内容を生成する「ハルシネーション」も大幅に減少しました。
また、ユーザーの状況や知識レベルに合わせて回答を調整する能力も強化され、
より賢く、使いやすいモデルとなっています。
"""
print(len(long_text))
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
)
text_list = text_splitter.split_text(long_text)
print(text_list)
print(len(text_list))