# About: transposed a provided set of chords

import sys

keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# Transposed a single chord
def transpose_chord(chord, semi_tones):
    # only process the 1st letter of the chord, without parts such as m, add9 etc
    chord_key = chord[0]
    if(len(chord) > 1 and (chord[1] == "#" or chord[1] == "b")):
        chord_key = chord_key + chord[1]
    id_chord = keys.index(chord_key)
    id_transposed_chord_key = (id_chord + semi_tones) % len(keys)
    transposed_chord_key = keys[id_transposed_chord_key]
    transposed_chord = chord.replace(chord_key, transposed_chord_key)
    return transposed_chord

# Transpose a set of chords, separated by space
def transpose_chords(chords, semi_tones):
    transposed_chords = ''
    for chord in chords.split():
        transposed_chords = transposed_chords + ' ' + transpose_chord(chord, semi_tones)
    return transposed_chords.strip()

def test():
    c1 = transpose_chord('C', 2)
    assert(c1 == 'D')
    chords_transposed = transpose_chords("C Am G D", 2)
    assert(chords_transposed.strip() == "D Bm A E")

test()


# e.g., python3 transpose_chords.py  "C Am" 2
if (len(sys.argv) > 2):
    orig_chords = sys.argv[1]
    semi_tones = int(sys.argv[2])
    transposed_chords = transpose_chords(orig_chords, semi_tones)
    print(orig_chords + " -> ")
    print(transposed_chords)
