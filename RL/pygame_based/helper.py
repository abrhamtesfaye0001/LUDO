import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(plotables):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Moves')
    plt.ylabel('Score')
    # plt.ylim(ymin=0)
    for plotDict in plotables:
        plotable = plotDict["plotable"]
        plt.plot(plotable,plotDict["color"][0] )
        
        plt.text(len(plotable)-1, plotable[-1], str(plotable[-1]))
        
    plt.show(block=False)
    plt.pause(.1)
