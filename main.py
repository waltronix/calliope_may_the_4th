def on_pin_touch_p1():
    basic.show_string("hi!")
input.on_pin_touch_event(TouchPin.P1, input.button_event_down(), on_pin_touch_p1)

def on_logo_touched():
    music.play_melody("C D E F G A B C5 ", 120)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_a():
    music.set_tempo(32)
    music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(175, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(175, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(220, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    basic.show_leds("""
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        . # . # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # #
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # . # .
        # . # . #
        . # . # .
        . . . . .
        # . # . #
        """)
    basic.show_leds("""
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        # # # # #
        """)
    basic.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        # # # # #
        # # # # #
        """)
    basic.show_leds("""
        . # . # .
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.show_leds("""
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        . # . # .
        """)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_pin_touch_p0():
    music.play_melody("C5 B A G F E D C ", 120)
    music.play_melody("C D E F G A B C5 ", 120)
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

def on_forever():
    basic.set_led_colors(0x0000ff, 0x000000, 0x000000)
    basic.pause(500)
    basic.set_led_colors(0x000000, 0x000000, 0x0000ff)
    basic.pause(500)
basic.forever(on_forever)
