# Donatello

Donatello is the TensorFlow implementation of my research paper [Aided Modeling](bishopcolton.com) which proposes a topology and symmetry-aware deep learning architecture that incorporates user analysis to build upon a state of the art approach for generating 3D mesh models from 2D images described in [this paper](http://openaccess.thecvf.com/content_ECCV_2018/papers/Nanyang_Wang_Pixel2Mesh_Generating_3D_ECCV_2018_paper.pdf). This research project was advised my [Professor Jia Deng](https://www.cs.princeton.edu/~jiadeng/). 

## Get Started with Donatello

Follow the instruction beow to build a copy of the project on your local machine for development and testing purposes.

### Dependencies and Requirements

Set up the Pixel2Mesh and Donatello environment with the following:

Python2.7+ with Numpy and scikit-image
Tensorflow (version 1.0+)
TFLearn

The code has been tested with Python 2.7, TensorFlow 1.3.0, TFLearn 0.3.2, CUDA 8.0 on Ubuntu 14.04.

### Installation

```
git clone https://github.com/coltonbishop/donatello.git
```

Download the trained model [here](bishopcolton.com) and save it to the directory 'mesher/utils'.

Navigate to the directory 'mesher/external' and change the first three lines of the makefile to point to your nvcc, cudalib and tensorflow libraries. Then run:

```
make
```
## Model an image

Navigate to the directory 'mesher' and save the PNG image you would like to model here. (This image should be a single object with a white background.) Next, run the command:

```
python demo.py --image your_image.png
```

Optionally, include any of the arguments below to provide the system with more information about the symmetry (-s), complexity (-c), or topology (-t) of your object:

```
-s x y z p (where x, y, z, and p define a plane of symmetry through your object)
-c m b (where m and b define a line of complexity through your object)
-t d (where d is one of the supported object domains) 
```

To better understand how to determine and provide these values, 


## Contributors

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc## Donatello

```
pip install donatello
```

</br>
<p align="center">
<img src="resources/poster.png" width = "825px" />
</p>

<p align="center">
<img src="resources/domain.png" width = "200px" />

<img src="resources/complex.png" width = "200px" />

<img src="resources/sym.jpg" width = "200px" />
</p>

</br>
