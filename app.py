from flask import Flask, render_template, request
from chatbot_settings import ChatbotSettings

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
            bot_response = generate_text(user_input)
            run_data_extraction(bot_response)
        else:
            bot_response = "Please provide a prompt."
        
        return render_template('index.html', user_input=user_input, bot_response=bot_response)
    return render_template('index.html')


class ExtractData:
    def __init__(self, response):
        self.response = response
    def take_bot_response(self):
        return self.response
    

def run_data_extraction(response):
    bot_response = ExtractData(response).take_bot_response()
    print(bot_response)



if __name__ == '__main__':
    chatbot.run_program()
    app.run(debug=True)
