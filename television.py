class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        :param: self
        Sets each variable to an instance.
        """
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        :param:self
        Toggling self.__status to true or false 
        """
        # Method to turn the TV on and off
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Unmute when turning off

    def mute(self) -> None:
         """
        :param:self
        Toggling self.__muted to true or false 
        """
        # Method to mute and unmute the TV
        self.__muted = not self.__muted

    def channel_up(self) ->:
         """
        :param:self
        Increment channel to go up to three 
        """
        # Method to increase the TV channel
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
         """
        :param:self
        Increment channel to go down to three 
        """
        # Method to decrease the TV channel
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
         """
        :param:self
        Increment Volume to go up to two
        """
        # Method to increase the TV volume
        if self.__status and not self.__muted:
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
         """
        :param:self
        Increment volume to go down to two 
        """
        # Method to decrease the TV volume
        if self.__status and not self.__muted:
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self)-> str:
         """
        :param:self
        Displaying the cureent status of the variables
        """
        # Method to format the TV object values
        power_status = "On" if self.__status else "Off"
        return f"Power [{power_status}], Channel [{self.__channel}], Volume [{self.__volume}]"


if __name__ == "__main__":
    
