import google.generativeai as genai
from ai_training import safety_settings, generation_config, system_instruction, history

prompt_string = "With this response just name me 3 possible medical places I can go nearby to get this condition treated. List the 3 locations and just the 3 locations and nothing else in the response...: "
class ChatbotSettings:
    def __init__(self):
        self._api_key = "AIzaSyB4OUHNrACY9K5LkPyAtQ416tlOX1jTjSk"
        self._safety_settings = []
        self._generation_config = {}
        self._model = None
        self._chat_session = None

    def configure_api(self):
        genai.configure(api_key=self._api_key)

    def set_safety_settings(self):
        self._safety_settings = safety_settings
        
    def set_generation_config(self):
        self._generation_config = generation_config

    def set_model(self):
        self.configure_api()
        self.set_safety_settings()
        self.set_generation_config()

        self._model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            safety_settings=self._safety_settings,
            generation_config=self._generation_config,
            system_instruction=system_instruction,
        )

    def create_chat_session(self):
        self.set_model()
        self._chat_session = self._model.start_chat(history=history)

    def run_program(self):
        self.create_chat_session()


