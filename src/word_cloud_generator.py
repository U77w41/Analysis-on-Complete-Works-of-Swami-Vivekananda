from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pathlib import Path
from processtext import clean,remove_sw
# Getting the parent directory path
PATH = str(Path.cwd())

# Reading the data
with open(PATH+"/data/raw/Complete Works of Swami Vivekananda -  All Volumes - Swami Vivekananda.txt") as f:
    data = f.read()

# Doing the basic preprocessing using the precesstext library
data = clean(data)
data = remove_sw(data)

# Generating the Swami Vivekananda mask using the png file
mask_path = PATH + "/etc/Swami-Vivekananda.png"
mask = np.array(Image.open(mask_path)) if mask_path else None

# Setting up the colors taking oranges, yellow, brown and black color tones
colors = ["#b54605","#e65907", "#6e3515", "#f28305", "#080503", '#734002' , "#730202", "#f70202", "#bf6011", "#000000"]

# Creating the wordcloud
wordcloud = WordCloud(max_font_size=60,
                      max_words=36000,
                      background_color="white",
                      colormap=plt.cm.colors.ListedColormap(colors),
                      collocations= True,
                      prefer_horizontal=0.5,
                      mask= mask).generate(data)

# Creating the word cloud
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig(PATH+'/etc/swami-ji.svg', format='svg', dpi=200)