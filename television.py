class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        # Method to turn the TV on and off
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Unmute when turning off

    def mute(self) -> None:
        # Method to mute and unmute the TV
        if self.__status == True:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        # Method to increase the TV channel
        if self.__status and self.__channel < Television.MAX_CHANNEL:
            self.__channel = (self.__channel + 1)

    def channel_down(self) -> None:
        # Method to decrease the TV channel
        if self.__status and self.__channel > Television.MIN_CHANNEL:
            self.__channel = (self.__channel - 1)

    def volume_up(self):
        # Method to increase the TV volume
        if self.__status and not self.__muted:
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self):
        # Method to decrease the TV volume
        if self.__status and not self.__muted:
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        """ 
        :param self: variable of Television class
        """
        power_status = "True" if self.__status else "False"
        if self.__muted == True:
            return f"# Power = [{power_status}], Channel = [{self.__channel}], Volume = [0]"
        # Method to format the TV object values
        return f"# Power = [{power_status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
 

