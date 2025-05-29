# Gemini Multi-Turn Chat

A simple interactive console-based chatbot that uses the Google Gemini API to maintain conversation context across multiple turns.

## Features

- Maintains conversation context across multiple turns
- Configurable model parameters (temperature, top_p, top_k)
- Simple console-based interface
- Uses the latest Gemini 1.5 Flash model

## Prerequisites

- Python 3.7+
- Google Gemini API key (get one at [Google AI Studio](https://ai.google.dev/))

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/gemini-multi-turn-chat.git
   cd gemini-multi-turn-chat
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Gemini API key:
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file and add your API key.

## Usage

Run the script:
```bash
python gemini_chat.py
```

The program will:
1. Ask if you want to configure model parameters (temperature, top_p, top_k)
2. Start a conversation with the Gemini model
3. Allow you to have a multi-turn conversation, maintaining context between turns
4. Type 'exit' at any prompt to end the conversation

## Model Parameters

- **Temperature** (0.0-1.0): Controls randomness. Lower values make responses more focused and deterministic, while higher values make responses more creative and diverse.
- **Top_p** (0.0-1.0): Controls diversity via nucleus sampling. Lower values make responses more focused.
- **Top_k** (1-100): Controls diversity by limiting the token selection to the top k options. Lower values make responses more focused.

## Note

Do not commit your API key to version control. The `.env` file is included in `.gitignore` to prevent this.