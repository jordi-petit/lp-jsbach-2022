python3 hanoi.py > hanoi.lily
lilypond hanoi.lily
timidity -Ow -o hanoi.wav hanoi.midi
open hanoi.pdf
rm hanoi.mp3
ffmpeg -i hanoi.wav -codec:a libmp3lame -qscale:a 2 hanoi.mp3
afplay hanoi.mp3
