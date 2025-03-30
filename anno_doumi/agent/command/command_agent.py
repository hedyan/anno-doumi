import os

from openai import OpenAI

test_command_1 = "Bring some cotton from Seoul to Tokyo"
test_command_2 = "Return Sun-Shin to Busan"
test_command_3 = "Return the citrus fleet to Hawaii"
test_command_4 = "Build a cathedral on the right side of Jeju"


class CommandAgent:
    AGENT_NAME = "CommandAgent"
    INSTRUCTION_FILE = "anno_doumi/command/instruction_v2.txt"

    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def process_command(self, command_text):
        with open(self.INSTRUCTION_FILE, 'r', encoding='utf-8') as file:
            instructions = file.read()

        response = self.openai_client.chat.completions.create(model='gpt-4o-mini', messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": command_text}
        ])
        return response.choices[0].text.strip()
