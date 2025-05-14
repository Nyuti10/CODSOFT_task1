import re
from datetime import datetime


def get_time():
    now = datetime.now()
    return now.strftime('%H:%M:%S')

def get_date():
    now = datetime.now()
    return now.strftime('%Y-%m-%d')

def calculate_expression(user_input):
    # Extract the math expression from the input
    # Accepts: what is 2 + 2, calculate 5 * 7, what is 10 divided by 2
    expr = user_input.lower()
    expr = expr.replace('what is', '').replace('calculate', '').strip()
    expr = expr.replace('divided by', '/').replace('times', '*').replace('x', '*')
    expr = expr.replace('plus', '+').replace('minus', '-')
    # Remove any non-math words
    expr = re.sub(r'[^0-9\+\-\*/\.\(\) ]', '', expr)
    try:
        result = eval(expr, {"__builtins__": None}, {})
        return f"The answer is {result}."
    except Exception:
        return "Sorry, I couldn't calculate that."

def chatbot():
    print("Chatbot: Hello! I'm your rule-based chatbot. Type 'bye' or 'exit' to quit.")
    while True:
        user_input = input('You: ').strip()
        if not user_input:
            continue
        normalized = user_input.lower().strip()

        # Exit
        if normalized in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        # Greetings
        elif normalized in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I help you today?")

        # Identity
        elif re.search(r"what'?s your name|who are you", normalized):
            print("Chatbot: I'm a rule-based chatbot.")

        # Well-being
        elif 'how are you' in normalized:
            print("Chatbot: I'm doing great! Thanks for asking.")

        # Time
        elif re.search(r"what('?s| is) the time|what time is it", normalized):
            print(f"Chatbot: The current time is {get_time()}.")

        # Date
        elif re.search(r"what('?s| is) the date today|what day is it", normalized):
            print(f"Chatbot: Today's date is {get_date()}.")

        # Math
        elif re.search(r"(what is|calculate) [0-9\s\+\-\*/xX\.]+|divided by|times|plus|minus", normalized):
            print(f"Chatbot: {calculate_expression(normalized)}")

        # Joke
        elif 'tell me a joke' in normalized:
            print("Chatbot: Why did the computer show up at work late? It had a hard drive!")

        # Thank you
        elif 'thank you' in normalized or 'thanks' in normalized:
            print("Chatbot: You're welcome!")

        # Unrecognized
        else:
            print("Chatbot: Sorry, I didn't understand that.")

if __name__ == '__main__':
    chatbot() 