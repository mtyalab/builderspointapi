import requests


api_base_url = "https://api.mailgun.net/v3/sandbox076c4c47ced94eddae953015fc395f70.mailgun.org/messages"
api_key = "08e2bb984c2a54263deda28d188512f8-c4d287b4-576fae56"


def registration_success_notification(email_address: str):
    return requests.post(
        api_base_url,
        auth=("api", api_key),
        data={
            "from": "<mailgun@sandbox076c4c47ced94eddae953015fc395f70.mailgun.org>",
            "to": [email_address],
            "subject": "Registration Success",
            "html": "<html><body><h1>Welcome to My App!</h1><p>Thank you for registering!</p></body></html>"})


def send_reset_code(email: str, code: str):
    code = code
    receiver_email = email  # Enter receiver address

    message = f"""\
    Subject: BuildersPoint: Security Code
    
    Your password reset code is : {code}
    """

    return requests.post(
        api_base_url,
        auth=("api", api_key),
        data={
            "from": "<mailgun@sandbox076c4c47ced94eddae953015fc395f70.mailgun.org>",
            "to": [receiver_email],
            "subject": "BuildersPoint: Security Code",
            "text": message,
        }
    )
