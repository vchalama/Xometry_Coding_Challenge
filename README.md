#This code calculates the volume of polyhedron with triangular facets. 

* Numpy extension is required to run this code. 

* polyhedron_mesh_volume.py 
    * This is the file which implements the function. User needs to input the numpy array file name including its path. After the file name
      is entered, code will execute and will output the volume on the screen. 
    * It will throw an exception if the file is unreadable or not found. 
    * It will throw an exception if the polyhedron has facets with more than 3 vertices.

* Test cases 
  * unit_test.py  is the test case file.  It checks if the calculate_triangular_mesh_volume function is calculating the volume
    correctly by comparing the function output with the volumes known apriori.  Test cases check volumes for unit cube and two
    other known geometries given in the mesh_volume folder. 
