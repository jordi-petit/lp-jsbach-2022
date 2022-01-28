import random

notes = "cdefgab"


def fibo(n):
    print(notes[n]+"'4")
    if n > 1:
        fibo(n-1)
        fibo(n-2)


def main():
    fibo(6)


if 1:
    print("""
    \\version "2.22.1"
    \\score {
    \\absolute {
    \\tempo 4 = 180
    \key c \major
    """)
    main()
    print("""
    }
    \\layout { }
    \\midi { }
    }
    """)
else:
    main()
