#This code calculates the volume of polyhedron with triangular facets. 

To clone the repository into your local machine, type the following command in the terminal. 
git clone https://github.com/vchalama/Xometry_coding_challenge.git

* Numpy extension is required to run this code. 

* Implementation -- polyhedron_mesh_volume.py has the implementation of all functions 

    * When you run this python file, it will ask for the numpy array file name including its path. After the file name
      is entered, code will execute and will output the volume on the screen. 

    * It throws an exception if the file is unreadable or not found. 

    * It throws an exception if the facet is not a triangle. 

    * It displays a warning message if the geometry is non-manifold.


* Test cases -- unit_test.py is the test case file

  * First three test cases verify if the calculate_triangular_mesh_volume function is 
    accurately calculating the volume of know objects. 

  * Fourth test case checks if the geometry is manifold or non-manifold.
    It throws an error if the geometry is non-manifold.
