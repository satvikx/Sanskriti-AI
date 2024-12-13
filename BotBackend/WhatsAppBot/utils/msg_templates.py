import json


# "buttons: The quick reply button payload length (165) exceeds limit (128)"
def booking_ticket(recipient, body):
    img_link = "https://www.trawell.in/admin/images/upload/14523999Bhopal_State_Archaeological_Museum_Main.jpg"
    place = "Bhopal State Archaeological Museum"
    date = "09/09/2024"
    time = "10 PM"
    button_payload = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": f"Further {body}"},
        }
    )

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "template",
        "template": {
            "name": "booking_tickets",
            "language": {
                "code": "en"
            },
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": img_link
                            }
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": place
                        },
                        {
                            "type": "text",
                            "text": date
                        },
                        {
                            "type": "text",
                            "text": time
                        },
                        # {
                        #     "type": "currency",
                        #     "currency": {
                        #     "fallback_value": "VALUE",
                        #     "code": "USD",
                        #     "amount_1000": 111
                        #     }
                        # },
                        # {
                        #     "type": "date_time",
                        #     "date_time": {
                        #     "fallback_value": "DATE",
                        #     }
                        # }
                    ]
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": "0",
                    "parameters": [
                        {
                            "type": "payload",
                            "payload": "button_payload"
                        }
                    ]
                },
            ]
        }
    }
    return json.dumps(payload)

