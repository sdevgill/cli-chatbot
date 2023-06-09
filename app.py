import argparse

import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end


def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end


def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end


def main():
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT-4"
    )

    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="friendly and helpful",
    )

    parser.add_argument(
        "--show-response",
        action="store_true",
        help="Display the response object when exiting",
    )

    args = parser.parse_args()

    initial_prompt = (
        f"You are a conversational chatbot. Your personality is: {args.personality}"
    )
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            user_input = input("\n" + bold(blue("You: ")))

            if user_input.lower() in ["exit", "quit"]:
                print("Exiting...")
                break

            messages.append({"role": "user", "content": user_input})

            res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

            messages.append(res["choices"][0]["message"].to_dict())
            print(bold(red("Assistant: ")), res["choices"][0]["message"]["content"])

            total_tokens = res["usage"]["total_tokens"]
            print(
                "\n"
                + bold("Cost: $")
                + f"{total_tokens * 0.000002:.6f}"
                + " --- Tokens used: "
                + str(total_tokens)
            )
            print("\n" + "----------------------------------------")

        except KeyboardInterrupt:
            print("Exiting...")
            break

    if args.show_response:
        print(res)


if __name__ == "__main__":
    main()
