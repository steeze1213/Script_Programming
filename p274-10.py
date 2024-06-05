import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki = wikipedia.page('South Korea')
text = wiki.content

s_words = STOPWORDS.union({'south', 'north', 'korean', 'world', 'country'})

wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words).generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
