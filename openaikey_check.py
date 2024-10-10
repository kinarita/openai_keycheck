import openai

# Set your OpenAI API key
api_key = "SET_YOUR_API_KEY"  # Enter your API key here
openai.api_key = api_key

def check_api_key_validity():
    try:
        # Send a simple request to check if the key is valid
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        )
        print("API key is valid. The request was successful.")
    except openai.error.AuthenticationError:
        print("API key is invalid. Please set the correct key.")
    except openai.error.OpenAIError as e:
        print(f"An OpenAI API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Check the validity of the API key
check_api_key_validity()
