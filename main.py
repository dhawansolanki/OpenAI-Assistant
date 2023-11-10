import os
import openai
from openai import OpenAI

client = OpenAI()
client.api_key = os.environ.get('OPENAI_API_KEY')

assistant = client.beta.assistants.create(
    name="Prompt",
    instructions="You are a personal assistant. Write and run code to answer questions",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="A boy playing guitar on beach during sunset."
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Dhawan Solanki. The user has a premium account."
)

run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)


messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

print("Message Received is : ",messages)