# The python library for the isa68k-database project, by Sporniket

A library that can be included to process the files constituting the database of the "Motorola 68000" Instruction Set Architecture.

## Running a script

### db2html

A prototype that transform a file compatible with `Database - Integer instructions.tsv` into an html document.

**Invocation :**  `pdm run db2html [--output file] [source_files...]`

#### Typical invocation

_One should be in this script project folder_

Process given file `/path/to/mydb.tsv`:

```
pdm run db2html /path/to/mydb.tsv
```

Process standard input

```
...something that outputs TSV lines... | pdm run db2html
```
