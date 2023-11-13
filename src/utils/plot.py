import matplotlib.pyplot as plt 

def plot_spike(x,y,label=None,title=None,legend=False,xlabel=None,ylabel=None):
    plt.figure(figsize=(10,6))
    plt.plot(x,y,label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if legend:
        plt.legend()
    plt.show()
