# CLI Chatbot

A GPT-powered Command Line Interface (CLI) chatbot that allows users to interact with an AI assistant via the terminal.

## Features

- Interactive conversation with a GPT-4 or GPT-3.5-turbo powered AI chatbot.
- Customizable chatbot personality.
- Colorful command-line interface for enhanced user experience.

## Installation

### Prerequisites

- Python ^3.11

### Steps

1. Clone the repository and navigate to the project directory.

```
git clone git@github.com:sdevgill/cli-chatbot.git
cd cli-chatbot
```

2. Install Poetry, a package manager for Python:

```
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install the required packages:

```
poetry install
```

4. Create and add your OpenAI API key to the `.env` file:

```
cp .env.example .env
```

## Usage

1. Activate the virtual environment:

```
poetry shell
```

2. Run the chatbot:

```
python app.py
```

3. Optionally, customize the chatbot's personality using the --personality flag:

```
python app.py --personality "a knowledgeable and insightful teacher"
python app.py --personality "rude and sarcastic"
```

4. Type your messages to the chatbot and press Enter. The chatbot will respond with its AI-generated message.

5. To exit the chat, press Ctrl+C.

## License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).
