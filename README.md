# Tiny_Sphere

I reproduced the paper Reach for the Spheres: Tangency-Aware Surface Reconstruction of SDFs here. Feel free to use this code.

For the SDF file, I generated them by my another repository code, you can have a look at https://github.com/alecjacobson/geometry-processing-mesh-reconstruction. I can't post the code since the course policy.

# Results

| Model | Cat(32x39x46) | Elephant(26x34x32) |  Elephant(42x62x56) |
| -- | -- | -- | -- |
| pass 1 | <img src="img/cat1.png" alt="isolated" width="200"/> | <img src="img/elephant11.png" alt="isolated" width="200"/> | <img src="img/elephant21.png" alt="isolated" width="200"/> |
| pass 2 | <img src="img/cat2.png" alt="isolated" width="200"/> | <img src="img/elephant12.png" alt="isolated" width="200"/> | <img src="img/elephant22.png" alt="isolated" width="200"/> |
| pass 3 | <img src="img/cat3.png" alt="isolated" width="200"/> | <img src="img/elephant13.png" alt="isolated" width="200"/> | |
| ground truth | <img src="img/ground_cat.png" alt="isolated" width="200"/> | <img src="img/ground_elephant1.png" alt="isolated" width="200"/> | <img src="img/ground_elephant1.png" alt="isolated" width="200"/> |