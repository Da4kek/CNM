import matplotlib.pyplot as plt 

def plot_spike(x,y,label=None,title=None,legend=False,xlabel=None,ylabel=None,marker=None):
    plt.figure(figsize=(10,6))
    plt.plot(x,y,label=label,marker=marker)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if legend:
        plt.legend()
    plt.show()

def plot_sep(x,y,**kwargs):
    plt.plot(x,label = kwargs['xlegend'])
    plt.plot(y,label = kwargs['ylegend'])
    plt.xlabel(kwargs['xlabel'])
    plt.ylabel(kwargs['ylabel'])
    plt.grid(True)
    plt.legend()
    plt.show()