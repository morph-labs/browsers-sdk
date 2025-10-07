from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_list import SessionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    replicas: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["replicas"] = replicas

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/session/{id}/branch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SessionList]]:
    if response.status_code == 200:
        response_200 = SessionList.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, SessionList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    replicas: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, SessionList]]:
    """Branch Session

     Branch an existing session into N replicas.

    Each branched session receives a new `browsers:id` while inheriting the
    parent's recording state via a shared `browsers:recording_id`.

    Args:
        id (str):
        replicas (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SessionList]]
    """

    kwargs = _get_kwargs(
        id=id,
        replicas=replicas,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    replicas: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, SessionList]]:
    """Branch Session

     Branch an existing session into N replicas.

    Each branched session receives a new `browsers:id` while inheriting the
    parent's recording state via a shared `browsers:recording_id`.

    Args:
        id (str):
        replicas (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SessionList]
    """

    return sync_detailed(
        id=id,
        client=client,
        replicas=replicas,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    replicas: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, SessionList]]:
    """Branch Session

     Branch an existing session into N replicas.

    Each branched session receives a new `browsers:id` while inheriting the
    parent's recording state via a shared `browsers:recording_id`.

    Args:
        id (str):
        replicas (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SessionList]]
    """

    kwargs = _get_kwargs(
        id=id,
        replicas=replicas,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    replicas: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, SessionList]]:
    """Branch Session

     Branch an existing session into N replicas.

    Each branched session receives a new `browsers:id` while inheriting the
    parent's recording state via a shared `browsers:recording_id`.

    Args:
        id (str):
        replicas (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SessionList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            replicas=replicas,
        )
    ).parsed
