"""Morph Browsers SDK plugin for MorphCloud.

Provides a plugin entry point so MorphCloudClient loads a convenient
`browsers` and `browsers_async` client, mirroring the morphdb pattern.
"""

from __future__ import annotations

import os
import typing as _t

from .client import AuthenticatedClient, Client
from .api.default import (
    create_session as _create_session,
    list_sessions as _list_sessions,
    get_session as _get_session,
    stop_session as _stop_session,
)


class BrowsersApi:
    """Sync convenience wrapper for the Browsers service using the generated SDK.

    Example:
        from morphcloud.api import MorphCloudClient
        client = MorphCloudClient()
        browsers = client.browsers
        sess = browsers.create_session(name="demo")
    """

    def __init__(self, base_url: str, token: str):
        self._client = AuthenticatedClient(base_url=base_url, token=token)

    # Core endpoints
    def create_session(self, name: _t.Optional[str] = None):
        return _create_session.sync(client=self._client, name=name)

    def list_sessions(self):
        return _list_sessions.sync(client=self._client)

    def get_session(self, id: str):  # noqa: A002 (shadow builtins)
        return _get_session.sync(client=self._client, id=id)

    def stop_session(self, id: str):  # noqa: A002 (shadow builtins)
        return _stop_session.sync(client=self._client, id=id)


class AsyncBrowsersApi:
    """Async convenience wrapper for the Browsers service using the generated SDK."""

    def __init__(self, base_url: str, token: str):
        self._client = AuthenticatedClient(base_url=base_url, token=token)

    # Core endpoints
    async def create_session(self, name: _t.Optional[str] = None):
        return await _create_session.asyncio(client=self._client, name=name)

    async def list_sessions(self):
        return await _list_sessions.asyncio(client=self._client)

    async def get_session(self, id: str):  # noqa: A002
        return await _get_session.asyncio(client=self._client, id=id)

    async def stop_session(self, id: str):  # noqa: A002
        return await _stop_session.asyncio(client=self._client, id=id)


def _resolve_base_url(explicit: _t.Optional[str] = None) -> str:
    if explicit:
        return explicit
    return os.environ.get("BROWSERS_BASE_URL", "https://browsers.svc.cloud.morph.so")


def create_service_client(morph_client, browsers_base_url: _t.Optional[str] = None) -> BrowsersApi:
    """Create a sync client bound to a MorphCloud client."""
    return BrowsersApi(base_url=_resolve_base_url(browsers_base_url), token=morph_client.api_key)


def create_async_service_client(morph_client, browsers_base_url: _t.Optional[str] = None) -> AsyncBrowsersApi:
    """Create an async client bound to a MorphCloud client."""
    return AsyncBrowsersApi(base_url=_resolve_base_url(browsers_base_url), token=morph_client.api_key)


def register_sdk_plugin(morph_client) -> None:
    """Register `browsers` and `browsers_async` on MorphCloudClient.

    This function is discovered and called by MorphCloudClient via the
    `morphcloud.sdk_plugins` entry point group.
    """
    morph_client.browsers = create_service_client(morph_client)
    morph_client.browsers_async = create_async_service_client(morph_client)


__all__ = (
    "AuthenticatedClient",
    "Client",
    "BrowsersApi",
    "AsyncBrowsersApi",
    "create_service_client",
    "create_async_service_client",
    "register_sdk_plugin",
)
