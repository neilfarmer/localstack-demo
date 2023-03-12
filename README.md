# localstack-demo

## Getting Started

This repo shows an example of using vscode tasks (.vscode/tasks.json) and localstack (terraform/python).
I did this cause I wanted to use both of them in a project. Tis pretty cool stuffs

Requirements: - python3 - docker

### Setup

#### Download repo

```bash
git clone git@github.com:neilfarmer/localstack-demo.git
```

#### Using vscode, run the `install-dependencies` task

But if that doesnt work:

```bash
pip install --upgrade pip poetry; poetry install
```

#### Using vscode, run the `build-localstack` task

But if that doesnt work:

```bash
poetry run localstack start -d; poetry run localstack status services; poetry run localstack status
```

This will build localstack in docker and provide its status

### Testing with python

#### Using vscode, run the `run-python` task

But if that doesnt work:

```bash
poetry install; poetry run python localstack-python/s3_test.py
```

```bash
poetry install; poetry run tflocal init; poetry run tflocal -chdir=localstack-terraform apply -auto-approve
```

You can see the API calls for this apply in localstack via the `localstack-logs` task

```bash
poetry run localstack logs
```

### Testing with terraform

#### Using vscode, run the `run-terraform-plan` task

But if that doesnt work:

```bash
poetry install; poetry run tflocal -chdir=localstack-terraform init; poetry run tflocal -chdir=localstack-terraform plan
```

Then run the `run-terraform-apply` task

```bash
poetry install; poetry run tflocal init; poetry run tflocal -chdir=localstack-terraform apply -auto-approve
```

You can see the API calls for this apply in localstack via the `localstack-logs` task

But if that doesnt work:

```bash
poetry run localstack logs
```

## Cleanup

Run the task `teardown-localstack`

But if that doesnt work:

```bash
poetry run localstack stop
```

Yer done brah...
