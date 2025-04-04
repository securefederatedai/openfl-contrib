# Contributing

`openfl-contrib` is an extension of [OpenFL](https://github.com/securefederatedai/openfl). It serves as a staging ground for new features that may eventually be upstreamed to OpenFL or as a home to host experimental features, research code, tutorials, and more. This repository is organized into several directories, each serving a specific purpose:

- **openfl_contrib**: Framework-level contributions that mirror the core OpenFL source files.
- **openfl_contrib_tutorials**: A flexible space for community tutorials.
- **openfl_contrib_workspace**: Workspaces for federated learning experiments using OpenFL's TaskRunner.
- **research**: A space for researchers to host their work.

We welcome contributions from the community. There are several ways to contribute:

* Improvements in documentation
* New tutorials and demos
* Contributing to OpenFL-contrib's code-base via bug-fixes or feature additions
* Participating in the upstream OpenFL's [roadmap](https://github.com/securefederatedai/openfl/blob/develop/ROADMAP.md) discussions

Join the [\#openfl-contrib channel](https://join.slack.com/t/openfl/shared_invite/zt-ovzbohvn-T5fApk05~YS_iZhjJ5yaTw) in the OpenFL Slack to get in touch quickly with the development and maintainer team. We are happy to answer questions and provide guidance if you're interested in contributing to a particular area.

## How to contribute code

### openfl_contrib

This directory requires the most rigorous process, as contributions here intended to directly extend and enhance the OpenFL framework:

1. **Open an Issue**: Before making any changes, open an [issue](https://github.com/securefederatedai/openfl-contrib/issues) to discuss your proposed changes. This helps ensure alignment with the project's goals and prevents duplication of effort.

2. **Fork and Develop**: Fork the repository and set up a development environment. Make your changes in a feature branch.

3. **Testing**: Ensure your changes are thoroughly tested.

4. **Create a Pull Request (PR)**: Open a PR from your feature branch to the `main` branch. Follow standard PR formatting guidelines.

5. **Code Review**: We will review your PR and provide feedback.

6. **Sign Your Work**: Sign off your commits.

### openfl_contrib_tutorials

This directory is more flexible, focusing on educational content:

1. **Open an Issue (Optional)**: For substantial tutorials, consider opening an issue to outline your plan.

2. **Fork and Develop Your Tutorial**: Create your tutorial in a new directory or file within `openfl_contrib_tutorials`.

3. **Create a Pull Request (PR)**: Open a PR to add your tutorial. Include a brief description of its purpose and any prerequisites.

4. **Review and Feedback**: Your tutorial will be reviewed for clarity and accuracy.

### openfl_contrib_workspace

Contributions here involve setting up workspaces to run with OpenFL's Task Runner API:

1. **Open an Issue**: Describe the workspace you intend to create and its intended use case.

2. **Fork and Develop Your Workspace**: Set up the workspace with necessary configurations and scripts.

3. **Testing**: Run tests to ensure the workspace functions as expected.

4. **Create a Pull Request (PR)**: Submit your workspace via a PR. Include documentation on how to use it.

5. **Review and Feedback**: Your workspace will be reviewed for functionality and usability.

### research

This directory is intended for sharing research work:

1. **Open an Issue (Optional)**: If your research involves substantial code or data, consider opening an issue to discuss its scope.

2. **Fork and Develop Your Research Space**: Add your research code, datasets, and documentation. Use the [template](https://github.com/securefederatedai/openfl-contrib/tree/main/research/template) for guidance.

3. **Create a Pull Request (PR)**: Submit your research work via a PR. Include a summary of your research and any relevant publications.

4. **Review and Feedback**: Your contribution will be reviewed for relevance and completeness.

## Setup environment

We recommend setting up a local dev environment. Clone your forked repo to your local machine and install the dependencies.

```shell
git clone https://github.com/YOUR_GITHUB_USERNAME/openfl-contrib.git
cd openfl-contrib
pip install -U pip setuptools wheel
pip install .
pip install -r linters-requirements.txt