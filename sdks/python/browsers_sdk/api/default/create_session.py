from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session import Session
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[None, Unset, str] = UNSET,
    viewport_width: Union[None, Unset, int] = 1280,
    viewport_height: Union[None, Unset, int] = 720,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_name: Union[None, Unset, str]
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_viewport_width: Union[None, Unset, int]
    if isinstance(viewport_width, Unset):
        json_viewport_width = UNSET
    else:
        json_viewport_width = viewport_width
    params["viewport_width"] = json_viewport_width

    json_viewport_height: Union[None, Unset, int]
    if isinstance(viewport_height, Unset):
        json_viewport_height = UNSET
    else:
        json_viewport_height = viewport_height
    params["viewport_height"] = json_viewport_height

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Session]]:
    if response.status_code == 200:
        response_200 = Session.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Session]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[None, Unset, str] = UNSET,
    viewport_width: Union[None, Unset, int] = 1280,
    viewport_height: Union[None, Unset, int] = 720,
) -> Response[Union[HTTPValidationError, Session]]:
    """Create Session

     Create a new browser session.

    If resource limits are reached, return an existing session for the user
    instead of failing with 500.

    Args:
        name (Union[None, Unset, str]):
        viewport_width (Union[None, Unset, int]):  Default: 1280.
        viewport_height (Union[None, Unset, int]):  Default: 720.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Session]]
    """

    kwargs = _get_kwargs(
        name=name,
        viewport_width=viewport_width,
        viewport_height=viewport_height,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[None, Unset, str] = UNSET,
    viewport_width: Union[None, Unset, int] = 1280,
    viewport_height: Union[None, Unset, int] = 720,
) -> Optional[Union[HTTPValidationError, Session]]:
    """Create Session

     Create a new browser session.

    If resource limits are reached, return an existing session for the user
    instead of failing with 500.

    Args:
        name (Union[None, Unset, str]):
        viewport_width (Union[None, Unset, int]):  Default: 1280.
        viewport_height (Union[None, Unset, int]):  Default: 720.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Session]
    """

    return sync_detailed(
        client=client,
        name=name,
        viewport_width=viewport_width,
        viewport_height=viewport_height,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[None, Unset, str] = UNSET,
    viewport_width: Union[None, Unset, int] = 1280,
    viewport_height: Union[None, Unset, int] = 720,
) -> Response[Union[HTTPValidationError, Session]]:
    """Create Session

     Create a new browser session.

    If resource limits are reached, return an existing session for the user
    instead of failing with 500.

    Args:
        name (Union[None, Unset, str]):
        viewport_width (Union[None, Unset, int]):  Default: 1280.
        viewport_height (Union[None, Unset, int]):  Default: 720.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Session]]
    """

    kwargs = _get_kwargs(
        name=name,
        viewport_width=viewport_width,
        viewport_height=viewport_height,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[None, Unset, str] = UNSET,
    viewport_width: Union[None, Unset, int] = 1280,
    viewport_height: Union[None, Unset, int] = 720,
) -> Optional[Union[HTTPValidationError, Session]]:
    """Create Session

     Create a new browser session.

    If resource limits are reached, return an existing session for the user
    instead of failing with 500.

    Args:
        name (Union[None, Unset, str]):
        viewport_width (Union[None, Unset, int]):  Default: 1280.
        viewport_height (Union[None, Unset, int]):  Default: 720.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Session]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
        )
    ).parsed
