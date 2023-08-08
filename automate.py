import openai

# Set your OpenAI API key
openai.api_key = "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"

def correct_answer(question, answer):
    conversation = f"You: {question}\nAI: {answer}\nYou: Please correct the answer."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ],
    )
    corrected_answer = response['choices'][0]['message']['content']
    return corrected_answer

# Example usage
question = "What is the capital of France?"
answer = "The capitol of France is Paris."

corrected_answer = correct_answer(question, answer)
print(f"Corrected Answer: {corrected_answer}")
