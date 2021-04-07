from matplotlib import pyplot as plt
class JarvisMarch:

    def __init__(self,data):
        self.data = data
        self.x =  [dat[0] for dat in data]
        self.y =  [dat[1] for dat in data]
        self.size = len(self.x)
    def LeftPoint(self):
        #find the most left point
        min = 0 
        
        for i in range(1,len(self.x)):
            
            if self.x[i]< self.x[min]:
                min = i
            elif self.x[i]==self.x[min]:
                if self.y[i]> self.y[min]:
                    min=i
        return min

    def Orientation(self,p,q,r):
        # calculate the orientation of the points
        #If val is 2 the points are counter-clockwise
     
        val = (self.y[q] - self.y[p]) * (self.x[r] - self.x[q])- \
        (self.x[q] - self.x[p]) * (self.y[r] - self.y[q]) 
    
        if val == 0: 
            return 0
        elif val > 0: 
            return 1
        else: 
            return 2

    def ConvHull(self):

        p = self.LeftPoint()
        temp = p
        hull = []
        #initialize the point q for later usage
        q=0
        #assign the p to l
        #l  will help to exit 
        #the while loop until the "wrapping" is over
        l=p

        while(True):

            #keep track of last visited most counterclock-  
            #wise point in q. If any point 'i' is more counterclock-  
            #wise than q, then update q. 

            hull.append(p)

            q = (p+1) % self.size 
            for i in range(len(self.x)):
                if(self.Orientation(p,i,q)==2):
                    q=i
            #Now the q is the most counterclockwise point
            #append it in p and we re-do the search 
            #for the most counter-clockwise point
            p=q
            #exit if the last point p is equals to point l
            if(p==l):
                break
        hullx = []
        hully=[]
        # Print Result  
        for each in hull: 
            hullx.append(self.x[each])
            hully.append(self.y[each])
        #plot the bounding of the cluster inside this class
        plt.plot(hullx,hully,color = 'blue',linewidth=2)
        plt.plot(self.x[temp],self.y[temp],self.x[hull[len(hull)-1]],self.y[hull[len(hull)-1]])


