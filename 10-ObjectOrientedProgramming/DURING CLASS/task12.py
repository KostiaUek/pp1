class TV:

    def __init__(self, is_on, channel_no=1):
        self.is_on = is_on
        self.channel_no = channel_no

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        status = "on" if self.is_on else "off"
        return f'TV is {status}, channel {str(self.channel_no)}'


if __name__ == "__main__":
    tv = TV(False)
    print(tv.show_status())
    tv.turn_on()
    print(tv.show_status())
    tv.turn_off()
    print(tv.show_status())
