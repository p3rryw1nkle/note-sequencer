import random

def sequencer():
    notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
    sequence = []

    while len(notes) > 0:
        note = random.choice(notes)
        notes.remove(note)

        if "#" in note: # if note is a flat or a sharp, choose either flat or sharp variation
            note = note.split("/")
            note = random.choice(note)
            # if you want to append both variations (scambled), comment the first lne above and the following below
            # first = random.choice(note)
            # note.remove(first)
            # note.append(first)
            # note = "/".join(note)
        sequence.append(note)
    
    print("\n"*2 + "SEQUENCE:")
    print("\n".join(sequence) + "\n"*2)

sequencer()