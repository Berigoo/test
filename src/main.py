from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def reply():
    msg = request.form.get('Body')
    response = MessagingResponse()
    reply = response.message()

    if msg.strip().upper().startswith("#COMPLAINT"):
        complaint_text = msg[len("#COMPLAINT"):].strip()
        # Save to Google Sheets or log it
        print("New complaint:", complaint_text)
        reply.body("✅ Your complaint has been received:\n" + complaint_text)
    elif msg.strip().upper() == "#HELP":
        reply.body("Commands:\n#COMPLAINT your message\n#INFO\n#CONTACT")
    else:
        reply.body("❓ Unknown command. Type #HELP to see available options.")

    return str(response)

if __name__ == "__main__":
    app.run()
