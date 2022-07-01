# edi-ci

Continuous integration for edi project configurations based on GitHub actions.

Currently edi-ci is capable of

- building OS images based on an edi project configuration
- dispatching the OS images to embedded devices
- testing the dispatched OS images on the embedded devices


Note: edi-ci is a private GitHub repository as it is interfacing with GitHub action runners.
edi-ci-public is a clone of edi-ci and makes the content visible for a broader audience.

## Run Tests Locally

``` bash
export MENDER_USER=MY_MENDER_LOGIN
export MENDER_PASSWORD=MY_MENDER_PASSWORD
export DEVICE_SECRETS="$(cat config/device_secrets_sample.json)"
./run-tests MENDER_DEVICE_ID EDI_PROJECT_CONFIGURATION
```

## Secrets on GitHub


`CI_CD_SSH_PUB_KEY`: ssh public key of the user that wants to easily access the CI/CD devices (optional)

`DEVICE_SECRETS`: check `config/device_secrets_sample.json` for an example json

`MENDER_TENANT_TOKEN`: the token of your hosted Mender tenant

`MENDER_USER`: the Mender user (e-mail)

`MENDER_PASSWORD`: the Mender password

## More Information

This [blog post](https://www.get-edi.io/Building-and-Testing-OS-Images-with-GitHub-Actions/) describes
the setup of the CI pipeline.
