import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 100, 500)
plt.plot(n, np.log(n))
# plt.show()

laptop = {}

laptop["owner"] = "Bryan"
laptop["make"] = "Dell"

print(laptop)