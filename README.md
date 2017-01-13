#This code calculates the volume of polyhedron with triangular facets. 

* Numpy extension is required to run this code. 

* Implementation -- polyhedron_mesh_volume.py if the file which implements all functions 

    * When you run this python file, it will ask for the numpy array file name including its path. After the file name
      is entered, code will execute and will output the volume on the screen. 

    * It will throw an exception if the file is unreadable or not found. 

    * It will throw an exception if the facet is not a triangle. 

    * It will display a warning message if the geometry is non-manifold.


* Test cases -- unit_test.py is the test case file

  * First three test cases verify if the calculate_triangular_mesh_volume function is 
    accacurately calculating the volume of know objects. This test case calls
    calculate_triangular_mesh_volume function for geometries whose volume is known apriori.
         
  * Fourth test case checks if the geometry is manifold or non-manifold.
    It throws an error if the geometry is non-manifold.
