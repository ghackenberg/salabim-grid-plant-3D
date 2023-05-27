# Factory Design Automation

In this project we study techniques for reducing the effort of modeling and analyzing factory layouts.
To achieve this goal, we develop an easy-to-use configurator and simulator for a particular class of factories.
More precisely, we concentrate on flexible manufacturing systems, which can be adapted to a variety of products and processes.
We assume that the material flow between the work stations of the factory is handled completely by gantry robots.

## Requirements

To use this project, you need to install the following software packages on your machine.
Note that simulation experiments can be carried out without the optional software packages.

* Python
* *Discrete event simulation support*
  * Salabim
  * *3D animation support (optional)*
    * PyOpenGL
    * PyOpenGL_accelerate
  * *OBJ Wavefront file format support (optional)*
    * PyWavefront
    * PyGlet
  * *Video production support (optional)*
    * opencv-python
    * numpy
* *Graph visualization support (optional)*
  * NetworkX
  * Matplotlib

## Screenshots

Here are some screenshots of our prototypes:

### 🖼️ Simulator

We provide a discrete event simulator with 3D visualization capabilities.

![Salabim screenshot](./screenshots/salabim.png)

### 🖼️ Visualizer

We also provide a visualization of the possible products and processes.

![NetworkX screenshot](./screenshots/networkx.png)

## Models

Here are some models explaining our overall idea:

### 📈 Class model

The class model describes the entities of factory design:

![Class model](./models/class-model.png)

### 📈 Object model

The object model describes an example factory design:

#### Object model 1

![Object model 1](./models/object-model-1.png)

#### Object model 2

![Object model 2](./models/object-model-2.png)

## Folders

You find more information in the following folders:

* [Models](./models)
* [Prototypes](./prototypes)
* [Screenshots](./screenshots)