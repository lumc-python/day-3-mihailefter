# Finding the most common 7-mer in a FASTA file
# =============================================
#
# Write a script to print out the most common 7-mer and its GC percentage from
# all the sequences in data/records.fa. You are free to reuse your existing
# toolbox.
#
# The example FASTA file was adapted from: Genome Biology DNA60 Bioinformatics
# Challenge.
#
# Hints:
# - FASTA files have two types of lines: header lines starting with a ">"
#   character and sequence lines. We are only concerned with the sequence line.
# - Read the string functions documentation.
# - Read the documentation for built in functions.
#
# Challenges:
# - Find out how to change your script so that it can read from
#   data/challenge.fa.gz without unzipping the file first.
# - Can you change the parser so that there is an option flag to tell the
#   program whether the input file is gzipped or not?
# - Can you change your script so that it works for any N-mers instead
#   of for just 7-mers?

import seq_toolbox
import argparse
import gzip


def most_common_nmer(file_path, file_type):
    # Dictionary with k-mer keys and their appearance number as values.
    nmer_dict = {}

    # Do the file type check.
    if file_type == 'text':
        open_any = open
    elif file_type == 'gzip':
        open_any = gzip.open

    # We open the file in the correct way.
    with open_any(file_path) as f:
        # Populate the nmer_dict.
        for line in f:
            # We sanitize the file line.
            seq = str(line).strip().upper()
            if not seq.startswith('>'):
                for i in range(len(seq) - 7 + 1):
                    nmer_seq = seq[i:i+7]
                    if nmer_seq in nmer_dict:
                        nmer_dict[nmer_seq] += 1
                    else:
                        nmer_dict[nmer_seq] = 1

    # The most common 7-mer is the nmer_dict key which has the maximum value.
    most_nmer = max(nmer_dict, key=nmer_dict.get)

    # Get the number of occurences.
    occurences = nmer_dict[most_nmer]

    # Get the GC percentage.
    gc = seq_toolbox.calc_gc_percent(most_nmer)

    return most_nmer, occurences, gc


if __name__ == '__main__':
    # Create our argument parser object.
    parser = argparse.ArgumentParser()
    # Add the expected file path argument.
    parser.add_argument('file_path', type=str,
                        help="Fasta input file path.")
    # Add the file type: gzip or textfile.
    parser.add_argument('file_type', type=str, choices=['text', 'gzip'],
                        help="Input file type.")
    # Do the actual argument parsing.
    args = parser.parse_args()

    # Printing the result.
    print("Most common 7-mer is '{}' (appears {} times) "
      "with a GC percentage of {:.2f}%.".format(
      *most_common_nmer(args.file_path, args.file_type)))
