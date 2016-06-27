import numpy as np
from sklearn.cluster import KMeans

class BagOfVisualWords:

    def __init__(self, clusterCount, trainingDescriptorsList):
        self.clusterCount = clusterCount
        self.trainingDescriptorsList = trainingDescriptorsList

    def getHistogramForImages(self, eigenVectorsDictionary, emotions):
        kMeans = KMeans(100)
        kMeans.fit(self.trainingDescriptorsList) # Cluster the descriptors to form words

        histogramDictionary = {}

        for emotion in emotions:

            eigenvectorsList = eigenVectorsDictionary[emotion]
            histogramList = []

            for eigenvectors in eigenvectorsList:

                img_clustered_words = kMeans.predict(eigenvectors) # Each descriptor is mapped to a word
                print len(img_clustered_words)

                histogram = np.array(
                    [np.bincount(img_clustered_words, minlength=self.clusterCount)]) # Create a histogram ; how many times does a word (cluster) come in an image?

                histogramArray = np.array(histogram)
                print histogramArray.shape

                histogramList.append(histogramArray)

            histogramDictionary[emotion] = histogramList

        return histogramDictionary
