from television import Television
import pytest 

def test_init():
    tv = Television()
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_power():
    # Test the power method when the TV is off
    tv = Television()
    tv.power()
    assert tv._status is True

    # Test the power method when the TV is on
    tv.power()
    assert tv._status is False

def test_mute():
    # Test muting and unmuting the TV
    tv = Television()

    # Mute the TV
    tv.mute()
    assert tv._muted is True

    # Unmute the TV
    tv.mute()
    assert tv._muted is False

def test_channel_up():
    # Test channel up when the TV is off
    tv = Television()
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL

    # Test channel up when the TV is on
    tv.power()
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL + 1

    # Test channel up beyond the maximum channel
    for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
        tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL

def test_channel_down():
    # Test channel down when the TV is off
    tv = Television()
    tv.channel_down()
    assert tv._channel == Television.MIN_CHANNEL

    # Test channel down when the TV is on
    tv.power()
    tv.channel_down()
    assert tv._channel == Television.MIN_CHANNEL - 1

    # Test channel down beyond the minimum channel
    for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
        tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL

