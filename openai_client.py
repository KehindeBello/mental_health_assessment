from openai import OpenAI

#
class OpenAPIClient:
    client = None

    @staticmethod
    def build_client():
        if OpenAPIClient.client is None:
            OpenAPIClient.client = OpenAI(
                api_key=''  # Ensure you replace with your actual API key
            )
        return OpenAPIClient.client

    @staticmethod
    def query_responses(responses: list):
        client = OpenAPIClient.build_client()
        message = (
            "Summarize the mental health status based on the following responses:\n"
            f"{responses}\n"
            "Provide a summary indicating the potential presence of anxiety, depression, or stress, and the severity."
        )
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            temperature=1,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. I want you to give me a summary of this "
                                              "person's mental health"},
                {'role': 'user', 'content': message}
            ],
            max_tokens=256,
            n=1,
            stop=None
        )
        # Ensure the response structure is as expected; the path to the message might need adjustments
        return response.choices[0].message.content
