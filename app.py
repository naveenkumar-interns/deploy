from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'working'})
    
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/llmin', methods=['GET'])
def llmin():
    text = llm.invoke("hi").content
    return jsonify({"response":text})

@app.route('/llmout', methods=['POST'])
def response():
    text = request.json['message']
    text = llm.invoke(text).content
    return jsonify({"response":text})

if __name__ == '__main__':
    app.run()
