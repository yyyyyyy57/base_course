import random

flowers = ['rose', 'dandelion', 'chamomile', 'tulip']
colors = ['red', 'yellow', 'white', 'pink', 'blue', 'purple']

bouquet = dict(zip(flowers, [random.choice(colors) for i in flowers]))
print(bouquet)