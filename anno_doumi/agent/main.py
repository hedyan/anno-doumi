from stt import STTAgent
from command import CommandAgent


if __name__ == '__main__':
    stt_agent = STTAgent()
    cmd_agent = CommandAgent()

    for text in stt_agent.start_listening():
        print(f"Detected text by stt_agent : {text}")
        try:
            result = cmd_agent.process_command(text)
            print(f"Command parsed by cmd_agent : {result}.")
        except Exception as e:
            print(f"Error processing command: {e}")
            result = "Error processing command"
            print(result)
