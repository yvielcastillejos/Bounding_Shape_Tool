# Bounding_Shape_Tool
A tool useful for bounding circles around an object. This tool can be used for bounding images for Neural Network Training.
Tips:
- The images are recommended to be squares before passing into the tool to avoid distortion.
## Instructions
If one wants to use this tool:
- Clone this repository
- Install pygame
- Install math libraries such as Numpy, Scipy, and Matplotlib.
- In ```config.py```, change the directory of the images you want to label with bounding circles (under ```path_to_imgs```)
- In ```config.py```, change the directory where you want the bounded images to be saved (under ```path_to_save```)
- Note that making the directory ```path_to_img``` and ```path_to_save``` the same path, the original image will be overwritten by the labelled image.
- run   ``` python3 src/main.py```


| Files| Description|
|-----|-------------|
| ```main.py```| run this to use the tool|
| ```config.py``` | contains the configuration for the program. Change file path here.|
|```boundbox.py```| contains the functions for renderring GUI|
|```buttons.py ```| Functions for rendering the buttons and text|

## Demo
A demo as shown:                                
<img src = "https://github.com/yvielcastillejos/Bounding_Shape_Tool/blob/main/Bound.gif" width = "500" height = "500">
- Note that once it is saved, the circles can no longer be undone
## Next Steps
- I can add the option to use bounding squares instead of circles.
- This was inspired by coin counter project.
