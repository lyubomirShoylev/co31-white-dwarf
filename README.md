# co31-white-dwarf

This project studies the structure of white dwarf by numerically solving the equation of state given by the degenerate electron gas. For an in-depth discussion of methods and results, look for the lab report at `report/co31-report`.

## Physics problem

The physics problem set is the following --- assuming a white dwarf in the simplest case (no rotation, magnetic fields, etc.) there are two forces acting on the matter inside the white dwarf:

* gravity, which tries to shrink the star, i.e. inwards pressure;
* electron degeneracy pressure, which acts as outwards pressure.

Given that we are in the simplest case, we can derive two coupled radial equations for the mass and density of matter, which we will solve numerically rather than analytically. There are two possible cases, for non-relativistic and relativistic electrons, which have a different expression for the differential equation.

A specific range of central density is provided in the assignment to guide the student to exploring new physics. The final goal is finding out the dependence of radius and total mass on central density, as well as dependence of size on total mass.

## Numerical solution

The task of numerically integrating the system of equations is done with a simple Runge-Kutta 4th order (RK4) method. Comparison of simpler methods to RK4 is presented in the lab report.

Another element to consider is the step size used between consecutive calculations in the integration. This has also been tested and an optimal value has been chosen based on a convergence criterion for the whole range of values tested.

Finally, due to the large number of calculations needed to perform the integration (even with an optimal step size), additional effort has been made to speed up the process by simple parallelisation of calculations for different values of central density.

## Results

By running the procedures we find that for relativistic electrons there is a limiting mass --- the Chandrasekhar limit. More details in the lab report.

## Skills acquired

During the making of this project, I learned several new things:

* General OOP concepts in Python such as class inheritance: built a generic differential equation solver parent class and a white dwarf child class.
* Python-specific package building: prepared a mini-library for the white dwarf solver.
* Data visualisation using matplotlib and proper preparation of figures.
* Simple parallelisation using `multiprocessing` library to speed up calculations.
* Document preparation in LaTeX: improved on previous knowledge and devised a simple collection of packages to facilitate university reports, as well as creating a bibliography using JabRef.
