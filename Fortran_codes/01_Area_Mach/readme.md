This FOTRAN code is to solve the simple Area-Mach realtion in supersonic flow.

* The code is to find the mach number by using the Area as an input
* The iteration method which here is used is Bi-section method
* The limit of Mach number is 1 to 10 (supersonic region)

----------------------------- The Compiling method -----------------------------
* Here i am using gfortran to compile the code
* Here i named the main Fortran file as Area_Mach.f90
* To run follow the comands bellow
	- gfortan -c Area_Mach.f90
	- gfortran Area_Mach.o -o run.exe
	- ./run.exe
