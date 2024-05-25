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
        user_input = request.form['user_input']
        file = request.files['file_input']
        
        if file:
            prompt = "Uploaded image: " + file.filename
            bot_response = generate_text(prompt)
        elif user_input.strip():
            prompt = user_input
            bot_response = generate_text(user_input)
        else:
            bot_response = "Please provide a prompt."
        
        # Render the template with the previous user input
        return render_template('index.html', user_input=user_input, bot_response=bot_response)
    
    # If it's a GET request or no input was provided, render the template with no previous input
    return render_template('index.html', user_input="", bot_response="")

if __name__ == '__main__':
    chatbot.run_program()
    app.run(debug=True)
