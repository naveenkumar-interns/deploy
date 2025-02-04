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
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


@app.route('/llm', methods=['GET'])
def llm():
    text = llm.invoke("hi").content
    return jsonify({'message': 'Hello, World!',"response":text})

if __name__ == '__main__':
    app.run()
