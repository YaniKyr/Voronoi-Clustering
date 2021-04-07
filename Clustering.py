import K_means as km
import matplotlib.pyplot as plt
import ConvexHull as ch


#It parses a file
def Mini_Parse(filename):
    file = open(filename,"r")
    mfile=file.read()
    file.close()
    data = [i.split("    ") for i in mfile.split("\n")]
    
    for i in range(len(data)):
        
        data[i].remove('')

    size = len(data)-1
    data.remove(data[size])


    _data = [[int(data[i][j]) for j in range(len(data[i]))]for i in range(len(data))]
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

_data = Mini_Parse("data.txt")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_facecolor("black")

# We create an object of the Kmeans class and we put the data in it
kmeans = km.Kmeans(_data)
#The input defines the number of centroids and it calculates them
means = kmeans.CalculateMeans(4)
#Based on the means or centroids it creates the clusters
clusters = kmeans.FindClusters()


# Call for each cluster the Jarvis March Algorithm
for i in range(len(clusters)):
    if len(clusters[i]) <=1:
        continue
    else:
        chtemp = ch.JarvisMarch(clusters[i])
        chtemp.ConvHull()


#===============Visualization======================
means_x1 = [i[0] for i in means]
means_y1 = [i[1] for i in means]

cluster_x = [[clusters[i][j][0] for j in range(len(clusters[i]))] for i in range(len(clusters))]
cluster_y = [[clusters[i][j][1] for j in range(len(clusters[i]))] for i in range(len(clusters))]
                
for i in range(len (clusters)):
    plt.scatter(cluster_x[i],cluster_y[i],s=5)


plt.scatter(means_x1,means_y1,color= "white")

plt.show()
