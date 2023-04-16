# Capo @ 2
# key D
# Chords w/ Capo: C Am F C; I vi IV I, w/o Capo: D Bm G D
# Chords @ Chorus w/ Capo:F C A# F, w/o Capo: G D C G
intro="Ab:1|Ab:1"
# these are v1 v2 and v3
V1_rep_a="Ab:2|Ab:.5|Db:2|Eb:2|Ab:2"
V1_rep_b="Ab:2|Ab:.5|Db:2|Eb:2|Ab:2"
V1_rep_c="Ab:1|Db:2|Eb7:1|Ab:2"
# TODO: for later section, include the planned variations such as Am, D7
V1=${V1_rep_a}"|"${V1_rep_a}"|"${V1_rep_b}"|"${V1_rep_b}"|"${V1_rep_c}"|"${V1_rep_c}

# TODO: review
int1_a="Ab:2|Db:2|Ab:2"
int1_b="A#m:2|Fm:2|F#:2|Db5:2"
int1_c="A#m:2|Fm:2|F#:2"
int1_d="G#:2"
int1=${int1_a}"|"${int1_b}"|"${int1_c}"|"${int1_d}
V4="F#:2|G#:2|F#:2|G#:2|D#7:2|G#:1"
TA_a="G#:.5|D#:.5|C#add9:.5|G#:.5"  #turnaround
TA_b="G#sus2:.25|G#sus2:.25|G#sus2:.25|G#sus2:.25|G#sus2:.25|G#sus2:.25|G#sus2:.25|G#sus2:.25"
TA=${TA_a}"|"${TA_b}
V5_a="Ab:2|Ab:.5|Db:2|Eb:2|Ab:2"  #outro
V5_b="Ab:2|Ab:.5|Db:2|Eb:1.5|Ab:2"
V5_c="Bb:2|Bb:.5|Eb:2|F:1.5|Bb:2"
V5=${V5_a}"|"${V5_b}"|"${V5_c}

Chorus="G:2|G:2|D:2|D:2|C:1|C:2|C:2|D:2|D:2"
song="ke_vayo"
chords_to_midi $intro ${song}-intro.mid
chords_to_midi $V1 ${song}-v1.mid
chords_to_midi $int1 ${song}-int1.mid
chords_to_midi $V4 ${song}-v4.mid
chords_to_midi $TA ${song}-ta.mid
chords_to_midi $V5 ${song}-V5.mid

#chords_to_midi $Chorus ${song}-chorus.mid

