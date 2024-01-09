class TV:

    def __init__(self, is_on=False, channel_no=1, channels=None):
        self.is_on = is_on
        self.channel_no = channel_no
        self.channels = channels

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        status = "on" if self.is_on else "off"
        channel_name = " (" + self.channels[self.channel_no - 1] + ")" if self.channels and self.channel_no - 1 < len(self.channels) else ""
        return f'TV is {status}, channel {str(self.channel_no)}{channel_name}'

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list: list):
        self.channels = channels_list

    def show_channels(self):
        if not self.channels:
            return "There are no channels set"

        prefix = "Channels list: \n"

        i = 0
        while i < len(self.channels):
            prefix += f'{str(i + 1)} {str(self.channels[i])} \n'
            i += 1

        return prefix


if __name__ == "__main__":
    tv = TV()
    print(tv.show_status())
    tv.turn_on()
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"])
    print(tv.show_status())
    tv.set_channel(2)
    print(tv.show_status())
    tv.set_channel(100)
    print(tv.show_status())
    tv.turn_off()
