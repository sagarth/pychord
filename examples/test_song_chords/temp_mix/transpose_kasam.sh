add_semi_tones=3  # capo locaiton
transpose_script=/root/ktmmusiclab/tools/chord_generators/chords_transposer/transpose_chords.py

python3 $transpose_script "G G" 3
python3 $transpose_script "G Cadd9" 3
python3 $transpose_script "Cadd9 G" 3
