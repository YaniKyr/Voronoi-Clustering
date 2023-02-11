
from matplotlib import pyplot as plt 
class Vertex:
    def __init__(self,id,coords,edge):
        self.id = id
        self.coords = coords
        self.edge = edge


class Edge:
    def __init__(self,id,start,end):
        self.id  = id 
        self.start = start
        self.end = end
class HalfEdge:
    def __init__(self):
        self.halfedge = None
        self.origin = None
        self.next = None
        self.previous = None
        self.twin = None
        self.face = None
        


class Graph:
    
    def __init__(self):
        self.halfe = []
        self.count = 0
        self.index = 0
        self.temp =HalfEdge()
        
    
    def CreateHE(self,coords1,coords2):
        #create the origin Halfedge and the next and create a linkage between them!!!!!!!!!
        
        _instance = HalfEdge()
        
        if self.temp is not None:
            
            _instance.previous = self.temp
            
        self.temp = self.InsertInto(_instance,coords1,coords2)
        
        self.halfe.append(_instance)
        self.halfe[self.index-1].next = self.temp
        
        self.index +=1


    def InsertInto(self,_instance,coords1,coords2):
        self.count +=1

        
        temp = self.count+1
        
        _instance.halfedge =Edge('e'+str(self.count)+'-'+str(temp),coords1,coords2)
        _instance.origin = Vertex('u'+str(self.count),coords1,_instance.halfedge)
                    
        
        _instance.twin = Edge('e'+str(temp)+'-'+str(self.count),coords2,coords1)
        
        self.temp = _instance
        return _instance


    def PrintHE(self):
        if self.halfe is not None:
            for i in range(len(self.halfe)):
                    print(self.halfe[i].halfedge.id,self.halfe[i].origin.id,self.halfe[i].twin.id,self.halfe[i].next.halfedge.id,self.halfe[i].previous.halfedge.id)
        print("Just want to print a specific instance of the Graph:")
        print("Prev  Current  Next")
        print(self.halfe[len(self.halfe)-1].previous.halfedge.id,self.halfe[len(self.halfe)-1].halfedge.id,self.halfe[len(self.halfe)-1].next.halfedge.id,self.halfe[len(self.halfe)-1].next.halfedge.end)
    
        print("Vertices:")
        for i in range(len(self.halfe)):
            print(self.halfe[i].origin.id,self.halfe[i].origin.coords,self.halfe[i].origin.edge.id)        

    def PlotHe(self):
        if self.halfe is None:
            print("DCEL is Empty")
        point_x = [self.halfe[i].origin.coords[0] for i in range(len(self.halfe))]
        point_y = [self.halfe[i].origin.coords[1] for i in range(len(self.halfe))]
        return plt.plot(point_x,point_y,color = 'blue',linewidth=2)
    
    def PlotHe3D(self):
        if self.halfe is None:
            print("DCEL is Empty")
        fig  =plt.figure()
        ax = fig.add_subplot(111,projection = '3d')

        point_x = [self.halfe[i].origin.coords[0] for i in range(len(self.halfe))]
        point_y = [self.halfe[i].origin.coords[1] for i in range(len(self.halfe))]
        point_z = [self.halfe[i].origin.coords[2] for i in range(len(self.halfe))]
        return ax.plot(point_x,point_y,point_z,color = 'blue',linewidth =2)
        