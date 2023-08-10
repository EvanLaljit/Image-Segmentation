# Image Segmentation
## Description 
 This Python-based, object-oriented project uses an image segmentation model, https://github.com/facebookresearch/segment-anything, to mask images and the python package PIL to edit images. It provides a user-friendly interface for cropping and editing several different features of images, as well as for masking any number of objects within these images using different combinations of input parameters.
 ## Folders
 The example masking folder contains 3 sets of example images and code to mask these images. 

The Jupyter notebook folder contains the Jupyter notebook file which documents in detail how to use the code.

The source code folder contains all Python files necessary to edit and mask images.

The requirements.txt contains all required Python packages. 

## Installation
To properly use the code, the necessary Python packages need to be installed using the requirements.txt file already provided. Additionally, from the segmentation model githubpage linked above, one of the model checkpoints must be installed to use the masking feature of this project. 

## How to Use
The source code contains the code to edit and mask images, via multiple different classes. 

The Jupyter Notebook contains all the necessary documentation to figure out how to use the code for image editing and masking. In particular, it contains more information on the package installation and importation, as well as methods to **test cropping and editing of the images before you save them**. In addition, you can try to mask the images "manually" without the use of the source code's classes. Finally, it contains the classes already found in the source code folder as well as a **thorough explanation of how to use the predictor function** within the masking class, and some more examples of using the classes. 
