import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler

class Classify_WF:
    def __init__(self,spike_waveforms):
        self.spike_waveforms = spike_waveforms
        self.scaler = StandardScaler()
        self.normalized_features = None 

    def fit(self): 
        features = np.vstack((np.mean(self.spike_waveforms,axis=1),np.std(self.spike_waveforms,axis=1))).T
        self.normalized_features = self.scaler.fit_transform(features)
        
        kmeans = KMeans(n_clusters=2,random_state = 0)
        cluster_labels = kmeans.fit_predict(self.normalized_features)
        return cluster_labels
    
    def visualize(self):
        for id in range(2):
            cluster_samples = self.spike_waveforms[self.fit() == id]
            plt.figure()
            for sample in cluster_samples:
                plt.plot(sample,color='g',alpha=0.5,marker='o')
            plt.title(f"Cluster {id}")
        plt.xlabel("Time")
        plt.ylabel("amplitude")
        plt.show()