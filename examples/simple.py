import numpy as np
import columnplots as clp

# turn this parameter to false if LaTeX is not installed
if_latex=True

# prepare x data for plotting
x = np.linspace(0, 10, 10)

# prepare y data for plotting
y = (x**2 - x + 3)*1e4

# prepare input values for scientific plotting
xs = [x]*2
ys = [y]*2
colors = ["ko", "r--"]
labels = ["$y_1$", "$y_2$"]

# do plotting

# 1. Initialize a 2x2 figure
axes = clp.initialize(col=2, row=2,
               width=8.6, height=8.6*0.618,
               LaTeX=if_latex,
               labelthem=True, labelthemPosition=[0.1, 0.95],
               fontsize=12)

# 2. Plot at each figure
clp.plotone(xs, ys, axes[0,0], labels=labels, colors=colors, lw=1,
            ylabel="$y$ value",
            yscientificAtLabel=True)

clp.plotone(xs, ys, axes[0,1], labels=labels, colors=colors, lw=1, showlegend=False,
            yscientificAtLabel=True)

clp.plotone(xs, ys, axes[1,0], labels=labels, colors=colors, lw=1, showlegend=False,
            ylabel="$y$ value", xlabel="$x$ value",
            yscientificAtLabel=True)

clp.plotone(xs, ys, axes[1,1], labels=labels, colors=colors, lw=1, showlegend=False,
            xlabel="$x$ value",
            yscientificAtLabel=True)

# [Optional] adjust the legend position shown in Fig. (a)
axes[0,0].legend(loc="lower right")

# 3. tune the spacing between subplots and save file as example.png
clp.adjust(tight_layout=True, savefile="example.png")
