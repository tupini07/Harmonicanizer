# Harmonicanizer

I'm learning to play the chomatic harmonica, and reading music sheets is not
hard but I've found it to be an unnecessarily long process to transcribe music
sheets to harmonica holes. So I wrote a program to do it for me!

How this program works is that you provide a file in _Harmonicanizer Notation_
and outputs chromatic harmonica notation. In the future the idea is to also
allow it to output diatonic harmonica notation as well.

Example usage:

```bash
python main.py convert-chromatic "songs/Legend of Zelda Medley.hcs"
```

## Harmonicanizer Notation

The idea is for you to easily be able to specify the notes. This format
completely ignore the rhythm information found in traditional music sheets. The
notation was made to make it as easy as possible  to symbolize where the note is
and if it has any modifiers (*sharp*, or *flat*).

You specify *where* the note is by saying which *line* or *blank* the note is
in. For example, `l1` is a note on the first line, so *Do/C*. `b1` is the note
on the first *blank*, so *Re/D*.

Modifiers for each note are specified by prepending to the note `#:` for sharp,
`@:` for flat, and `x:` to cancel global modifiers.

Global modifiers are modifiers that are applied to a certain note. For instance
specifying `#:l4` as global modifier will make it so that all `l4` in your input
sheet will get converted to `#:l4`. To cancel a global modifier, prepend `x:` to
the note: `x:l4` will be interpreted as a simple `l4` (no modifier).

This is probably all very confusing, so to make things simpler check
[schema.hcs](schema.hcs) which shows an example of how the notation is to be
used. If you want a more *real* example then check the files in [songs](songs).