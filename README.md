# Finding the most common 7-mer in a FASTA file

## Your task

Write a script to print out the most common 7-mer and its GC percentage from all
the sequences in `data/records.fa`. You are free to reuse your existing toolbox.

- The example FASTA file was adapted from: Genome Biology DNA60 Bioinformatics
  Challenge.

## Hints

- FASTA files have two types of lines: header lines starting with a ">"
character and sequence lines. We are only concerned with the sequence line.
- Read the [string functions documentation](https://docs.python.org/3/library/string.html).
- Read the [documentation for built in functions](https://docs.python.org/3/library/functions.html).
- [Parse command line arguments](https://docs.python.org/3/howto/argparse.html)

## Challenges

- Find out how to change your script so that it can read from
  `data/challenge.fa.gz` without unzipping the file first (hint: check standard
  library).
- Can you change the parser so that there is an option flag to tell the
  program whether the input file is gzipped or not?
- Can you change your script so that it works for any N-mers instead of for
  just 7-mers?
