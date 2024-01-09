class Phone:

    def __init__(self, model, os_type, is_on):
        self.model = model
        self.os_type = os_type
        self.is_on = is_on
        self.phone_number = ""

    def __str__(self):
        phone_number_string = f' Phone number: {self.phone_number}' if self.phone_number else ""
        phone_state = ", turned on." if self.is_on else ", turned off."
        return f'{self.model} {self.os_type}{phone_state}{phone_number_string}'

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def add_sim_card(self, phone_number):
        self.phone_number = phone_number


phone = Phone("iPhone X", "IOS 15.4", False)
print(phone)
phone.add_sim_card("+1234567890")
phone.turn_on()
print(phone)
