from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter
import textract


# Create function to count tokens
def count_tokens(text: str) -> int:
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    return len(tokenizer.encode(text))


# Split text into chunks
def get_text_splitter():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 512,
        chunk_overlap  = 20,
        length_function = count_tokens,
    )
    return text_splitter


# Converting pdf to chunks using split_text funcion
def pdf_to_chunks(file):
    doc = textract.process(file)
    text = doc.decode()
    text_splitter = get_text_splitter()
    chunks=text_splitter.split_text(text)
    return chunks


# Converting Query into langchain.Document for it to be accepted by ChatGPT (qa.chain function)
def text_to_docs(text):
    text_splitter = get_text_splitter()
    docs = text_splitter.create_documents([text])
    return docs