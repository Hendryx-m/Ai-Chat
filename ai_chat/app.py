from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


app = Flask(__name__)

# Initializing the AI model and tokenizer

MODEL_NAME = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Tokenizing the user input and appending the end of string token
    input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    
    # Generating a response from the AI model
    output_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    #  Extracting generated tokens from the AI
    generated_tokens = output_ids[:, input_ids.shape[-1]:][0]
    # Decoding the output, skipping input prompt tokens
    response_text = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)