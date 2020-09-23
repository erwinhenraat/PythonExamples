import random

original = "hallo"
randomised = ''.join(random.sample(original, len(original)))
print(randomised)
