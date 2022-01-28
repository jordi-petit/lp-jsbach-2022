python3 selsort.py > selsort.lily
lilypond selsort.lily
timidity -Ow -o selsort.wav selsort.midi
open selsort.pdf
rm selsort.mp3
ffmpeg -i selsort.wav -codec:a libmp3lame -qscale:a 2 selsort.mp3
afplay selsort.mp3
