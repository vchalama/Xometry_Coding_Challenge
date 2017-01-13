# -*- coding: utf-8 -*-
"""
This code calculates the volume of any triangular mesh geometry given the numpy arrays. Volume of the polyhedron is 
the summation of volume of each tetrahedron formed by three vertices of the triangular facet and the origin. This code
works for both convex and concave polyhedrons.
@author: vchalama
"""
###############################################################################
import numpy 
###############################################################################
"""Function to calculate volume"""
def calculate_triangular_mesh_volume(file_name):

    # Loading the numpy array file    
    try:
        data = numpy.load(file_name)
    except:
        raise Exception('Cannot find file or read data')
        
    Volume = 0.0   #  Initializing the volume to zero
 
    """Calculating the volume by looping over each triangular facet"""
    for i in range (0,len(data)):
        
        if len(data[i]) == 3:              
            """ Triangular mesh with 3 vertices """
            v1 = data[i][0]  # Vertex 1
            v2 = data[i][1]  # Vertex 2
            v3 = data[i][2]  # Vertex 3

            Volume = Volume + (1.0/6.0)*numpy.dot((numpy.cross(v1,v2)),v3)
        else:                             
            """Polygon has more than 3 vertices"""
            raise Exception("Please input a triangular mesh. Function yet to be implemented for facets with more than 3 vertices")
            
    return Volume

    
    
###############################################################################
""" Function to determine whether the object is manifold"""  
def is_manifold(file_name):
    # Loading the numpy array file
    try:
        data = numpy.load(file_name)
    except:
        raise Exception('Cannot find file or read data')
        
    edge_dict = dict()
    # Loop over each triangle 
    for i in range (0,len(data)):
        if len(data[i]) == 3:              
            """ Triangular mesh with 3 vertices """
            
            # Obtaining edges of each triangle
            for j in range(0,3):
                e = []
                e.append(data[i][j])
                v2=data[i][j+1] if j<2 else data[i][0] # Second vertex of the edge
                e.append(v2)
                e = order(e)
                
                if e in edge_dict.keys():
                    edge_dict[e]=edge_dict[e]+1
                else:
                    edge_dict[e]=1

                if edge_dict[e]>2:
                    return False
        else:                             
            """Polygon has more than 3 vertices"""
            raise Exception("Please input a triangular mesh. Function yet to be implemented for facets with more than 3 vertices")
            
    for k in edge_dict.keys():
        if edge_dict[k]!=2 :
            return False  
        
    return True
###############################################################################    


""" Function to order vertices """
def order(vertex_list):
    vertex_list.sort(key=lambda tup: (tup[0],tup[1],tup[2]))
    edge_tup = (tuple(vertex_list[0]),tuple(vertex_list[1]))
    return edge_tup
###############################################################################    
    

""" Main function """
def main():
    while True:
        # Reading the input array file
        file_name = input("\nEnter the numpy array file name including the path: ")
       
        # Function call 
        imf = is_manifold(file_name)
        if imf==False:
            print("\033[1;31mWarning: Geometry object is non-manifold\033[1;m")    
        Volume = calculate_triangular_mesh_volume(file_name)
        print("\033[1;30mVolume of the mesh =\033[1;m", Volume)
 
        another_volume = input("\nDo you want to calculate volume for another polyhedron. Press y or n: ")

        if another_volume=="y":
            continue
        elif another_volume=="n":
            print("\nExiting the function\n")
            break
        else:
            print("\n\033[1;31mWarning: Invalid selection\033[1;m")
            break
       
if __name__ == '__main__':
    main()
