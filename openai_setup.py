import os,openai
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Connecting to OpenAI using secret API Key to perform various tasks
def connect_openai():
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key=os.environ["OPENAI_API_KEY"]
    return

def generate_answer(query,context_docs):
    chain = load_qa_chain(OpenAI(temperature=0.1), chain_type="stuff")
    result=chain.run(input_documents=context_docs, question=query)
    return result

