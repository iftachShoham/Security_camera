import time
import pyautogui
import keyboard as k
import pywhatkit


class WhatsappSending:
    def __init__(self):
        self.phone_number = "+972548031740"  # Tali's phone number.
        self.message = "I love you"  # Default message idk...
        self.phone_numbers = []

    @staticmethod
    def send_message(phone_number="+972548031740", message="I love you"):
        # Sending the WhatsApp Message
        # The true value ref the fact that its close.
        pywhatkit.sendwhatmsg_instantly(phone_number, message, 5, True, 30)

        # clicks on the screen so when pressing enter works.
        time.sleep(1)
        pyautogui.click(1050, 950)
        time.sleep(1)
        k.press_and_release('enter')

        # Displaying a Success Message
        print("WhatsApp message sent!")

    def add_new_phone_to_phone_book(self,new_phone):
        # Maybe ill want to check here in the future if the number is correct.
        # Function for checking....
        self.phone_numbers.append(new_phone)


    def Notify_all(self, _message):
        # When I want to notify all.
        for phone in self.phone_numbers:
            self.send_message(phone, _message)
