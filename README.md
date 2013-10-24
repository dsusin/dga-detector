dga-detector
============
Original Jaccard algorithm by Gokul Das (study-jaccard-shingling) licensed under the BSD 3-clause license.

Copyright (c) 2012, Gokul Das
All rights reserved.

Modified by Daniel Susín.
Modified to run with Python 2.7.
Algorithm applied to the detection of DGA generated domains.

usage: python jaccard.py [2nd_level_domain]. Ex: "python jaccard.py gloooogle" "python jaccard.py myrahlakboegc"

Original readme:
===============

study-jaccard-shingling
===============

An accademic implementation of Jaccard shingling algorithm. Written in Python 3. The aim is to identify a similar word from a text corpus to a given input word. The text to prepare the corpus is given in one of the source files. For more info, refer:

http://matpalm.com/resemblance/jaccard_coeff/

http://nlp.stanford.edu/IR-book/html/htmledition/near-duplicates-and-shingling-1.html

Algorithm
---------

The body of text is first tokenised into a list of words. Then each word is send through a shingler function to identify its character bigram shingles. For example, 'process' would have shingles 'pr', 'ro', 'oc', 'ce', 'es' and 'ss'. Then, once the user enters a word, the same process is done to identify the set of its bigram shingles. The input bigrams are then compared to bigrams of each of the corpus words, and a jaccard index is prepared to signify their similarity. The final index is sorted to identify the most similar 3 words in the corpus and is displayed.  

jaccard.py
-----------
This file contains the implementation of the algorithm. Its functions are as follows:

### bigram_shingler(str)
The function that does the shingling to extract the bigram set for a single word.

### jacc_ind(bigrams1, bigrams2):
The function to calculates the jaccard index for 2 words, given the bigram sets for the words.

LICENSE
-------
This project is licensed under the BSD 3-clause license. Refer LICENSE file for details.
