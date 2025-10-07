from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordingInfo")


@_attrs_define
class RecordingInfo:
    """
    Attributes:
        id (str):
        session_id (str):
        started_at (float):
        name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        ended_at (Union[None, Unset, float]):
        event_count (Union[Unset, int]):  Default: 0.
    """

    id: str
    session_id: str
    started_at: float
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    ended_at: Union[None, Unset, float] = UNSET
    event_count: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        session_id = self.session_id

        started_at = self.started_at

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ended_at: Union[None, Unset, float]
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = self.ended_at

        event_count = self.event_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session_id": session_id,
                "started_at": started_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if event_count is not UNSET:
            field_dict["event_count"] = event_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("session_id")

        started_at = d.pop("started_at")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_ended_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        event_count = d.pop("event_count", UNSET)

        recording_info = cls(
            id=id,
            session_id=session_id,
            started_at=started_at,
            name=name,
            description=description,
            ended_at=ended_at,
            event_count=event_count,
        )

        recording_info.additional_properties = d
        return recording_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
