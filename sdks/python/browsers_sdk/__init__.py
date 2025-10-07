"""MorphCloud Browsers Service Plugin"""

__version__ = "0.1.0"

import os
import typing
from .gen.client import MorphLabsApi, AsyncMorphLabsApi


def create_service_client(
    morph_client,
    browsers_base_url: typing.Optional[str] = None
):
    """Create a sync service client from a MorphCloud client."""
    # Set up service base URL independently
    base_url = browsers_base_url or os.environ.get(
        "BROWSERS_BASE_URL", "https://browsers.svc.cloud.morph.so"
    )
    
    return MorphLabsApi(
        token=morph_client.api_key,  # Still use the main client's API key
        base_url=base_url
    )


def create_async_service_client(
    morph_client,
    browsers_base_url: typing.Optional[str] = None
):
    """Create an async service client from a MorphCloud client."""
    # Set up service base URL independently
    base_url = browsers_base_url or os.environ.get(
        "BROWSERS_BASE_URL", "https://browsers.svc.cloud.morph.so"
    )
    
    return AsyncMorphLabsApi(
        token=morph_client.api_key,  # Still use the main client's API key
        base_url=base_url
    )


def register_sdk_plugin(morph_client):
    """Register the service client with the main MorphCloud client."""
    morph_client.browsers = create_service_client(morph_client)
    morph_client.browsers_async = create_async_service_client(morph_client)


# Aliases for backwards compatibility
BrowsersClient = MorphLabsApi
AsyncBrowsersClient = AsyncMorphLabsApi

__all__ = [
    "BrowsersClient", 
    "AsyncBrowsersClient", 
    "create_service_client", 
    "create_async_service_client",
    "register_sdk_plugin"
]