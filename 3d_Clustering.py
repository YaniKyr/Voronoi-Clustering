import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import K_means as km
import D3ConvexHull as d3ch
import time
#It parses a file
def Mini_Parse(filename):
    file = open(filename,"r")
    mfile=file.read()
    file.close()
    data = [i.split(" ") for i in mfile.split("\n")]
    _data = [[float(dat[i])*1000000 for i in range(3)]for dat in data]
   
    return _data

#It calculates the fail rate of Clustering
def Failrate(clusters):
    count1=0
    count2=0
    for clust in clusters:
        
        if clust is None or len(clust) <=1:
                count1+=1
        else:
            count2+=1
    return (count1/len(clusters))*100

#===========Main========================    
_data =Mini_Parse("stars.txt")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor("black")


# We create an object of the Kmeans class and we put the data in it 
kmeans = km.Kmeans(_data)
#The input defines the number of centroids and it calculates them
means = kmeans.CalculateMeans(35)
#Based on the means or centroids it creates the clusters
clusters = kmeans.FindClusters()
    
 

hullx = []
hully = []
hullz = []

# Call for each cluster the Jarvis March Algorithm
for i in range(len(clusters)):
    if(len(clusters[i]))<=1:
        continue
    else:
        temp = d3ch.JarvisMarch(clusters[i])
        hullx,hully,hullz = temp.ConvHull()
        # It returns three arrays, one for each dimension.
        # It plots the arrays inside these loop because after evey run
        # it clears its three arrays because we do not want to save 
        # all the points, but one cluster per loop.
        ax.plot(hullx,hully,hullz,linewidth = 2,color = "white")
        hullx.clear()
        hully.clear()
        hullz.clear()
    
#===============Visualization======================
means_x = [mean[0] for mean in means]
means_y = [mean[1] for mean in means]
means_z = [mean[2] for mean in means]


cluster_x = [[clusters[i][j][0] for j in range(len(clusters[i]))] for i in range(len(clusters))]
cluster_y = [[clusters[i][j][1] for j in range(len(clusters[i]))] for i in range(len(clusters))]
cluster_z = [[clusters[i][j][2] for j in range(len(clusters[i]))] for i in range(len(clusters))]

                
        
#for i in range(len (cluster_x)):
#    ax.scatter(cluster_x[i],cluster_y[i],cluster_z[i])

ax.scatter(means_x,means_y,means_z,color="black")
plt.show()
