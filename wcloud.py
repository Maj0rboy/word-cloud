import wordcloud as wc
import wikipedia
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys

# ......read the text and saved it into a variable
# text = ""
# with open('word.txt', encoding='utf-8') as f:
#     text = " ".join(f.readlines())
    
# ...reading the input from a wikipedia page
x = str(input('enter a title:'))
title = wikipedia.search(x)[0]
page = wikipedia.page(title)
text = page.content
    
def calculate_frequencies(text):
    # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    # ,,,,a function to go through the text and remove uninteresting words
    file_contents = ''
    for index, char in enumerate(text):
        if char.isalpha() == True or char.isspace():
            file_contents += char
        
    file_contents = text.split()
    file_without_uninteresting_words = []
    
    for word in file_contents:
        if word.lower() not in uninteresting_words and word.isalpha() == True:
            file_without_uninteresting_words.append(word)
# ,,,,,calculate the number a times a word appears in the text
    frequency = {}
    for word in file_without_uninteresting_words:
        if word.lower() not in frequency:
            frequency[word.lower()] = 1
        else:
            frequency[word.lower()] += 1
    cloud = wc.WordCloud(max_font_size=100,width=600, height=400,background_color='black')
    cloud.generate_from_frequencies(frequency)
    return cloud.to_array()
# ,,,,,displaying the image
myimage = calculate_frequencies(text)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()

            
    