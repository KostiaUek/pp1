class TV:

    def __init__(self, is_on=False, channel_no=1):
        self.is_on = is_on
        self.channel_no = channel_no

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        status = "on" if self.is_on else "off"
        return f'TV is {status}, channel {str(self.channel_no)}'

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no


if __name__ == "__main__":
    tv = TV()
    print(tv.show_status())
    tv.turn_on()
    print(tv.show_status())
    tv.set_channel(5)
    print(tv.show_status())
    tv.turn_off()
    print(tv.show_status())
