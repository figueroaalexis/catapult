input.onButtonPressed(Button.A, function () {
    if (pins.digitalReadPin(DigitalPin.P2) > 0) {
        music.playTone(784, music.beat(BeatFraction.Eighth))
        basic.showNumber(1)
        music.playTone(784, music.beat(BeatFraction.Eighth))
        basic.showNumber(2)
        music.playTone(784, music.beat(BeatFraction.Half))
        basic.showNumber(3)
        pins.digitalWritePin(DigitalPin.P8, 1)
        armed = 0
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    if (pins.digitalReadPin(DigitalPin.P2) > 0) {
        pins.digitalWritePin(DigitalPin.P8, 1)
        armed = 0
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
let armed = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
armed = 0
basic.forever(function () {
    basic.pause(500)
    if (pins.digitalReadPin(DigitalPin.P2) > 0) {
        pins.digitalWritePin(DigitalPin.P8, 0)
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
        strip.show()
        if (armed < 1) {
            music.playTone(349, music.beat(BeatFraction.Eighth))
            armed = 1
            basic.showLeds(`
                . . # . .
                . . . . .
                # . # . #
                . . . . .
                . . # . .
                `)
        }
    } else {
        pins.digitalWritePin(DigitalPin.P8, 1)
        armed = 0
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
