import random


def main():
    v = ["c", "d", "e", "f", "g", "a", "b"]
    random.shuffle(v)
    # print(v)
    n = len(v)
    for i in range(n):
        p = i
        for j in range(i, n):
            print(v[i]+"'4")
            print(v[j]+"'4")
            if v[j] < v[p]:
                p = j
        v[p], v[i] = v[i], v[p]
        print(v[p]+"'2")
    # print(v)


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
    c'1
    }
    \\layout { }
    \\midi { }
    }
    """)
else:
    main()
