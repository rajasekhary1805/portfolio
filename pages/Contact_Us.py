import streamlit as sl
from send_email import send_email

sl.header("Contact Me")

with sl.form(key="email_forms"):
    user_email = sl.text_input("Your Email Address")
    input_message = sl.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{input_message}
    """
    button = sl.form_submit_button("Submit")
    if button:
        send_email(message)
        sl.info('Your Email sent successfully..')
