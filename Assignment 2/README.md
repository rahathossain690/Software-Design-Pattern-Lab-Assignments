# Assignment 1
Python code for assignment 2. This code uses strategy design pattern.

# Installing
1. Install python and pip.
2. Install packages from requirement.
```
pip install -r requirements.txt
```
3. Run 
```
python SentenceGenerator_32.py
```

# Problem description
Sentence Generator is a program that generates sentences using English words. All sentence
generators have an internal vocabulary (one vocabulary for each sentence generator), which is
initially empty and can be updated by adding some words. All sentence generators are able to
generate sentences according to some rules. You have to implements following three types of
sentence generators:
1. Random Sentence Generator - RSG
When a word is added to RSG, before storing it in internal vocabulary, the word is
converted to lowercase. RSG generates new sentences by randomly picking random
amount of words from its internal vocabulary and concatenating them using single space
between the words.
2. Sorted Sentence Generator - SSG
Before adding a word into its internal vocabulary, SSG also converts the word to
lowercase. Like RSG, SSG picks up the words randomly. The only difference is that it
sorts these words before the concatenation.
3. Ordered Sentence Generator - OSG
OSG is different from both RSG and SSG. A word, before adding into internal
vocabulary, will be converted to upper case and reversed. OSG concatenates all of the
words in the same order they have been added to the vocabulary.

Finally, after creating these sentence generators you have to create a sentence generator
application(console/gui/etc), in which user can choose a particular sentence generator from a
menu to create a sentence. Moreover, using the same menu user can also give input to add new
words in the vocabulary.

# File Structure
1. SentenceGenerator_32.py: Python console application
2. ClassDiagram_32.png
3. ClassDiagram_32_no.png: This should not be submitted
4. TaskTwo.zargo: argoUML file
5. SDP_Assignment_TaskTwo_32.docx: Project assumption