# CNM:

CNM is a python package for computational neuroscience modelling. It is designed to be a flexible and easy-to-use tool for building and simulating neural networks and other computational models related to neuroscience. 

## Classification of models:

I will be using Marr D's classification of models as a guide for the development of this package. The classification includes:

1. Descriptive Models
   * Neural firing rate models 
   * Population rate models
   * Neural field models 
2. Mechanistic Models 
   * Hodgkin-Huxley models
   * Synaptic models such as STDP and Tsodyks-Markram
   * Biophysical Models such as Izhikevich and FitzHugh-Nagumo
3. Interpretive Models 
   * Integrate-and-Fire models
   * Generalized linear models such as temporal filtering, bernoulli GLM and Logistic regression


## Hierarchy of the package:
I will be starting the package development by designing the hierarchy of the package. The package will be divided into three main modules:
1. the `models` module. Which will contain all the different models that can be used to initiate the type of model that the user wants to simulate.
2. the `algorithm` module. Which will contain submodules for different algorithms that can be used to simulate the model. For example, the `algorithm` module will contain a `STDP` submodule that will contain the algorithm that can be used to solve the model.
3. the `utils` module. Which will contain submodules for different utilities that can be used to analyze the results of the simulation. For example, the `utils` module will contain a `plot` submodule that will contain the functions that can be used to plot the results of the simulation.

## Installation:
The project will soon be available for installation through `pip`. For now, you can install the package by cloning the repository and running the following command in the root directory of the project:
```bash
git clone 
```

## Contribution:
Feel free to contribute to the project by opening an issue or a pull request. Any contribution is welcome.