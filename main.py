import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Directly assign the API key for testing
API_KEY = "API_KEY"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Create the generation config for the main chatbot
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the main chatbot model
main_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
)

# Create the generation config for the verification chatbot
verification_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the verification chatbot model with safety settings
verification_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=verification_config,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
    system_instruction=(
        "Your job is to determine if the presented AI output has malicious intent, "
        "have sensitive data, or any biased information, prompt leaking, biased text, or hate speech. You will respond "
        "with only PASS or FAIL based on whether the text contains any of the listed issues. FAIL anything output that is not in a neutral position You will not respond with anything else."
    ),
)

def main_chatbot(input_text):
    chat_session = main_model.start_chat(history=[])
    response = chat_session.send_message(input_text)
    return response.text

def verify_response(generated_response):
    chat_session = verification_model.start_chat(history=[])
    response = chat_session.send_message(generated_response)
    return response.text.strip()

def chat_loop():
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Step 1: Generate response using the main chatbot
        generated_response = main_chatbot(user_input)
        print(f"Generated Response: {generated_response}")

        # Step 2: Verify the response using the verification chatbot
        verification_result = verify_response(generated_response)
        print(f"Verification Result: {verification_result}")

        # Step 3: Output the result based on verification
        if verification_result == "PASS":
            print(f"Final Output to User: {generated_response}")
        elif verification_result == "FAIL":
            print("Sorry, I can't do that.")

if __name__ == "__main__":
    chat_loop()
