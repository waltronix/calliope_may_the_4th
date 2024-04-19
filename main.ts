input.onPinTouchEvent(TouchPin.P1, input.buttonEventDown(), function () {
    basic.showString("hi!")
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    music.playMelody("C D E F G A B C5 ", 120)
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    music.setTempo(32)
    music.play(music.tonePlayable(220, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(220, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(220, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(175, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(220, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(175, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(220, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    basic.showLeds(`
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        . # . # .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        . . . . .
        # . # . #
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        # # # # #
        `)
    basic.showLeds(`
        # . # . #
        . # . # .
        # . # . #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        . # . # .
        `)
})
input.onPinTouchEvent(TouchPin.P0, input.buttonEventDown(), function () {
    music.playMelody("C5 B A G F E D C ", 120)
    music.playMelody("C D E F G A B C5 ", 120)
})
basic.forever(function () {
    basic.setLedColors(0x0000ff, 0x000000, 0x000000)
    basic.pause(500)
    basic.setLedColors(0x000000, 0x000000, 0x0000ff)
    basic.pause(500)
})
