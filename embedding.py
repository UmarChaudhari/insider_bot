import pandas as pd
import openai

# Returns embedding of text provided
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input = text, model=model)['data'][0]['embedding']


def process_col1(value):
    return get_embedding(value)


# for given chunks, it creates a df with 3 columns:  id | text(chunk) | embedding
def get_embeddings(chunks):
    df = pd.DataFrame(
        {'text': chunks}
    )
    df['id']="my_chatbot"
    # Apply the function to create the second column
    df['embed'] = df['text'].apply(process_col1)
    return df
