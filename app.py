from flask import Flask, render_template, request
from chatbot_settings import ChatbotSettings
from extract_data import run_data_extraction

app = Flask(__name__)
chatbot = ChatbotSettings()

class FlaskApp:
    _bot_response = None  # Define _bot_response as a class-level variable

    @staticmethod
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            user_input = request.form['user_input']
            file = request.files['file_input'] 
            
            if file:
                prompt = "Uploaded image: " + file.filename
                FlaskApp._bot_response = FlaskApp.generate_text(prompt)
                return render_template('chat_output.html', user_input=user_input, bot_response=FlaskApp._bot_response)
                
            elif user_input.strip():  
                prompt = user_input
                FlaskApp._bot_response = FlaskApp.generate_text(prompt)
                return render_template('chat_output.html', user_input=user_input, bot_response=FlaskApp._bot_response)
                
            else:
                FlaskApp._bot_response = "Please provide a prompt."
                return render_template('index.html', user_input=user_input, bot_response=FlaskApp._bot_response)

        return render_template('index.html')

    @staticmethod
    @app.route('/locations', methods=['GET', 'POST'])
    def locate():
        if request.method == 'POST':
            state = request.form['state']
            city = request.form['city']
            locations = run_data_extraction(FlaskApp._bot_response, chatbot, state, city)
            print(locations)
        return render_template('locations.html')

    @staticmethod
    def generate_text(prompt):
        convo = chatbot._chat_session
        convo.send_message(prompt)
        return convo.last.text


if __name__ == '__main__':
    chatbot.run_program()
    app.run(debug=True)
