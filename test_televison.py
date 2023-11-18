from television import *
import pytest 

def test_init():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0], Muted = [False]"
    tv.power()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0], Muted = [False]"


def test_power():
    # Test the power method when the TV is on
    tv = Television()
    tv.power()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0], Muted = [False]"

    # Test the power method when the TV is off
    tv.power()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0], Muted = [False]"

def test_mute():
    # Test muting and unmuting the TV
    tv = Television()
    

    # Mute the TV
    tv.mute()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0], Muted = [True]"

    # Unmute the TV
    tv.mute()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0], Muted = [False]"

def test_channel_up():
    # Test channel up when the TV is off
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0], Muted = [False]"

    # Test channel up when the TV is on
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = [True], Channel = [1], Volume = [0], Muted = [False]"
    # Test channel up beyond the maximum channel
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = [True], Channel = [3], Volume = [0], Muted = [False]"

def test_channel_down():
    # Test channel down when the TV is off
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0], Muted = [False]"

    # Test channel down when the TV is on
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == "Power = [True], Channel = [2], Volume = [0], Muted = [False]"

    # Test channel down beyond the minimum channel
    tv.channel_down()
    assert str(tv) == "Power = [True], Channel = [1], Volume = [0], Muted = [False]"

