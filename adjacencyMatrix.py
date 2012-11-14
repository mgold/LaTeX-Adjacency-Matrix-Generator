#!/usr/bin/python

from string import ascii_uppercase as uppercase
from sys import argv

# Number of rows/columns to have in the table. Must be <= 26.
N = 9

# String to place in each column of the table.
FILL = "   "

# You shouldn't have to touch anything below this line.
#######################################################


def endLine(startCol, n):
    return "\\\\ \cline{"+str(startCol)+"-"+str(n+2)+"}"

def main(n, fill, names = uppercase):
    assert 1 <= n <= len(names)
    assert len(fill) > 0

    print "\documentclass{article}"
    print "\usepackage{multirow}"
    print "\usepackage{rotating}"
    print "\\begin{document}"
    print

    print "\\begin{tabular}{|lr|l|l|l|l|l|l|l|l|l|} \cline{"+str(3)+"-"+str(n+2)+"}"
    print "\multicolumn{1}{l}{} && \multicolumn{"+str(n)+"}{c|}{To} "+endLine(3, n)

    print "\multicolumn{1}{l}{} &",
    for letter in names[:n]:
        print "& "+letter,
    print "\\\\ \hline"

    print "\multirow{"+str(n)+"}{*}{\\begin{sideways}From\end{sideways}}"
    print "%                         " + " "*((len(fill))//2),

    for letter in names[:n-1]:
        print letter+" "*(len(fill)-1),
    print letter

    body = ("&"+fill)*n

    for letter in names[:n-1]:
        print "& \multicolumn{1}{|r|}{"+letter+"} "+body+endLine(2, n)
    print "& \multicolumn{1}{|r|}{"+names[n-1]+"} "+body+"\\\\ \\hline"
    print "\end{tabular}"

    print
    print "\end{document}"

if __name__ == "__main__":
    argc = len(argv)
    if argc == 3:
        main(int(argv[1]), argv[2])
    elif argc == 2:
        main(int(argv[1]), "   ")
    else:
        main(N, FILL)
