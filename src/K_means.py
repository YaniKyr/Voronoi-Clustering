import math 
import random
class Kmeans:

    def __init__(self,data):
        self.data = data
        #maxInt will help to do some comparisons
        self.maxInt = 999999
        self.size = len(data)
        self.means =None
    
    
    def findMinMax(self):
        #initialize two arrays of min and max
        min = [self.maxInt for i in range(self.size)]
        max = [-self.maxInt-1 for i in range(self.size)]


        for dat in self.data:
            for i in range(len(dat)):
                if dat[i]<min[i]:
                    
                    min[i] = dat[i]

                if dat[i]>max[i]:
                    max[i]=dat[i]
        return min,max


    def InitMeans(self,k,Min,Max):
        #initialize the means 
        size = len(self.data[0])
        self.means = [[0 for i in range(size)]for j in range(k)]

        #applies pseudo random values in means 
        for mean in self.means:
            for i in range(len(mean)):
                mean[i]=random.uniform(Min[i]+1,Max[i]-1)
        


    def EuclideanDistance(self,x, y):  
        S = 0 # The sum of the squared differences of the elements  
        for i in range(len(x)):  
            S += math.pow(x[i]-y[i], 2) 
    
        #The square root of the sum 
        return math.sqrt(S) 




    def UpdateMean(self,n,mean,item): 

        for i in range(len(mean)): 
            m = mean[i]
            m = (m*(n-1)+item[i])/float(n)
            mean[i] = round(m, 3)
        
        return mean



    def Classify(self,item): 
        min = self.maxInt
        # Classify item to the mean with minimum distance     
        
        index = -1
    
        for i in range(len(self.means)): 

            # Find distance from item to mean 
            dis = self.EuclideanDistance(item,self.means[i])
    
            if (dis < min): 
                min = dis
                index = i
        
        return index




    def CalculateMeans(self,k,maxIterations=100000): 
    
        # Find the min and max for columns 
        cMin, cMax = self.findMinMax()
        
        # Initialize means at random points 
        self.InitMeans(k,cMin,cMax)
        
        # Initialize clusters, the array to hold 
        # the number of items in a class 
        clusterSizes= [0 for i in range(len(self.means))]
    
        # An array to hold the cluster an item is in 
        belongsTo = [0 for i in range(len(self.data))] 
    
        # Calculate means 
        for j in range(maxIterations): 
    
            # If no change of cluster occurs, halt 
            noChange = True 
            for i in range(len(self.data)): 
    
                item = self.data[i]
    
                # Classify item into a cluster and update the 
                # corresponding means.         
                index = self.Classify(item) 
    
                clusterSizes[index] += 1
                cSize = clusterSizes[index]
                self.means[index] = self.UpdateMean(cSize,self.means[index],item)
    
                # Item changed cluster 
                if(index != belongsTo[i]): 
                    noChange = False
    
                belongsTo[i] = index
    
            # Nothing changed, return 
            if (noChange): 
                break
    
        return self.means




    def FindClusters(self): 
        clusters = [[] for i in range(len(self.means))] # Init clusters 
        
        for item in self.data: 
    
            # Classify item into a cluster 
            index = self.Classify(item)
    
            # Add item to cluster 
            clusters[index].append(item)
    
        return clusters

