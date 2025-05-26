# SketchFL: Federated Learning via Matrix Sketching

Welcome to **SketchFL**, a research contribution to the OpenFL community. This project explores **integrating sketch-based compression into federated learning workflows**, using OpenFL's experimental Workflow API to accelerate both training and inference while reducing communication overhead. Additionally, the framework adds a basic level of privacy by obfuscating the original (high-dimensional) model updates through sketching.

> **Note:** This document describes the SketchFL methodology and supplemental code. It is intended to showcase sketch-based FL research rather than serve as a standalone software package. Feel free to adapt the concepts and code snippets in your own experiments.

## Abstract

SketchFL is a framework that applies CountSketch-based compression within federated learning using OpenFL. By sketching model weights and activations in both forward and backward passes, SketchFL reduces communication bandwidth and computation time. We handle fractional compression ratios (q >= 1.0) and support gradient reconstruction via inverse sketching. Our evaluation on an MNIST classification task with a simple MLP architecture demonstrates that at q = 6, SketchFL maintains over 95% test accuracy while offering substantial speedups.

## Overview

<img src="DoubleBlindFL_Diagram.png" alt="SketchFL Diagram" width="60%"/>

SketchFL shows how randomized numerical linear algebra techniques (CountSketch) integrate into federated learning experiments via OpenFL’s Workflow API. 

### Aggregator
1. Calculates sketched (aggregated) weights using `FedAvg` and broadcasts them along with the hash parameters.  
2. At the beginning of each round, generates fresh hash parameters (i.e., sketching matrix S).  
3. Never sees the full weights from the collaborators.

### Collaborator
1. Uses the hash parameters shared by the aggregator to compress the private input data.  
2. Calculates sketched weights through local training using compressed weight gradients and shares with the server.  
3. Never sees the full aggregated weights from the aggregator.

Included are:

- **Code Snippets:** Python modules for CountSketch utilities and a `SketchLinear` PyTorch layer.
- **Notebook Examples:** Jupyter notebooks illustrating sketch-based federated learning on MNIST with an MLP.
- **Configuration Guides:** Instructions for integrating SketchFL into an OpenFL workflow.

> **Note:** Current examples focus on an MLP architecture on the MNIST dataset, demonstrating feasibility of sketch-based compression in federated learning.

## Running the Experiment

Generally, OpenFL's workflow interface can be run entirely as a Jupyter Notebook, but you may wish to call out any special instructions, especially if you introduced any unique customizations.

## Results

[Summarize the key findings of the research. You may want to include any relevant charts, graphs, or tables that illustrate the results. You may also provide links to additional resources or publications related to the project.]

## License

[Indicate any licenses]

## Acknowledgments

[Recognize any individuals, organizations, or funding sources that contributed to the research.]

## Citation

The core sketching methodology implemented in SketchFL is based on the following publication:
```latex
@inproceedings{zhang2021matrix, 
title={Matrix sketching for secure collaborative machine learning}, 
author={Zhang, Mengjiao and Wang, Shusen}, 
booktitle={International Conference on Machine Learning}, 
pages={12589--12599}, 
year={2021}, 
organization={PMLR}}