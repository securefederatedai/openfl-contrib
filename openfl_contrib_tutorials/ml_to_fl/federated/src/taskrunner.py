# Copyright (C) 2024 Intel Corporation
# Licensed subject to the terms of the separately executed evaluation license agreement between Intel Corporation and you.

import numpy as np

from typing import Iterator, Tuple

from openfl.federated import PyTorchTaskRunner
from openfl.utilities import Metric

import torch.optim as optim
import torch.nn.functional as F
from src.cnn_model import DigitRecognizerCNN, train_epoch, validate

class TemplateTaskRunner(PyTorchTaskRunner):
    """Template Task Runner for PyTorch.

    This class should be used as a template to create a custom Task Runner for your specific model and training workload.
    After generating this template, you should:
    1. Define your model, optimizer, and loss function as you would in PyTorch. PyTorchTaskRunner inherits from torch.nn.Module.
    2. Implement the `train_` and `validate_` functions to define a single train and validate epoch of your workload.
    3. Modify the `plan.yaml` file to use this Task Runner.

    The `plan.yaml` modifications should be done under the `<workspace>/plan/plan.yaml` section:
    ```
    task_runner:
        defaults : plan/defaults/task_runner.yaml
        template: src.taskrunner.TemplateTaskRunner # Modify this line appropriately if you change the class name
        settings:
            # Add additional arguments that you wish to pass through `__init__`
    ```

    Define the `forward` method of this class as a forward pass through the model.
    """

    def __init__(self, device="cpu", **kwargs):
        """Initialize the Task Runner.

        Args:
            device: The hardware device to use for training (Default = "cpu").
            **kwargs: Additional arguments that may be defined in `plan.yaml`
        """
        super().__init__(device=device, **kwargs)

        # Define the model
        self.model = DigitRecognizerCNN()
        self.to(device)

        # Define the optimizer
        self.optimizer = optim.Adam(self.model.parameters(), lr=1e-4)

        # Define the loss function
        self.loss_fn = F.cross_entropy

    def forward(self, x):
        """Forward pass of the model.

        Args:
            x: Data input to the model for the forward pass.

        Returns:
            The output of the model's forward pass.
        """
        return self.model(x)

    def train_(
        self, train_dataloader: Iterator[Tuple[np.ndarray, np.ndarray]]
    ) -> Metric:
        """Single Training epoch.

        Args:
            train_dataloader: Train dataset batch generator. Yields (samples, targets) tuples
                              of size = `self.train_dataloader.batch_size`.

        Returns:
            Metric: An object containing the name of the metric and its value as an np.ndarray.
        """
        # Implement training logic here and return a Metric object with the training loss.
        # Replace the following placeholder with actual training code.

        loss = train_epoch(self.model, self.optimizer, self.loss_fn, train_dataloader, self.device)
        return Metric(name="training loss", value=np.array(loss))

    def validate_(
        self, validation_dataloader: Iterator[Tuple[np.ndarray, np.ndarray]]
    ) -> Metric:
        """Single validation epoch.

        Args:
            validation_dataloader: Validation dataset batch generator. Yields (samples, targets) tuples.
                                   of size = `self.validation_dataloader.batch_size`.

        Returns:
            Metric: An object containing the name of the metric and its value as an np.ndarray.
        """
        # Implement validation logic here and return a Metric object with the validation accuracy.
        # Replace the following placeholder with actual validation code.

        accuracy = validate(self.model, validation_dataloader, self.device)
        return Metric(name="accuracy", value=np.array(accuracy))
