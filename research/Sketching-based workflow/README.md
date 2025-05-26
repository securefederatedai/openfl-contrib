# SketchFL: Federated Learning via Matrix Sketching

Welcome to **SketchFL**, a research contribution to the OpenFL community. This project explores **integrating sketch-based compression into federated learning workflows**, using OpenFL's experimental Workflow API to accelerate both training and inference while reducing communication overhead. 

> **Note:** This document describes the SketchFL methodology and supplemental code. It is intended to showcase sketch-based FL research rather than serve as a standalone software package. Feel free to adapt the concepts and code snippets in your own experiments.

## Abstract

We introduce SketchFL, a framework that applies CountSketch-based compression within federated learning using OpenFL. By sketching model weights and activations in both forward and backward passes, SketchFL reduces communication bandwidth and computation time. We handle fractional compression ratios (q >= 1.0) and support gradient reconstruction via inverse sketching. Our evaluation on an MNIST classification task with a simple MLP architecture demonstrates that at q = 6, SketchFL maintains over 98% test accuracy while offering substantial speedups.

## Overview

SketchFL shows how randomized numerical linear algebra techniques (CountSketch) integrate into federated learning experiments via OpenFL’s Workflow API. Included are:

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

If you find this project useful in your research, please consider citing our work:
```latex
@inproceedings{
author={Your Name and Collaborators},
title={Project Title},
booktitle={Conference or Journal Name},
year={Year},
url={Link to publication}
}