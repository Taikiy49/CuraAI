from geolocation import location_summary

prompt_string = "With this response just name me 3 possible medical places I can go nearby to get this condition treated. List the 3 locations and just the 3 locations and nothing else in the response...: "

def generate_text(prompt, chatbot):
    convo = chatbot._chat_session
    convo.send_message(prompt)
    return convo.last.text


class ExtractData:
    def __init__(self, response, chatbot, state, city):
        self._response = response
        self._manipulated_data = None
        self._chatbot = chatbot
        self._state = state
        self._city = city

    def take_bot_response(self):    
        return self._response
    
    def manipulate_bot_response(self):
        bot_response = self._response
        manipulate_data = generate_text(f"{prompt_string}{bot_response} Give me locations in {self._state}: {self._city}. Give it to me in comma-separated values", self._chatbot)
        self._manipulated_data = manipulate_data

    def get_locations(self):
        self.take_bot_response()
        self.manipulate_bot_response()
        return self._manipulated_data
    
def run_data_extraction(response, chatbot, state, city):
    coordinates_list = []
    locations = list(ExtractData(response, chatbot, state, city).get_locations().strip().split(','))
    for location in locations:
        coordinates_list.append(location_summary(location, state, city))
    return coordinates_list
