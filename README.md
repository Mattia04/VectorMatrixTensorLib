# VectorMatrixTensorLib

This is a library module that makes working with vectors, matrices and tensors easy, intuitive and at the same time very precise.

In the next chapters are described the modules in detail.

## Scope of the project

I'm a physics student, and I created this repository to learn python programming for scientific pourposes.

Feel free to use and contribute to this repository.

## Vectors

Vectors store n-dimensional information in an array-like structure, this library makes possible to work with n-dimensional vectors, 2-dimensional vectors and 3-dimensional vectors.

### Vector

This class it's a general vector class for n-dimensional vectors.

To create a vector simply write: ```Vector(1, 3.4, ...)```, the number of arguments it's the same as the vector dimension. The vectors sores the cartesian coordinates as a list.

You can access the coordinates with ```.coords``` (you can modify the coordinates of the object, even tho it's not recommended use ```.translate(...)``` instead) or with ```.get_cartesian_coordinates()``` (you cannot modify the coordinates of the objet)

To the the modulus of the vector use the ```.module``` property.

The operations defined are: addition, negation, subtraction, multiplication by scalar, inner product, division by scalar and integer power. Those operations need the vectors to be of the same length.

You can check if the vector is a zero vector by using ```.is_zero()``` method.

You can copy a vector by using ```.copy()```.

You can modify in place the coordinates of the vector using ```.translate(origin)```, where ```origin``` is a vector with the same dimension as the vector you want to translate.

You can normalize(get a parallel vector with module equal to 1) the vector, in place using ```.normalize()``` or in a new instance using ```.get_normalized()```.

You can create a parallel vector by using ```.create_parallel(module)```, where module is the module of the new vector.

**TO BE ADDED IN FUTURE**
Getting two vectors to the same length: you can shorten the longest to the shortest, or increase the shorter to the longer one.

**TO BE ADDED IN FUTURE**
If you don't know the length of the vector you can use ```Vector.shorten_to_minimum_length(a, b)``` and ```Vector.stretch_to_maximum_length(a, b)``` where ```a``` and ```b``` are ```Vector()```.

You can check if two vectors have the same dimension with ```have_same_dimension(a, b)``` where ```a``` and ```b``` are ```Vector()```.

You can get the distance between two vectors with ```Vector.distance(a, b)``` where ```a``` and ```b``` are ```Vector()```.

### Vec2

I'm too lazy to do this now

### Vec3

I'm too lazy to do this now

## Matrices

**NOT YET IMPLEMENTED**.

## Tensors

**NOT YET IMPLEMENTEd**.
