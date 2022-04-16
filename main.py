def on_button_pressed_a():
    global armed
    if pins.digital_read_pin(DigitalPin.P2) > 0:
        music.play_tone(784, music.beat(BeatFraction.EIGHTH))
        basic.show_number(1)
        music.play_tone(784, music.beat(BeatFraction.EIGHTH))
        basic.show_number(2)
        music.play_tone(784, music.beat(BeatFraction.HALF))
        basic.show_number(3)
        pins.digital_write_pin(DigitalPin.P8, 1)
        armed = 0
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
        strip.show()
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global armed
    if pins.digital_read_pin(DigitalPin.P2) > 0:
        pins.digital_write_pin(DigitalPin.P8, 1)
        armed = 0
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
        strip.show()
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

armed = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
armed = 0

def on_forever():
    global armed
    basic.pause(500)
    if pins.digital_read_pin(DigitalPin.P2) > 0:
        pins.digital_write_pin(DigitalPin.P8, 0)
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        if armed < 1:
            music.play_tone(349, music.beat(BeatFraction.EIGHTH))
            armed = 1
            basic.show_leds("""
                . . # . .
                                . . . . .
                                # . # . #
                                . . . . .
                                . . # . .
            """)
    else:
        pins.digital_write_pin(DigitalPin.P8, 1)
        armed = 0
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
        strip.show()
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
