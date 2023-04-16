# Capo @ 2
# key D
# Chords w/ Capo: C Am F C; I vi IV I, w/o Capo: D Bm G D
# Chords @ Chorus w/ Capo:F C A# F, w/o Capo: G D C G
intro="D:2|Bm:2|G:2|D:2"
V1="D:2|D:2|Bm:2|Bm:2|G:2|D:2|D:2"
Chorus="G:2|G:2|D:2|D:2|C:1|C:2|C:2|D:2|D:2"
V3="C#:4|A#m:4|F#:2|C#:4""|C#:4|A#m:4|G#:2|C#:4""|C#:4|A#m:4|F:2|C#:4"
echo $V3
#chords_to_midi $intro kehi_shabda-intro.mid
#chords_to_midi $V1 kehi_shabda-v1.mid
#chords_to_midi $Chorus kehi_shabda-chorus.mid
chords_to_midi $V3 kehi_shabda-v3.mid

