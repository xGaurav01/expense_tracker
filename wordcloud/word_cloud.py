from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('data.txt','r') as file:
    text = file.read()

wordcloud = WordCloud(width=800,height=400,background_color='white').generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation='bilinear')
plt.title("Wordcloud from data.txt")
plt.axis('off')
plt.show()
