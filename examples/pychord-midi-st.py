# An example to create MIDI file with PyChord and pretty_midi
# Prerequisite: pip install pretty_midi
# pretty_midi: https://github.com/craffel/pretty-midi


import pretty_midi
import sys

from pychord import Chord


def create_midi(chords):
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            piano.notes.append(note)
    midi_data.instruments.append(piano)
    midi_data.write('chord.mid')

def create_midi_vary_time(chords, lengths):
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    current_position = 0
    for n, chord in enumerate(chords):
        #print ("n:", n)
        length = lengths[n]
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=current_position, end=current_position + lengths[n])
            piano.notes.append(note)
        current_position = current_position + lengths[n]
    midi_data.instruments.append(piano)
    midi_data.write('chord.mid')

# input format example: "C:1 Dm7:.5 G:.5 C:1"
def parse_chords_barlen(chords_n_bars):
    split_pairs = chords_n_bars.split()
    chords = []
    lengths = []
    for chord_n_bar in split_pairs:
        c = chord_n_bar.split(":")[0]
        b = chord_n_bar.split(":")[1]
        chords.append(c)
        lengths.append(float(b))
    return chords, lengths

def test_main():
    chords_str = ["C", "Dm7", "G", "C"]
    lengths = [1, 1.5, 0.5, 1]
    chords = [Chord(c) for c in chords_str]
    for c in chords_str:
        print (Chord(c))

    create_midi_vary_time(chords, lengths)

def test_chords_n_bars_main():
    #chords_str = ["C", "Dm7", "G", "C"]
    #lengths = [1, 1.5, 0.5, 1]
    chords_n_bars = "C:0.5 Dm7:.5 G:.5 C:1"
    chords_str, lengths = parse_chords_barlen(chords_n_bars)
    print(chords_str)
    print(lengths)
    #return#

    chords = [Chord(c) for c in chords_str]
    for c in chords_str:
        print (Chord(c))

    create_midi_vary_time(chords, lengths)

def read_args():
    user_inputs = ''
    if (len(sys.argv)>0):
        user_inputs = sys.argv[1]
    return user_inputs

def main():
    chords_n_bars = read_args()
    if (chords_n_bars == ''):
        print('No input provided, pass e.g., "C:0.5 Dm7:.5 G:.5 C:1"')
    chords_str, lengths = parse_chords_barlen(chords_n_bars)
    print(chords_str)
    print(lengths)

    chords = [Chord(c) for c in chords_str]
    for c in chords_str:
        print (Chord(c))

    create_midi_vary_time(chords, lengths)
    

if __name__ == '__main__':
    main()
    #test_main()
    
