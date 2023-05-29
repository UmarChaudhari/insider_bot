import tempfile
from flask import Flask, render_template, request, jsonify
import pandas as pd
from query_pinecone import query_db
from upsert_pinecone import upser_to_db
import os,textract
app = Flask(__name__)


@app.route('/')
def chatbot():
    return render_template('chatbot.html')

@app.route('/uploadfile')
def otherpage(message=''):
    
    return render_template('uploadfile.html',message=message)


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['pdf-file']

    file_name = file.filename
    # # Get the file extension
    file_extension = os.path.splitext(file_name)[1].lower()


    # Check if the file extension is txt, docx, or pdf
    if file_extension == '.txt':
        # File is a TXT file
        # Perform processing for TXT files
        pass
    elif file_extension == '.docx':
        # File is a DOCX file
        # Perform processing for DOCX files
        pass
    elif file_extension == '.pdf':
        # File is a PDF file
        # Perform processing for PDF files
        
        # Save the uploaded file to a temporary location
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)

        # Upserting pdf data into Pinecone Database
        
        upser_to_db(file_path,file_name)

        # Delete the uploaded file to a temporary location
        os.remove(file_path)
        pass

    elif file_extension == '.csv':
        # File is a PDF file
        # Perform processing for PDF files
        print(pd.read_csv(file))
        pass
    else:
        # File has an unsupported extension
        message = "File has an unsupported extension"
        return render_template('uploadfile.html',message=message)
    
    # Perform processing on the uploaded file
    # ...

    # Return a response or perform additional actions
    message = 'File uploaded successfully.'
    return render_template('uploadfile.html',message=message)


@app.route('/query', methods=['POST'])
def process_query():

    query = request.json['query']
    
    result = query_db(query)
    
    response = {'answer': result}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, timeout=120)
