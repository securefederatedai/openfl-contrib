import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class DigitRecognizerCNN(nn.Module):

    def __init__(self, **kwargs):
        super(DigitRecognizerCNN, self).__init__(**kwargs)
        self.conv1 = nn.Conv2d(1, 20, 2, 1)
        self.conv2 = nn.Conv2d(20, 50, 5, 1)
        self.fc1 = nn.Linear(800, 500)
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 800)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x

def train(model, optimizer, loss_fn, dataloader, device="cpu", epochs=1):
    for epoch in range(epochs):
        print(f"Starting epoch {epoch + 1}/{epochs}")
        average_loss = train_epoch(model, optimizer, loss_fn, dataloader, device)
        print(f"Completed epoch {epoch + 1}/{epochs} with average loss: {average_loss}")

    return average_loss

def validate(model, test_dataloader, device="cpu"):
    total_correct = 0
    total_samples = 0

    for data, target in test_dataloader:
        data = torch.as_tensor(data).to(device)
        target = torch.as_tensor(target).to(device)
        output = model(data)
        pred = output.argmax(dim=1, keepdim=True)
        total_correct += pred.eq(target.view_as(pred)).sum().item()
        total_samples += len(target)

    return total_correct / total_samples

def train_epoch(model, optimizer, loss_fn, dataloader, device="cpu"):
    total_loss = 0
    num_batches = 0
    for data, target in dataloader:
        data = torch.as_tensor(data).to(device)
        target = torch.as_tensor(target).to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.detach().cpu().item()
        num_batches += 1
    average_loss = total_loss / num_batches

    return average_loss
