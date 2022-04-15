# edi-ci-cd

Continuous integration and delivery for edi project configurations based on GitHub actions.

Note: edi-ci-cd is a private GitHub repository as it is interfacing with GitHub action runners.
edi-ci-cd-public is a clone of edi-ci-cd and makes the content visible for a broader audience.

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
