from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Twilio sends a POST request with the URL of the voice recording
    recording_url = request.form.get("RecordingUrl")
    print(f"Received a recording from Twilio: {recording_url}")

    # --- FOR NOW, WE WILL USE A FIXED RESPONSE ---
    # This is the text from the original document [cite: 113]
    response_text = "तपाईंको खाता ब्यालेन्स ५०,००० रुपैयाँ छ।"

    # We tell Twilio to <Say> this text back to the caller using TwiML (Twilio's XML)
    # We can even suggest a voice, like the Indian voice 'Polly.Aditi'.
    twiml_response = f"<Response><Say voice='Polly.Aditi'>{response_text}</Say></Response>"

    # We return the TwiML response
    return Response(twiml_response, mimetype='text/xml')

if __name__ == "__main__":
    # The app will run on the port provided by the hosting service
    app.run(host='0.0.0.0', port=5001)