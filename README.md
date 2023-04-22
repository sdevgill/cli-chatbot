# CLI Chatbot

This is a command-line interface (CLI) chatbot powered by GPT language model. It is built with Python and uses the OpenAI GPT API to generate responses to user inputs.

## Requirements

- Python ^3.11
- Poetry ^1.4.0

## Installation

1. Clone the repository and navigate to the project directory.

```
git clone git@github.com:sdevgill/cli-chatbot.git
cd cli-chatbot
```

2. Create an .env file and add your OpenAI API key as shown in the .env.example file.

```
cp .env.example .env
```

3. Install the requirements.

```
poetry install
```

4. Activate the virtual environment.

```
poetry shell
```

5. Run the application.

```
python main.py
```

## Usage

Type a message and press Enter to send it to the chatbot.
The chatbot will respond with a generated message based on the input.
