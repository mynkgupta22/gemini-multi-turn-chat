#!/usr/bin/env python3
"""
Gemini Multi-Turn Chat

A simple console-based chatbot that uses the Google Gemini API
to maintain conversation context across multiple turns.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

def setup_gemini(temperature=0.7, top_p=0.95, top_k=40):
    """Initialize and configure the Gemini API client."""
    # Load API key from environment variable
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key or set it as an environment variable.")
        exit(1)
    
    # Configure the Gemini API client
    genai.configure(api_key=api_key)
    
    # Set up generation config
    generation_config = genai.GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k
    )
    
    # Return model with generation config
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

def get_user_input(prompt):
    """Get input from the user with the given prompt."""
    return input(prompt)

def main():
    print("Welcome to the Gemini Multi-Turn Chat!")
    print("You can have a conversation with the Gemini AI model.")
    print("Type 'exit' at any time to end the conversation.\n")
    
    # Ask if the user wants to configure model parameters
    configure_params = get_user_input("Would you like to configure model parameters? (y/n): ").lower()
    
    # Default parameters
    temperature = 0.7
    top_p = 0.95
    top_k = 40
    
    # Allow user to configure parameters if desired
    if configure_params.startswith('y'):
        try:
            temperature = float(get_user_input("Enter temperature (0.0-1.0, default 0.7): ") or temperature)
            top_p = float(get_user_input("Enter top_p (0.0-1.0, default 0.95): ") or top_p)
            top_k = int(get_user_input("Enter top_k (1-100, default 40): ") or top_k)
        except ValueError:
            print("Invalid input. Using default parameters.")
            temperature = 0.7
            top_p = 0.95
            top_k = 40
    
    # Initialize the Gemini model with the specified parameters
    model = setup_gemini(temperature=temperature, top_p=top_p, top_k=top_k)
    
    # Start a chat session
    chat = model.start_chat(
        history=[]
    )
    
    # First turn
    user_input = get_user_input("\nYou: ")
    if user_input.lower() == 'exit':
        return
    
    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}")
    
    # Continue the conversation for multiple turns
    while True:
        user_input = get_user_input("\nYou: ")
        if user_input.lower() == 'exit':
            break
        
        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}")

if __name__ == "__main__":
    main()
