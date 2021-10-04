# Load testing Azure Machine Learning inference endpoints

Quick example showing how an Azure Machine Learning inference endpoint can be load tested, for example deployed to an
Azure Kubernetes Cluster or Managed Online Endpoint.

The code requires the locust package to be installed. One way to install it, is by running
`pip install --upgrade locust`. (Please note the note in the troubleshooting section, however.)

Once installed,
- adjust the `user.py` file to your needs (note the wait time!),
- then run `locust -f user.py --web-host localhost` and
- open the URL shown by locust, and
- add your parameters when the UI pops up.
    * For the Host parameter, use the Score URL of your web service, example format: https://name.region.inference.ml.azure.com/score
    * To pre-define and avoid that the values have to be given in the UI, run locust with parameters `--host` and `--aml-webservice-auth-key`.


## Troubleshooting

### Cannot install locust on Windows

The Windows package of locust seems to have a problem with Python 3.8, or in more detail: some of its used dependencies.
A workaround is to use Python 3.7 or use the package in WSL2, a Linux or Mac machine.

## Documentation

For details on Azure Machine Learning, see the documentation
[here](https://docs.microsoft.com/en-us/azure/machine-learning).

## Disclaimer
As always, everything provided here is provided "as is". Feel free to use but don't blame me if things go wrong.

I am open for pull requests. Please submit a pull request before starting your own public fork so we can keep things
together.