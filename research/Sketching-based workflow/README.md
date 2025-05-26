# SketchFL: Federated Learning via Matrix Sketching

Welcome to **SketchFL**, a research contribution to the OpenFL community. This project explores **integrating sketch-based compression into federated learning workflows**, using OpenFL's experimental Workflow API to accelerate both training and inference while reducing communication overhead. Additionally, the framework adds a basic level of privacy by obfuscating the original (high-dimensional) model updates through sketching.

> **Note:** This document describes the SketchFL methodology and supplemental code. It is intended to showcase sketch-based FL research rather than serve as a standalone software package. Feel free to adapt the concepts and code snippets in your own experiments.

## Abstract

SketchFL is a framework that applies CountSketch-based compression within federated learning using OpenFL. By sketching model weights and activations in both forward and backward passes, SketchFL reduces communication bandwidth and computation time. We handle fractional compression ratios (q >= 1.0) and support gradient reconstruction via inverse sketching. Our evaluation on an MNIST classification task with a simple MLP architecture demonstrates that at q = 6, SketchFL maintains over 95% test accuracy while offering substantial speedups.

## Sketching Primer

Before diving into the code, here is a high‐level overview of CountSketch without heavy math:

1. **Goal:**  
   Reduce a long vector of numbers (length n) to a much shorter “sketch” (length m) so it’s faster to send over the network.

2. **How it works:**  
   - **Bucket assignment:** Each entry in the original vector is assigned to one of m buckets via a simple hash function.  
   - **Random sign flip:** Before adding, each entry is multiplied by either +1 or –1 at random.  
   - **Bucket summation:** For each bucket, sum up all the signed values that were hashed there. The result is your sketch of length m.

3. **Key properties:**  
   - **Unbiased:** On average, the sketch value for each bucket equals the sum of all original entries that fell into it.  
   - **Mergeable:** You can add together two sketches to get the sketch of the sum of the original data—perfect for federated averaging.  
   - **Invertible (approximately):** With a little extra work, you can map back from the sketch to an approximate version of the original vector (used during back‐propagation).

4. **Other benefits:**  
   - **Low memory footprint:** Stores only m numbers instead of n.  
   - **Fast computation:** Hash and summation operations are very cheap.  
   - **Privacy boost:** Random sign flipping and hashing obscure individual values, adding a layer of data protection.

5. **In SketchFL:**  
   - We sketch both the model weights and the layer activations during training.  
   - The server and clients only exchange the short sketches, cutting down bandwidth.  
   - A lightweight “inverse sketch” step recovers approximate gradients for updating full‐size weights locally.  


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

<!-- Included are:

- **Code Snippets:** Python modules for CountSketch utilities and a `SketchLinear` PyTorch layer.
- **Notebook Examples:** Jupyter notebooks illustrating sketch-based federated learning on MNIST with an MLP.
- **Configuration Guides:** Instructions for integrating SketchFL into an OpenFL workflow. -->

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