#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
There are four different test cases in this file. 

test_unit_cube_volume, test_shell_volume and test_robot_volume verifies if calculate_triangular_mesh function calculates
 the volume accurately. Validation is done by comparing with volumes known apriori

test_manifold verifies if a particular geometry is manifold or not.  There are many 
criterion which can make a geometry nonmanifold, however only a simple scenario is 
considered here. The criteria used to verify here is whether a particular edge is shared 
between two triangular facets. This unit test throws an error if an edge is part of only
one facet or if it is shared between three or more triangular facets.

@author: vchalama
"""

import unittest

from polyhedron_mesh_volume import calculate_triangular_mesh_volume
from polyhedron_mesh_volume import is_manifold

class volume_test_case(unittest.TestCase):
    
    def test_01_unit_cube_volume(self):
        file_name  = "mesh_volume/unit_cube_qppp.npy"
        self.assertAlmostEqual(calculate_triangular_mesh_volume(file_name),1.0,places=9,msg='Volumes not equal')
        print("Test passed: Volume verified for",file_name,"\n")

    def test_02_shell_volume(self):
        file_name  = "mesh_volume/shell.npy"
        self.assertAlmostEqual(calculate_triangular_mesh_volume(file_name),3.6586764273115655,places=9,msg='Volumes not equal')
        print("Test passed: Volume verified for",file_name,"\n")

    def test_03_robot_volume(self):
        file_name  = "mesh_volume/Robot_Maker_Faire_65pc.npy"
        self.assertAlmostEqual(calculate_triangular_mesh_volume(file_name),43677.42582662092,places=9,msg='Volumes not equal')
        print("Test passed: Volume verified for",file_name,"\n")

    def test_04_manifold(self):
        test_if_manifold=input("Do you want to perform a manifold test on your geometry.Press y or n:")
        if test_if_manifold=="y":
            file_name  = input("Enter the numpy array file name including the path: ")
            self.assertTrue(is_manifold(file_name), msg='Geometry is non-manifold')
            print("Test passed:",file_name," is manifold\n")	   
        elif test_if_manifold=="n":
            print("Unit test completed")
        else:
            print("\033[0;31mNot a valid response")
  
            
if __name__ == '__main__':
    unittest.main()
