from app import bargraph
bargraph.change(color: int, value: float) -> None
bargraph.clear_all() -> None
bargraph.get_value(color: int) -> Awaitable
bargraph.hide() -> None
bargraph.set_value(color: int, value: float) -> None
bargraph.show(fullscreen: bool) -> None


from app import display
display.hide() -> None
display.image(image: int) -> None
display.show(fullscreen: bool) -> None
display.text(text: str) -> None
app.display Constants # IMAGE_ROBOT_1 = 1 IMAGE_ROBOT_2 = 2 IMAGE_ROBOT_3 = 3 IMAGE_ROBOT_4 = 4 IMAGE_ROBOT_5 = 5 IMAGE_HUB_1 = 6 IMAGE_HUB_2 = 7 IMAGE_HUB_3 = 8 IMAGE_HUB_4 = 9 IMAGE_AMUSEMENT_PARK = 10 IMAGE_BEACH = 11 IMAGE_HAUNTED_HOUSE = 12 IMAGE_CARNIVAL = 13 IMAGE_BOOKSHELF = 14 IMAGE_PLAYGROUND = 15 IMAGE_MOON = 16 IMAGE_CAVE = 17 IMAGE_OCEAN = 18 IMAGE_POLAR_BEAR = 19 IMAGE_PARK = 20 IMAGE_RANDOM = 21


from app import music
music.play_drum(drum: int) -> None
music.play_instrument(instrument: int, note: int, duration: int) -> None
app.music Constants # DRUM_BASS = 2 DRUM_BONGO = 13 DRUM_CABASA = 15 DRUM_CLAVES = 9 DRUM_CLOSED_HI_HAT = 6 DRUM_CONGA = 14 DRUM_COWBELL = 11 DRUM_CRASH_CYMBAL = 4 DRUM_CUICA = 18 DRUM_GUIRO = 16 DRUM_HAND_CLAP = 8 DRUM_OPEN_HI_HAT = 5 DRUM_SIDE_STICK = 3 DRUM_SNARE = 1 DRUM_TAMBOURINE = 7 DRUM_TRIANGLE = 12 DRUM_VIBRASLAP = 17 DRUM_WOOD_BLOCK = 10 INSTRUMENT_BASS = 6 INSTRUMENT_BASSOON = 14 INSTRUMENT_CELLO = 8 INSTRUMENT_CHOIR = 15 INSTRUMENT_CLARINET = 10 INSTRUMENT_ELECTRIC_GUITAR = 5 INSTRUMENT_ELECTRIC_PIANO = 2 INSTRUMENT_FLUTE = 12 INSTRUMENT_GUITAR = 4 INSTRUMENT_MARIMBA = 19 INSTRUMENT_MUSIC_BOX = 17 INSTRUMENT_ORGAN = 3 INSTRUMENT_PIANO = 1 INSTRUMENT_PIZZICATO = 7 INSTRUMENT_SAXOPHONE = 11 INSTRUMENT_STEEL_DRUM = 18 INSTRUMENT_SYNTH_LEAD = 20 INSTRUMENT_SYNTH_PAD = 21 INSTRUMENT_TROMBONE = 9 INSTRUMENT_VIBRAPHONE = 16 INSTRUMENT_WOODEN_FLUTE = 13


from app import sound
sound.play(sound_name: str, volume: int = 100, pitch: int = 0, pan: int = 0) -> Awaitable # Play a sound in the SPIKE App
sound.set_attributes(volume: int, pitch: int, pan: int) -> None
sound.stop() -> None




import color
color Constants # BLACK = 0 MAGENTA = 1 PURPLE = 2 BLUE = 3 AZURE = 4 TURQUOISE = 5 GREEN = 6 YELLOW = 7 ORANGE = 8 RED = 9 WHITE = 10 UNKNOWN = -1


import color_matrix
color_matrix.clear(port: int) -> None # Turn off all pixels on a Color Matrix
color_matrix.get_pixel(port: int, x: int, y: int) -> tuple[int, int] # Retrieve a specific pixel represented as a tuple containing the color and intensity
color_matrix.set_pixel(port: int, x: int, y: int, pixel: tuple[color: int, intensity: int]) -> None # Change a single pixel on a Color Matrix
color_matrix.show(port: int, pixels: list[tuple[int, int]]) -> None # Change all pixels at once on a Color Matrix


import color_sensor
color_sensor.color(port: int) -> int # Returns the color value of the detected color. Use the color module to map the color value to a specific color.
color_sensor.reflection(port: int) -> int # Retrieves the intensity of the reflected light (0-100%).
color_sensor.rgbi(port: int) -> tuple[int, int, int, int] # Retrieve the raw LPF-2 data from a device.


import device
device.data(port: int) -> tuple[int] # Retrieve the raw LPF-2 data from a device.
device.id(port: int) -> int # Retrieve the device id of a device. Each device has an id based on its type.
device.get_duty_cycle(port: int) -> int # Retrieve the duty cycle for a device. Returned values is in range 0 to 10000
device.ready(port: int) -> bool # When a device is attached to the hub it might take a short amount of time before it's ready to accept requests. Use ready to test for the readiness of the attached devices.
device.set_duty_cycle(port: int, duty_cycle: int) -> None # Set the duty cycle on a device. Range 0 to 10000


import distance_sensor
distance_sensor.clear(port: int) -> None # Turns off all the lights in the Distance Sensor connected to port.
distance_sensor.distance(port: int) -> int # Retrieve the distance in millimeters captured by the Distance Sensor connected to port. If the Distance Sensor cannot read a valid distance it will return -1.
distance_sensor.get_pixel(port: int, x: int, y: int) -> int # Retrieve the intensity of a specific light on the Distance Sensor connected to port.
distance_sensor.set_pixel(port: int, x: int, y: int, intensity: int) -> None # Changes the intensity of a specific light on the Distance Sensor connected to port.


import force_sensor
force_sensor.show(port: int, pixels: list[int]) -> None # Change all the lights at the same time.
force_sensor.force(port: int) -> int # Retrieves the measured force as decinewton. Values range from 0 to 100
force_sensor.pressed(port: int) -> bool # Tests whether the button on the sensor is pressed. Returns true if the force sensor connected to port is pressed.
force_sensor.raw(port: int) -> int # Returns the raw, uncalibrated force value of the force sensor connected on port port


from hub import button
int button.pressed(button: int) -> int # This module allows you to react to buttons being pressed on the hub. You must first import the  button module to use the buttons.
hub.button Constants # LEFT\u00a0= 1 Left button next to the power button on the SPIKE Prime  hub RIGHT\u00a0= 2 Right button next to the power button on the SPIKE  Prime hub
 

from hub import light
light.color(light: int, color: int) -> None # Change the color of a light on the hub.
hub.light Constants # POWER = 0 The power button. On SPIKE Prime it's the button between the left  and right buttons. CONNECT = 1 The light around the Bluetooth connect  button on SPIKE Prime.
