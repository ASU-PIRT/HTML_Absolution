import numpy as np
import matplotlib.pyplot as plt

from pyscript import document, display
from pyscript.web import page, when

## Temporary Message
message = "hello worl"
x = np.array([1,123])

# Temporary Graph for Testing
fig, ax = plt.subplots()
display(fig)

#for terminal
print(message)
print(x * 2)

#for page display
display(message)
display(x * 2)

## Create script that cleans html