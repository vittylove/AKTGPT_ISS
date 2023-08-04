#from haystack.document_stores import InMemoryDocumentStore
from haystack.document_stores import SQLDocumentStore
from haystack.nodes import PromptNode, PromptTemplate,AnswerParser
from haystack.nodes import BM25Retriever
from haystack.pipelines import Pipeline

from pre import preprocess_documents

def initialize_system():
    # 调用 preprocess_documents 函数获取预处理后的文档
    dataset = preprocess_documents()

    # 初始化内存数据库
    #document_store = InMemoryDocumentStore(use_bm25=True)
    document_store = SQLDocumentStore()
    document_store.write_documents(dataset)

    # 初始化检索器
    retriever = BM25Retriever(document_store=document_store, top_k=2)

    # 初始化PromptNode
    lfqa_prompt = PromptTemplate(
        prompt="""Synthesize a comprehensive answer from the following text for the given question.
                                    Provide a clear and concise response that summarizes the key points and information presented in the text.
                                    Your answer should be in your own words and be no longer than 50 words.
                                    \n\n Related text: {join(documents)} \n\n Question: {query} \n\n Answer:""",
        output_parser=AnswerParser(),
    )
    prompt_node = PromptNode(model_name_or_path="google/flan-t5-large", default_prompt_template=lfqa_prompt)

    # 初始化管道
    pipe = Pipeline()
    pipe.add_node(component=retriever, name="retriever", inputs=["Query"])
    pipe.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])

    return pipe


