# Federated Discrete Denoising Diffusion Model for Molecular Generation with OpenFL

[arXiv](https://arxiv.org/abs/2501.12523)

## Abstract

Generating unique molecules with biochemically desired properties to serve as viable drug candidates is a difficult task that requires specialized domain expertise. In recent years, diffusion models have shown promising results in accelerating the drug design process through AIdriven molecular generation. However, training these models requires massive amounts of data, which are often isolated in proprietary silos. OpenFL is a federated learning framework that enables privacy-preserving collaborative training across these decentralized data sites. In this work, we present a federated discrete denoising diffusion model that was trained using OpenFL. The federated model achieves comparable performance with a model trained on centralized data when evaluating the uniqueness and validity of the generated molecules. This demonstrates the utility of federated learning in the drug design process



## Citation

If you find this project useful in your research, please consider citing our work:
```latex
@misc{
ta2025federateddiscretedenoisingdiffusion,
title={Federated Discrete Denoising Diffusion Model for Molecular Generation with OpenFL}, 
author={Kevin Ta and Patrick Foley and Mattson Thieme and Abhishek Pandey and Prashant Shah},
year={2025},
eprint={2501.12523},
archivePrefix={arXiv},
primaryClass={cs.LG},
url={https://arxiv.org/abs/2501.12523}, 
}