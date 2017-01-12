# -*- coding: utf-8 -*-
"""
This code calculates the volume of any triangular mesh given the numpy arrays. Volume of the polyhedron is 
the summation of volume of each tetrahedrons. 
"""

import numpy 
C = [0.0,0.0,0.0]
# Function implementation
def calculate_triangular_mesh_volume(file_name):

    # Loading the numpy array file    
    try:
        data = numpy.load(file_name)
    except:
        raise Exception('Cannot find file or read data')
    else:
        print("\n Numpy array file loaded succesfully")
        
    Volume = 0.0   #  Initializing the volume to zero
 
    # Calculating the volume  -- by looping for each triangular facet starts here
    for i in range (0,len(data)):
        
        if len(data[i]) == 3:              # Triangular mesh with 3 vertices
            v1 = data[i][0]  # Vertex 1
            v2 = data[i][1]  # Vertex 2
            v3 = data[i][2]  # Vertex 3

            Volume = Volume + (1.0/6.0)*numpy.dot((numpy.cross(v1-C,v2-C)),v3-C)
        else:                             #  Polygon has more than 3 vertices
            raise Exception("Please input a triangular mesh. Function yet to be implemented for facets with more than 3 vertices")
            
    return Volume

    
# Reading the input array file
#file_name = input("Enter the numpy array file name including the path: ")
#
        
# Function call    
#Volume = calculate_triangular_mesh_volume(file_name)
#print("\n Volume of the mesh =", Volume)
