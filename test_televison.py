from television import *
import pytest 

def test_init():
    tv = Television()
    tv.power()
    assert str(tv) == "# Power = [True], Channel = [0], Volume = [0]"
    tv.power()
    assert str(tv) == "# Power = [False], Channel = [0], Volume = [0]"


def test_power():
    # Test the power method when the TV is on
    tv = Television()
    tv.power()
    assert str(tv) == "# Power = [True], Channel = [0], Volume = [0]"

    # Test the power method when the TV is off
    tv.power()
    assert str(tv) == "# Power = [False], Channel = [0], Volume = [0]"

def test_mute():
    # Test muting and unmuting the TV
    tv = Television()

    tv.power()
    # Mute the TV
    tv.volume_up()
    tv.mute()
    assert str(tv) == "# Power = [True], Channel = [0], Volume = [1]"

    # Unmute the TV
    tv.mute()
    assert str(tv) == "# Power = [True], Channel = [0], Volume = [1]"

def test_channel_up():
    # Test channel up when the TV is off
    tv = Television()
    tv.channel_up()
    assert str(tv) == "# Power = [False], Channel = [0], Volume = [0]"

    # Test channel up when the TV is on
    tv.power()
    tv.channel_up()
    assert str(tv) == "# Power = [True], Channel = [1], Volume = [0]"
    # Test channel up beyond the maximum channel
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "# Power = [True], Channel = [3], Volume = [0]"

def test_channel_down():
    # Test channel down when the TV is off
    tv = Television()
    tv.channel_down()
    assert str(tv) == "# Power = [False], Channel = [0], Volume = [0]"

    # Test channel down when the TV is on
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == "# Power = [True], Channel = [2], Volume = [0]"

    # Test channel down beyond the minimum channel
    tv.channel_down()
    assert str(tv) == "# Power = [True], Channel = [1], Volume = [0]"

def test_volume_up():
    # Test volume up when TV is on
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "# Power = [True], Channel = [0], Volume = [1]"

    #Test volume up when TV is off
    tv.power()
    tv.volume_up()
    assert str(tv) == "# Power = [False], Channel = [0], Volume = [1]"

def test_volume_down():
    # Test volume down when TV is on
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "# Power = [True], Channel = [0], Volume = [1]"

    #Test volume down when TV is off
    tv.power()
    tv.volume_down()
    assert str(tv) == "# Power = [False], Channel = [0], Volume = [1]"
