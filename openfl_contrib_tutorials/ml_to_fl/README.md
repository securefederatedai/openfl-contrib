# From Centralized Machine Learning to Federated Learning with OpenFL

This folder contains the artefacts referenced by a blog post published [here](https://medium.com/openfl/from-centralized-machine-learning-to-federated-learning-with-openfl-b3e61da52432), walking through the steps for transitioning from a centrally-trained model to a federated learning setting.

The code samples can be executed independently of the blog post by following the instructions in this document.
It is recommended to do so in a Python virtual environment:
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

## Training the model centrally

```bash
cd ./central
pip install -r requirements.txt

python train.py
```

## Running the federated workspace

The first step is to install OpenFL (v1.6 from PyPi being the latest release as of the time of writing):
```bash
cd ./federated
pip install openfl==1.6
```

Initialize the workspace and prepare the dataset shards:
```bash
fx plan initialize --input_shape [1,28,28] --aggregator_address localhost
tar -xvf mnist_data_shards.tar.gz
```

Next, we need to prepare a local PKI setup, and register the data sets for the experiment:
```bash
# This will create a local certificate authority (CA), so the participants communicate over a secure TLS Channel
fx workspace certify

#################################################################
# Step 2: Setup the Aggregator #
#################################################################

# Generate a Certificate Signing Request (CSR) for the Aggregator
fx aggregator generate-cert-request --fqdn localhost

# The CA signs the aggregator's request, which is now available in the workspace
fx aggregator certify --fqdn localhost --silent

################################
# Step 3: Setup Collaborator 1 #
################################

# Create a collaborator named "collaborator1" that will use data path "data/1"
# This command adds the collaborator2,data/2 entry in data.yaml
fx collaborator create -n collaborator1 -d data/1

# Generate a CSR for collaborator1
fx collaborator generate-cert-request -n collaborator1

# The CA signs collaborator1's certificate, adding an entry to cols.yaml
fx collaborator certify -n collaborator1 --silent

################################
# Step 4: Setup Collaborator 2 #
################################

# Create a collaborator named "collaborator2" that will use data path "data/2"
# This command adds the collaborator2,data/2 entry in data.yaml
fx collaborator create -n collaborator2 -d data/2

# Generate a CSR for collaborator2
fx collaborator generate-cert-request -n collaborator2

# The CA signs collaborator2's certificate, adding an entry to cols.yaml
fx collaborator certify -n collaborator2 --silent
```

We are now ready to simulate the full FL experiment locally:
```bash
fx aggregator start & fx collaborator start -n collaborator1 & fx collaborator start -n collaborator2
```

A successful run concludes with the "End of Federation reached" log from each collaborator:
```bash
INFO     Round: 1, Collaborators that have completed all tasks: ['collaborator2', 'collaborator1']
    METRIC   {'metric_origin': 'aggregator', 'task_name': 'aggregated_model_validation', 'metric_name': 'accuracy', 'metric_value':
              0.8915090382660382, 'round': 1}
    METRIC   Round 1: saved the best model with score 0.891509
    METRIC   {'metric_origin': 'aggregator', 'task_name': 'train', 'metric_name': 'training loss', 'metric_value': 0.2952194180338876,
              'round': 1}
    METRIC   {'metric_origin': 'aggregator', 'task_name': 'locally_tuned_model_validation', 'metric_name': 'accuracy', 'metric_value':
              0.9181734901767464, 'round': 1}
INFO     Saving round 1 model...
INFO     Experiment Completed. Cleaning up...
INFO     Waiting for tasks...
INFO     Sending signal to collaborator collaborator1 to shutdown...
INFO     End of Federation reached. Exiting...

INFO     Waiting for tasks...
INFO     Sending signal to collaborator collaborator2 to shutdown...
INFO     End of Federation reached. Exiting...
```