import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/plot-chart")
def plot_iris():
  plt.style.use('_mpl-gallery')
  # make data
  x = np.linspace(0, 10, 100)
  y = 4 + 2 * np.sin(2 * x)
  # plot
  fig, ax = plt.subplots()

  ax.plot(x, y, linewidth=2.0)

  ax.set(xlim=(0, 9), xticks=np.arange(1, 8),
  ylim=(0, 8), yticks=np.arange(1, 8))
 
  plt.savefig('iris.png')
  file = open('iris.png', mode="rb")
  return StreamingResponse(file, media_type="image/png")

@app.get("/plot-bar")
def plot_bar(column:str,label:str,value:str,ylabel:str):
  fig, ax = plt.subplots()
  fruits = column.split(",")
  counts = value.split(",");
  counts = [eval(i) for i in counts]
  bar_labels = label.split(",")
  bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:pink']

  ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

  ax.set_ylabel(ylabel)
  ax.set_title('Fruit supply by kind and color')
  ax.legend(title='Fruit color')
  plt.savefig('iris.png')
  file = open('iris.png', mode="rb")
  return StreamingResponse(file, media_type="image/png")

@app.get("/plot-multipleChart")
def plot_iris():
       species = ("Adelie", "Chinstrap", "Gentoo")
       penguin_means = {
       'Bill Depth': (18.35, 18.43, 14.98),
       'Bill Length': (38.79, 48.83, 47.50),
       'Flipper Length': (189.95, 195.82, 217.19),
       }

       x = np.arange(len(species))  # the label locations
       width = 0.25  # the width of the bars
       multiplier = 0

       fig, ax = plt.subplots(layout='constrained')

       for attribute, measurement in penguin_means.items():
              offset = width * multiplier
              rects = ax.bar(x + offset, measurement, width, label=attribute)
              ax.bar_label(rects, padding=3)
              multiplier += 1

       # Add some text for labels, title and custom x-axis tick labels, etc.
       ax.set_ylabel('Length (mm)')
       ax.set_title('Penguin attributes by species')
       ax.set_xticks(x + width, species)
       ax.legend(loc='upper left', ncols=3)
       ax.set_ylim(0, 250)
       plt.savefig('iris.png')
       file = open('iris.png', mode="rb")
       return StreamingResponse(file, media_type="image/png")

