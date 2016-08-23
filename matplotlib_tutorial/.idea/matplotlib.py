import numpy as np

X = np.linspace(-np.pi , np.pi, 256, endpoint=True)

C,S = np.cos(X), np.sin(X)
import matplotlib.pyplot as plt
plt.plot(C)

