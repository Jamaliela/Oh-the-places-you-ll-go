######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Change this to your names
# Username: lovelle & heggens             TODO: Change this to your usernames
#
# Assignment: T10: Oh, the Places You'll Go!
#
# Purpose: This program is designed to open an input file called "io_input.txt",
#   copy the contents into a list of strings (a string per line in the input file),
#   and writes the list contents in reverse order into an output file.
#
#   For example, suppose the input file io_input.txt has the following:
#
#       Hello, my
#       name is Jack.
#
#   The output file would have:
#
#       name is Jack.
#       Hello, my
#
# Be sure to put the input file into the same folder as the program.
#
######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Mario Nakazawa and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


def read_file_contents(filenm):
    """
    Opens the input file, stores all the text into a tuple of strings,
    one normal order and one reverse order.
    Closes the file and returns the contents

    :param filenm: A string representing the name of the input file
    :return: A tuple with the input string and the reversed string
    """
    in_str = ""
    reverse_str = ""

    open_file = open(filenm, "r")               # use io_input.txt
    next_line = open_file.readline()            # reads the first line

    while(len(next_line) > 0):                  # while there is something to read
        in_str = in_str + next_line             # concatenates the string to the normal end
        reverse_str = next_line + reverse_str   # concatenates backwards
        next_line = open_file.readline()        # reads the next line
    open_file.close()
    print("{0} file read.".format(filenm))

    return (in_str, reverse_str)                # returns a tuple


def write_file_reverse(out_str ,outfile):
    """
    Creates a file, opens it, and outputs the list of
    strings in out_str out in reverse order. At the end, closes the file.

    :param out_str: the string to be written
    :param outfile: the file to write to
    :return: None
    """
    open_file = open(outfile, "w")
    open_file.write(out_str)                  # writes out the entire string
    open_file.close()

    print("{0} file written.".format(outfile))


# main program
def main():
    """
    The main function, which asks the user for the input file name, the output file name,
    and writes the string in the input file to the output file, in reverse order

    :return: None
    """
    in_filename = input("What is the input filename (default is 'io_input.txt')? ")

    if in_filename == "":
        in_filename = "io_input.txt"            # use io_input.txt if no filename entered

    (input_string, rev_string) = read_file_contents(in_filename)

    print("\nHere is the file in the normal order:\n")
    print(input_string)

    out_filename = input("What do you want the output filename to be (default is 'io_output.txt')? ")

    if out_filename == "":
        out_filename = "io_output.txt"              # use io_output.txt if no filename entered
    write_file_reverse(rev_string, out_filename)    # creates output file

    print("\nHere is the file in the reverse order:\n")
    print(rev_string)


if __name__ == "__main__":
    main()
