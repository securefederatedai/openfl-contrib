import torch
import torchvision
import torch.nn.functional as F
from torchvision.transforms import ToTensor
import torch.optim as optim

from cnn_model import DigitRecognizerCNN, train, validate

if __name__ == '__main__':
    model = DigitRecognizerCNN()

    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    loss_fn = F.cross_entropy

    data_train = torchvision.datasets.MNIST('./data', download=True, train=True, transform=ToTensor())
    data_test = torchvision.datasets.MNIST('./data', download=True, train=False, transform=ToTensor())

    train_data_loader = torch.utils.data.DataLoader(data_train, batch_size=64)
    test_data_loader = torch.utils.data.DataLoader(data_test, batch_size=64)

    train(model, optimizer, loss_fn, train_data_loader, epochs=1)
    acc = validate(model, test_data_loader)

    print(f"Digit recognizer accuracy: {acc}")
