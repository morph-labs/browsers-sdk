BASE_URL ?= https://browsers.svc.stage.morph.so

generate-python-sdk:
	wget $(BASE_URL)/openapi.json -O fern/openapi.json
	fern generate --group python-sdk --force

generate-ts-sdk:
	wget $(BASE_URL)/openapi.json -O fern/openapi.json
	fern generate --group ts-sdk --force