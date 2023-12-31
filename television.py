class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        # Method to turn the TV on and off
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Unmute when turning off

    def mute(self):
        # Method to mute and unmute the TV
        self.__muted = not self.__muted

    def channel_up(self):
        # Method to increase the TV channel
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        # Method to decrease the TV channel
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        # Method to increase the TV volume
        if self.__status and not self.__muted:
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        # Method to decrease the TV volume
        if self.__status and not self.__muted:
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self):
        # Method to format the TV object values
        power_status = "On" if self.__status else "Off"
        return f"Power = [{power_status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"


