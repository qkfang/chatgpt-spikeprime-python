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
