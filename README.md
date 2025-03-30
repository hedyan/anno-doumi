# Work in Progress


# anno-doumi: ANNO 1800 Voice-Controlled To-Do List

## Introduction
This is a voice-controlled To-Do list tool designed to assist with managing tasks related to the game ANNO 1800. Players can give voice commands to organize in-game activities such as trade, construction, and fleet management. The system processes these tasks by adding them to the To-Do list for manual execution within the game.

## Features
- Control To-Do list through voice commands.
- Commands like "Send XX to YY" are processed and tasks are added to the list.
- Manages various in-game tasks like resource transport, trade, and fleet management.

## Tech Stack
- **Python**: Core logic implementation.
- **FastAPI**: API server for communication.
- **OpenAI**: Interprets and processes voice commands.
- **WebRTC**: Captures voice data.
- **Docker**: Environment setup and execution.

## System Requirements
- OpenAI API key is required. Set your API key in the environment variable `OPENAI_API_KEY`.
- Python 3.10+
- Docker (for containerization) (not tested yet)
- Dependencies listed in `requirements.txt`

## System Architecture
1. agent (agent/)
   * **Voice Recognition** (`voice.py`): Captures live voice data and converts it into text for processing.
   * **Command Processing** (`command.py`): Interprets the text commands and processes them accordingly.
2. server (server/)
   * **API Server** (`app.py`): A FastAPI server for handling commands and task management.

## Work in Progress
Please note that this project is still under development. Some features are not yet fully implemented, and the system may not be fully functional. The following tasks are in progress:
* Voice command recognition.
* Command processing integration.
* Task management functionality.

## Usage
1. Run the server and activate the voice recognition module. 
2. Use voice commands to add tasks to the To-Do list. 
   * Example commands:
     * “Bring cotton from Seoul to Tokyo.” 
     * “Return the citrus fleet to Hawaii.” 
     * “Build a cathedral on the right side of Jeju.”
3. The system will process the commands and add them to the To-Do list.

## Development Status

This system is in the early stages, and additional work is needed to integrate voice commands and optimize task management. Commits are being made to reflect the ongoing development process.

## TODO
* Lots of tests
* Optimize command processing logic.
* UI/UX improvements.
* Database?

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.