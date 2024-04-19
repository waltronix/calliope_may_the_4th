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
    music.play(music.string_playable("A - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(10)
    music.play(music.string_playable("A - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(10)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_forever():
    basic.set_led_colors(0x0000ff, 0x000000, 0x000000)
    basic.pause(500)
    basic.set_led_colors(0x000000, 0x000000, 0x0000ff)
    basic.pause(500)
basic.forever(on_forever)
