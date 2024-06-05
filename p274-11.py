import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki1 = wikipedia.page('South Korea')
wiki2 = wikipedia.page('Japan')
text = wiki1.content + wiki2.content

stopwords = set(STOPWORDS)
stopwords.update(['south', 'north', 'korean', 'world', 'country', 'japan', 'japanese'])

wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
