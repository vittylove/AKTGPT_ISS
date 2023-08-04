from haystack.utils import convert_files_to_docs
from haystack.nodes import PDFToTextConverter, PreProcessor
import os
from multiprocessing import freeze_support

def preprocess_documents():
    # 获取当前工作目录
    current_dir = os.getcwd()

    # 设置子文件夹路径
    #doc_dir = os.path.join(current_dir, "data")
    
    # 读取全部文件
    #all_docs = convert_files_to_docs(dir_path=doc_dir)

    converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])
    doc_pdf = converter.convert(file_path="./data/Administrative.pdf", meta=None)[0]


    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=False,
        split_by="word",
        split_length=100,
        split_respect_sentence_boundary=True,
    )
    #docs = preprocessor.process(all_docs)

    docs = preprocessor.process([doc_pdf])

    # 返回预处理后的文档
    return docs

if __name__ == '__main__':
    freeze_support()
    docs = preprocess_documents()
