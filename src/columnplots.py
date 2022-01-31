'''
Created by Tao E. Li for scientific plotting @ 2021
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#mpl.use('pdf')

# global variables for personal colors
red = "#EA4E34"
yellow = "#ECA300"
navy_blue = "#006CA3"
cyan = "#3ABCD2"
sky_blue = "#009BD6"
brown = "#7B2B15"
red_economist = "#E3000F"
black = "k"
lightblue_background = "#D9E5EC"
lightgray_background = "#F6F6F4"

def initialize(col=1, row=1, width=4,
               height=None,
               sharex=False,
               sharey=False,
               commonX=None,
               commonY=None,
               commonYs=None,
               labelthem=None,
               labelsize=None,
               labelthemPosition=None,
               fontsize=8,
               return_fig_args=False,
               LaTeX=False
               ):
    plt.rc('font', family='sans-serif', serif='Osaka')
    plt.rc('text', usetex=LaTeX)
    plt.rc('xtick', labelsize=fontsize)
    plt.rc('ytick', labelsize=fontsize)
    plt.rc('axes', labelsize=fontsize)
    if height == None:
        height = width / 1.618
    fig, axes = plt.subplots(col, row, sharex=sharex, sharey=sharey)
    fig.set_size_inches(width, height)
    if commonX != None:
        fig.text(commonX[0], commonX[1], commonX[2], ha='center', fontsize=fontsize)
    if commonY != None:
        fig.text(commonY[0], commonY[1], commonY[2],  va='center', rotation='vertical', fontsize=fontsize)
    if commonYs != None:
        for i in range(row):
            fig.text(commonYs[i][0], commonYs[i][1], commonYs[i][2],  va='center', rotation='vertical', fontsize=fontsize)
    x0, y0 = -0.10, 1.15
    if labelthemPosition != None:
        x0, y0 = labelthemPosition
    if labelsize == None:
        labelsize = fontsize + 5
    if labelthem == True:
        if row == 1:
            label1List = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)"]
            for i in range(col):
                axes[i].text(x0, y0, label1List[i], transform=axes[i].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
        elif row == 2:
            label2List = [ ["(a)", "(b)"], ["(c)", "(d)"], ["(e)", "(f)"], ["(g)", "(h)"], ["(i)", "(j)"], ["(k)", "(l)"]]
            #if LaTeX:
            #    label2List = [ [r"\textbf{a}", r"\textbf{b}"], [r"\textbf{c}", r"\textbf{d}"], [r"\textbf{e}", r"\textbf{f}"], [r"\textbf{g}", r"\textbf{h}"] ]
            if col == 1:
                i = 0
                for j in range(row):
                    axes[j].text(x0, y0, label2List[i][j], transform=axes[j].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
            else:
                for i in range(col):
                    for j in range(row):
                        axes[i,j].text(x0, y0, label2List[i][j], transform=axes[i, j].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
        elif row == 3:
            label3List = [ ["(a)", "(b)", "(c)"], ["(d)", "(e)", "(f)"], ["(g)", "(h)", "(i)"]]
            if col == 1:
                for i in range(row):
                    axes[i].text(x0, y0, label3List[0][i], transform=axes[i].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
            else:
                for i in range(col):
                    for j in range(row):
                        axes[i,j].text(x0, y0, label3List[i][j], transform=axes[i, j].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
        elif row == 4:
            label2List = [ ["(a)", "(b)", "(c)", "(d)"], ["(e)", "(f)", "(g)", "(h)"], ["(i)", "(j)", "(k)", "(l)"] ]
            if col == 1:
                i = 0
                for j in range(row):
                    axes[j].text(x0, y0, label2List[i][j], transform=axes[j].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
            else:
                for i in range(col):
                    for j in range(row):
                        axes[i,j].text(x0, y0, label2List[i][j], transform=axes[i, j].transAxes, fontsize=labelsize, fontweight='bold', va='top', ha='right')
    if return_fig_args:
        return fig, axes
    else:
        return axes

def initialize_gridSpec(col=1, row=1, width=4,
               height=None,
               fontsize=8,
               LaTeX=False
               ):
    plt.rc('font', family='sans-serif')#, serif='Times')
    plt.rc('text', usetex=LaTeX)
    plt.rc('xtick', labelsize=fontsize)
    plt.rc('ytick', labelsize=fontsize)
    plt.rc('axes', labelsize=fontsize)
    if height == None:
        height = width / 1.618
    fig = plt.figure(constrained_layout=True)
    gs = fig.add_gridspec(col, row)
    fig.set_size_inches(width, height)
    return fig, gs


def plotone(
    xs,
    ys,
    ax,
    colors=None,
    linestyles=None,
    labels=None,
    lw=2,
    markersize=None,
    xlabel=None,
    ylabel=None,
    xlog=False,
    ylog=False,
    xlim=None,
    ylim=None,
    showlegend=True,
    alphaspacing=0.0,
    alpha=1.0,
    mfc="none",
    bothyticks=True,
    yscientific=False,
    yscientificAtLabel=False,
    yscientificAtLabelString=None,
    sharewhichx=None,
    sharewhichy=None,
    legendFontSize=None,
    legndFrameOn=True,
    legendFancyBox=True,
    legendFaceColor="inherit",
    legendEdgeColor="inherit",
    rainbowColor=False,
        ):
    # Find the scienfic order for y axis
    if yscientificAtLabel == True:
        if ylim != None:
            yorder = np.floor(np.log10(np.max(np.abs(ylim[1]))))
        else:
            yorder = np.floor(np.log10(np.max(np.abs(ys[0]))))
    else:
        yorder = 0
    lines = []
    if colors == None:
        for i in range(len(xs)):
            if labels == None:
                line, = ax.plot(xs[i], ys[i]/10**yorder, lw=lw, markersize=markersize, mfc=mfc, alpha=1.0 - i*alphaspacing if alphaspacing else alpha)
            else:
                line, = ax.plot(xs[i], ys[i]/10**yorder, lw=lw, label=labels[i], markersize=markersize, mfc=mfc, alpha=1.0 - i*alphaspacing if alphaspacing else alpha)
            lines.append(line)
    else:
        for i in range(len(xs)):
            if labels == None:
                line, = ax.plot(xs[i], ys[i]/10**yorder, colors[i], lw=lw, markersize=markersize, mfc=mfc, alpha=1.0 - i*alphaspacing if alphaspacing else alpha)
            else:
                line, = ax.plot(xs[i], ys[i]/10**yorder, colors[i], lw=lw, label=labels[i], markersize=markersize, mfc=mfc, alpha=1.0 - i*alphaspacing if alphaspacing else alpha)
            lines.append(line)
    if yscientific == True:
        ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    # Add xlabel and ylabel
    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        if yorder != 0:
            if yscientificAtLabelString != None:
                ax.set_ylabel(ylabel + " [$\\times$ 10$^{%d}$ %s]" %(yorder, yscientificAtLabelString))
            else:
                ax.set_ylabel(ylabel + " [$\\times$ 10$^{%d}$]" %(yorder))
        else:
            ax.set_ylabel(ylabel)
    # Set xlim or ylim
    if xlim != None:
        ax.set_xlim(xlim[0], xlim[1])
    if ylim != None:
        ax.set_ylim(ylim[0]/10**yorder, ylim[1]/10**yorder)
    # Choose the log or normal sacling for axes
    if xlog:
        ax.set_xscale('log')
    if ylog:
        ax.set_yscale('log')
    # Add twin axes
    if bothyticks:
        ax.tick_params(direction='in')
        ax.xaxis.set_ticks_position('both')
        ax.yaxis.set_ticks_position('both')
    # Save file
    if showlegend:
        ax.legend(fontsize=legendFontSize, markerscale=legendFontSize,
            frameon=legndFrameOn, fancybox=legendFancyBox,
            facecolor=legendFaceColor, edgecolor=legendEdgeColor)
    if sharewhichx != None:
        ax.get_shared_x_axes().join(sharewhichx, ax)
        sharewhichx.set_xticklabels([])
    if sharewhichy != None:
        ax.get_shared_y_axes().join(sharewhichy, ax)
        ax.set_yticklabels([])
    if rainbowColor:
        colormap = plt.cm.gist_rainbow #nipy_spectral, Set1,Paired
        colors = [colormap(i) for i in np.linspace(0, 1,len(ax.lines))]
        for i,j in enumerate(ax.lines):
            j.set_color(colors[i])
    if linestyles != None:
        for i,j in enumerate(ax.lines):
            j.set_linestyle(linestyles[i])
    return lines

def broken_y(ax, ax2, d=0.015, ymin_0=0, ymax_0=0.22, ymin_1=0.78, ymax_1=1.0):
    # zoom-in / limit the view to different portions of the data
    ax.set_ylim(ymin_1, ymax_1)  # outliers only
    ax2.set_ylim(ymin_0, ymax_0)  # most of the data

    # hide the spines between ax and ax2
    ax.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.xaxis.tick_top()
    ax.tick_params(labeltop=False)  # don't put tick labels at the top
    ax2.xaxis.tick_bottom()
    # This looks pretty good, and was fairly painless, but you can get that
    # cut-out diagonal lines look with just a bit more work. The important
    # thing to know here is that in axes coordinates, which are always
    # between 0-1, spine endpoints are at these locations (0,0), (0,1),
    # (1,0), and (1,1).  Thus, we just need to put the diagonals in the
    # appropriate corners of each of our axes, and so long as we use the
    # right transform and disable clipping.
    kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
    ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal
    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
    ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

def adjust(
    wspace=0,
    hspace=0,
    tight_layout=False,
    savefile=None,
    includelegend=None
    ):
    #plt.subplots_adjust(wspace=wspace, hspace=hspace)
    if tight_layout == True:
        plt.tight_layout()
    if savefile != None and includelegend == None:
        plt.savefig(savefile, dpi=300, bbox_inches="tight")
    if savefile != None and includelegend != None:
        plt.savefig(savefile, dpi=300, bbox_extra_artists=(includelegend,), bbox_inches='tight')
    # show figure
    plt.show()

if __name__ == '__main__':
    x = np.linspace(0, 1e4, 100)
    y = np.exp(-1e-4*x)
    y2 = np.cos(x)
    axes = initialize(2,1)
    plotone([x, x], [y, y2], axes[0], labels=['data 1', 'data 2'],  ylabel='$P_2$')
    plotone([x, x], [y*0.5, y2*2], axes[1], labels=['data 1', 'data 2'], xlabel='time', ylabel='$P_2$')
    adjust(tight_layout=True)
