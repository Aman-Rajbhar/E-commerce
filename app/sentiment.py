import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
# from nltk.corpus import wordnet as WordNetLemmatizer

# from django.shortcuts import render
# text = "One bad review or ten doesn mean  'exhausted hopeless': 'powerless', exhilarated happyexploited cheatedexposed fearfulfabulous ecstatic it the end of the world though. Your online reputation can be defended with your review responses and your other positive reviews"
text = open('data.txt').read()


lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Using word_tokenize because it's faster than split()
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)


emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)





class senti(object):
    def sentiment_analyse(self, sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        if score['neg'] < score['pos']:
            pos = "Satisfied"
            context = {'sentiment_result': pos}
            print(pos) 
        elif score['neg'] > score['pos']:
            neg = "Unsatisfied"
            context = {'sentiment_result': neg}
            print(neg)
        else:
            neut = "Neutral"
            context = {'sentiment_result': neut}
        
        return context
   
        

    
# print(w.keys())
# print(w.values())
    
def generate_plot():
    fig, ax = plt.subplots()
    ax.bar(w.keys(), w.values())
    # fig.autofmt_xdate() 
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_title('My Plot')
    # plt.savefig('static/graph.png')
    return 'graph.png'





# def generate_plot():
#     # create the plot
#     fig, ax1 = plt.subplots()
#     ax1.bar(w.keys(), w.values())
#     fig.autofmt_xdate()
    
#     ax1.set_xlabel('X Label')
#     ax1.set_ylabel('Y Label')
#     ax1.set_title('My Plot')
#     # save the plot as a static file
#     plt.savefig('static/my_plot.png')

#     # return the path to the static file
#     return 'my_plot.png'

    # # save the plot as a static file
    # plt.savefig('static/graph.png')
    # # return the path to the static file
    # return 'graph.png'


    




