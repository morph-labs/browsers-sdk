BASE_URL ?= https://browsers.svc.cloud.morph.so

generate-python-sdk:
	wget $(BASE_URL)/openapi.json -O fern/openapi.json
	fern generate --group python-sdk --force

