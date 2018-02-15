# longest-path-in-graph
April 18, 2015

Finding the longest path in a graph built on edit distance between words.

Edit Ladder: Given a sequence of words w1, w2, … wn, two words u and v are neighbours if they have edit distance 1. We orient these edges in dictionary order. This defines a directed graph. We then find the longest path in this graph.  

To run the code, run the file "longest_path.py" with the input file as second argument. If no input file is given, a default testcase file is taken.
