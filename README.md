# Browsers SDK

SDKs for the Morph Browsers service generated from OpenAPI via Fern.

## Install (Python)

Use directly from Git for now (until published):

```
uv add "browsers-sdk @ git+https://github.com/morph-labs/browsers-sdk.git@main#subdirectory=sdks/python"
```

## Generate SDKs

```
BASE_URL ?= https://browsers.svc.cloud.morph.so
make generate-python-sdk
```

This will fetch the OpenAPI from the running service and generate clients into `sdks/python` and `sdks/typescript` (configurable in `fern/generators.yml`).

