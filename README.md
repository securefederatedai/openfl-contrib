<div align="center">
  <img src="https://github.com/securefederatedai/artwork/blob/main/PNG/OpenFL%20Logo%20-%20color.png?raw=true" width="70%">
</div>

<div align="center">
	
[<img src="https://img.shields.io/badge/slack-@openfl-blue.svg?logo=slack">](https://join.slack.com/t/openfl/shared_invite/zt-ovzbohvn-T5fApk05~YS_iZhjJ5yaTw) 

[**Overview**](#overview)
| [**Installation**](#installation)
| [**Directory Structure**](#directory-structure)
| [**Contributing**](#contributing)
| [**License**](#license)
| [**Citation**](#citation)

</div>

# openfl-contrib: OpenFL community contributions

Repository for academic and research contributions to OpenFL.

## Overview

The `openfl-contrib` repository is dedicated to fostering academic and research contributions to the OpenFL framework. It serves as a collaborative space for researchers, developers, and enthusiasts to share their work, ideas, and innovations in the field of federated learning. Contributions can include new algorithms, enhancements, experimental features, research tutorials, and more.

OpenFL is a Python framework for Federated Learning, enabling organizations to train and validate machine learning models on sensitive data without sharing it with a central server. This contrib repository aims to expand the capabilities of OpenFL by integrating cutting-edge research and development efforts.

## Installation
Installing from source. This will also pull in the latest development branch of OpenFL. Follow these steps:

```bash
git clone https://github.com/securefederatedai/openfl-contrib.git
cd openfl-contrib
pip install -e .
```

## Directory Structure

This repository is organized into several directories, each serving a specific purpose. Here's a brief overview to help you navigate:

- **openfl_contrib**: This directory mirrors the core OpenFL source files and is intended for framework-level contributions. If you're looking to extend or modify the OpenFL framework itself, this is where your contributions should reside.

- **openfl_contrib_tutorials**: A flexible space for community tutorials. Whether you're sharing a simple example or a comprehensive guide, this directory is designed to host tutorials that help users understand and utilize OpenFL and its contrib features.

- **openfl_contrib_workspace**: Contains workspaces that can be run with OpenFL's TaskRunner. These workspaces are set up for federated learning experiments and can be customized to fit various use cases. For more information on TaskRunner, refer to the [TaskRunner documentation](https://openfl.readthedocs.io/en/latest/about/features_index/taskrunner.html).

- **research**: Intended for researchers to host their work. This directory provides a space for sharing experimental code, datasets, and results related to federated learning research.

For detailed information on how to contribute to each section, please refer to the contributing guidelines.

## Contributing

We welcome contributions from the community! Whether you're a researcher, developer, or enthusiast, your input is valuable. Please refer to the [contributing guidelines](CONTRIBUTING.md) for more information on how to get involved.

Join our [Slack channel](https://join.slack.com/t/openfl/shared_invite/zt-ovzbohvn-T5fApk05~YS_iZhjJ5yaTw) to connect with other contributors, share knowledge, and collaborate on advancing federated learning.

Stay updated by subscribing to the OpenFL mailing list: [openfl-announce@lists.lfaidata.foundation](mailto:openfl-announce@lists.lfaidata.foundation).

## License

This project is licensed under the [Apache License Version 2.0](LICENSE). By contributing to the project, you agree to the license and copyright terms therein and release your contribution under these terms.

## Citation

If you use OpenFL or contributions from this repository in your research, please consider citing the following:

```
@article{openfl_citation,
	author={Foley, Patrick and Sheller, Micah J and Edwards, Brandon and Pati, Sarthak and Riviera, Walter and Sharma, Mansi and Moorthy, Prakash Narayana and Wang, Shi-han and Martin, Jason and Mirhaji, Parsa and Shah, Prashant and Bakas, Spyridon},
	title={OpenFL: the open federated learning library},
	journal={Physics in Medicine \& Biology},
	url={http://iopscience.iop.org/article/10.1088/1361-6560/ac97d9},
	year={2022},
	doi={10.1088/1361-6560/ac97d9},
	publisher={IOP Publishing}
}
```