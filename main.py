from music21 import converter
from music21 import configure

# Load a MusicXML file
score = converter.parse('sample.xml')

# You can access the parts in the score like this
for part in score.parts:
    print(part.id)

# And you can access the notes in each part like this
for note in part.flat.notes:
    print(note, note.offset)



#configure.run()



score.show()
