#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:50:01 2017

@author: vchalama
"""

import unittest

from polyhedron_mesh_volume import calculate_triangular_mesh_volume

class volume_test_case(unittest.TestCase):
    """ Test case for calculate_triangular_mesh_volume """
    
    def test_unit_cube_volume(self):
        file_name  = "mesh_volume/unit_cube_qppp.npy"
        self.assertAlmostEqual(calculate_triangular_mesh_volume(file_name),1.0,places=9,msg='Volumes not equal')
        
    def test_shell_volume(self):
        file_name  = "mesh_volume/shell.npy"
        self.assertAlmostEqual(calculate_triangular_mesh_volume(file_name),3.6586764273115655,places=9,msg='Volumes not equal')
    
    def test_robot_volume(self):
        file_name  = "mesh_volume/Robot_Maker_Faire_65pc.npy"
        self.assertAlmostEqual(calculate_triangular_mesh_volume(file_name),43677.42582662092,places=9,msg='Volumes not equal')
        
if __name__ == '__main__':
    unittest.main()