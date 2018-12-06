import imaplib
import getpass
import email
import time
import serial
import os

os.system('cls')
ser = serial.Serial('COM3', 9600)
user = getpass.getpass('Username: ')
password = getpass.getpass('Password: ')
messages = 0
os.system('cls')
def send_arduino_signal(signal):
    ser.write(signal)

def parse_emails(Mail):
    global messages
    rv,data = Mail.search(None, "UNSEEN")
    new_messages = len(data[0].split())
    if(new_messages == 0):
        send_arduino_signal('0')
        os.system('cls')
        print("There are no unread messages.")
        messages = 0
        return

    if(new_messages > messages):
        messages = new_messages
        os.system('cls')
        if(messages == 1):
            print("There is {0} unread message.".format(messages))
        else:
            print("There are {0} unread messages.".format(messages))
    send_arduino_signal('1')

def connect_to_gmail(email, password):
    Mail = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        Mail.login(user, password)
    except imaplib.IMAP4.error:
        print("Login failed, please ensure your internet is connected and try again")
    
    rv, data = Mail.select("INBOX", readonly=True)
    if(rv=="OK"):
        parse_emails(Mail)
        Mail.close()
    Mail.logout()

while True:
    connect_to_gmail(email, password)
    time.sleep(2)
