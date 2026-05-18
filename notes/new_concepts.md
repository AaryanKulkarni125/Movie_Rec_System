# Key Concepts for this project 







* #### What vectorization means 
* #### CountVectorizer 
* #### Cosine similarity 
* #### Similarity matrix 
* #### Basic stemming 
* #### Python sorting with lambda



#### 

#### Here's what we're doing in vectorization:



We have a column called tags ,which is the combination of some other columns, and everything in that column is a string and an important phrase or keyword, so 

but the thing is for the machine to understand that text in a much better manner, we are converting it to numbers,

that's where vectorization comes in.

Here we need to create a vocabulary first. By creating a vocabulary ,what i mean is take in all the unique words from all the entries, and form a vocabulary that is the list of words we're aware of and then assign each word a position. The number of words is the number of dimensions our vector's gonna have. that is the number of spaces in it .

When a tag entry is interpreted by the machine ,using vectorization, it checks which words in the input match our vocabulary, the ones that match get a 1 in their index and the ones that don't get a 0. But that's for  binary vectorization, CountVectorization, counts the number of times a particular keyword has occurred in the tag and stores that value in that word's index .





#### Cosine\_Similarity and Similarity Matrix

Very simple shit 

It's just calculating the cos(theta) between two vectors.Because, it then acts as a measure of similarity, the value stays between -1 and 1 . One being perfect match, -1 being poles apart.

And the similarity matrix is a way to store this info between two or more vectors effectively .



#### Basic Stemming



What stemming does is it takes similar words like , actor ,acting, act and replaces them all with their root word "act" , this helps us improve our recommendation quality.



#### Python sorting with lambda

This sorting the movies based on their similarities, so that the one's with highest similarities pop up first .

