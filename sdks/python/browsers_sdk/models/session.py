from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    """
    Attributes:
        id (str):
        name (str):
        vcpus (int):
        memory (int):
        disk_size (int):
        cdp_url (str):
        connect_url (str):
    """

    id: str
    name: str
    vcpus: int
    memory: int
    disk_size: int
    cdp_url: str
    connect_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vcpus = self.vcpus

        memory = self.memory

        disk_size = self.disk_size

        cdp_url = self.cdp_url

        connect_url = self.connect_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "vcpus": vcpus,
                "memory": memory,
                "disk_size": disk_size,
                "cdp_url": cdp_url,
                "connect_url": connect_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        vcpus = d.pop("vcpus")

        memory = d.pop("memory")

        disk_size = d.pop("disk_size")

        cdp_url = d.pop("cdp_url")

        connect_url = d.pop("connect_url")

        session = cls(
            id=id,
            name=name,
            vcpus=vcpus,
            memory=memory,
            disk_size=disk_size,
            cdp_url=cdp_url,
            connect_url=connect_url,
        )

        session.additional_properties = d
        return session

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
