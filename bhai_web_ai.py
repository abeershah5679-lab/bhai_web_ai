from flask import Flask, request, jsonify
import datetime
import random

app = Flask(__name__)

jokes = [
    "Why don't programmers like nature? Too many bugs.",
    "Why did the computer go to therapy? It had too many bytes of trauma.",
    "Why was the math book sad? It had too many problems."
]

def process_command(command):
    command = command.lower()

    if "time" in command:
        return "The time is " + datetime.datetime.now().strftime("%H:%M")

    elif "joke" in command:
        return random.choice(jokes)

    elif "hello" in command:
        return "Hello bro, Bhai AI web version is online."

    elif "spotify" in command:
        return "OPEN_SPOTIFY"

    elif "youtube" in command:
        return "OPEN_YOUTUBE"

    elif "google" in command:
        return "OPEN_GOOGLE"

    elif "calculate" in command:
        try:
            expression = command.replace("calculate", "")
            result = eval(expression)
            return "The answer is " + str(result)
        except:
            return "Sorry, I cannot calculate that."

    else:
        return "I did not understand that."

@app.route("/")
def home():
    return """
    <html>
    <body style='font-family: Arial; text-align: center; margin-top: 50px;'>
        <h1>BHAI AI WEB</h1>

        <input type="text" id="commandInput" placeholder="Type your command">
        <button onclick="sendCommand()">Send</button>

        <p id="output"></p>

        <script>
            function sendCommand() {
                const text = document.getElementById("commandInput").value;

                fetch("/command", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({command: text})
                })
                .then(response => response.json())
                .then(data => {

                    let response = data.response;

                    if (response === "OPEN_SPOTIFY") {
                        window.open("https://open.spotify.com");
                        response = "Opening Spotify";
                    }
                    else if (response === "OPEN_YOUTUBE") {
                        window.open("https://www.youtube.com");
                        response = "Opening YouTube";
                    }
                    else if (response === "OPEN_GOOGLE") {
                        window.open("https://www.google.com");
                        response = "Opening Google";
                    }

                    document.getElementById("output").innerText = "AI: " + response;

                    const speech = new SpeechSynthesisUtterance(response);
                    speechSynthesis.speak(speech);
                });
            }
        </script>
    </body>
    </html>
    """

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    response = process_command(data["command"])
    return jsonify({"response": response})

if __name__ == "__main__":
    print("Bhai AI Web is starting...")
    app.run(host="0.0.0.0", port=5000, debug=True)