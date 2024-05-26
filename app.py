from flask import Flask, render_template, request
from chatbot_settings import ChatbotSettings
from chatbot_settings import prompt_string

app = Flask(__name__)
chatbot = ChatbotSettings()

def generate_text(prompt):
    convo = chatbot._chat_session
    convo.send_message(prompt)
    return convo.last.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']  # Get text input from the form
        file = request.files['file_input']  # Get uploaded file from the form
        
        if file:
            prompt = "Uploaded image: " + file.filename
            bot_response = generate_text(prompt)
            run_data_extraction(bot_response)
            
        elif user_input.strip():  # Check if user_input is not empty or whitespace
            prompt = user_input
            bot_response = generate_text(prompt)
            run_data_extraction(bot_response)
        else:
            bot_response = "Please provide a prompt."
        
        return render_template('index.html', user_input=user_input, bot_response=bot_response)
    return render_template('index.html')


class ExtractData:
    def __init__(self, response):
        self._response = response
        self._manipulated_data = None

    def take_bot_response(self):    
        return self._response
    
    def manipulate_bot_response(self):
        bot_response = self._response
        manipulate_data = generate_text(prompt_string + bot_response)
        self._manipulated_data = manipulate_data

    def run_class(self):
        self.take_bot_response()
        self.manipulate_bot_response()
        print(self._manipulated_data)
        return self._manipulated_data
    
def run_data_extraction(response):
    bot_response = ExtractData(response).run_class()




if __name__ == '__main__':
    chatbot.run_program()
    app.run(debug=True)
