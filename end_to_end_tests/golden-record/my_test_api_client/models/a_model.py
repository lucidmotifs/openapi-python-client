import datetime
from typing import Any, Dict, List, Optional, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.an_enum import AnEnum
from ..models.different_enum import DifferentEnum


@attr.s(auto_attribs=True)
class AModel:
    """ A Model for testing all the ways custom objects can be used  """

    an_enum_value: AnEnum
    some_dict: Optional[Dict[Any, Any]]
    a_camel_date_time: Union[datetime.datetime, datetime.date]
    a_date: datetime.date
    nested_list_of_enums: Optional[List[List[DifferentEnum]]] = None
    attr_1_leading_digit: Optional[str] = None
    a_nullable_union: Optional[Union[Optional[datetime.datetime], Optional[datetime.date]]] = None

    def to_dict(self) -> Dict[str, Any]:
        an_enum_value = self.an_enum_value.value

        some_dict = self.some_dict

        if isinstance(self.a_camel_date_time, datetime.datetime):
            a_camel_date_time = self.a_camel_date_time.isoformat()

        else:
            a_camel_date_time = self.a_camel_date_time.isoformat()

        a_date = self.a_date.isoformat()

        if self.nested_list_of_enums is None:
            nested_list_of_enums = None
        else:
            nested_list_of_enums = []
            for nested_list_of_enums_item_data in self.nested_list_of_enums:
                nested_list_of_enums_item = []
                for nested_list_of_enums_item_item_data in nested_list_of_enums_item_data:
                    nested_list_of_enums_item_item = nested_list_of_enums_item_item_data.value

                    nested_list_of_enums_item.append(nested_list_of_enums_item_item)

                nested_list_of_enums.append(nested_list_of_enums_item)

        attr_1_leading_digit = self.attr_1_leading_digit
        if self.a_nullable_union is None:
            a_nullable_union: Optional[Union[Optional[datetime.datetime], Optional[datetime.date]]] = None
        elif isinstance(self.a_nullable_union, datetime.datetime):
            a_nullable_union = self.a_nullable_union.isoformat() if self.a_nullable_union else None

        else:
            a_nullable_union = self.a_nullable_union.isoformat() if self.a_nullable_union else None

        return {
            "an_enum_value": an_enum_value,
            "some_dict": some_dict,
            "aCamelDateTime": a_camel_date_time,
            "a_date": a_date,
            "nested_list_of_enums": nested_list_of_enums,
            "1_leading_digit": attr_1_leading_digit,
            "a_nullable_union": a_nullable_union,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AModel":
        an_enum_value = AnEnum(d["an_enum_value"])

        some_dict = d["some_dict"]

        def _parse_a_camel_date_time(data: Dict[str, Any]) -> Union[datetime.datetime, datetime.date]:
            a_camel_date_time: Union[datetime.datetime, datetime.date]
            try:
                a_camel_date_time = isoparse(d["aCamelDateTime"])

                return a_camel_date_time
            except:  # noqa: E722
                pass
            a_camel_date_time = isoparse(d["aCamelDateTime"]).date()

            return a_camel_date_time

        a_camel_date_time = _parse_a_camel_date_time(d["aCamelDateTime"])

        a_date = isoparse(d["a_date"]).date()

        nested_list_of_enums = []
        for nested_list_of_enums_item_data in d.get("nested_list_of_enums") or []:
            nested_list_of_enums_item = []
            for nested_list_of_enums_item_item_data in nested_list_of_enums_item_data:
                nested_list_of_enums_item_item = DifferentEnum(nested_list_of_enums_item_item_data)

                nested_list_of_enums_item.append(nested_list_of_enums_item_item)

            nested_list_of_enums.append(nested_list_of_enums_item)

        attr_1_leading_digit = d.get("1_leading_digit")

        def _parse_a_nullable_union(
            data: Dict[str, Any]
        ) -> Optional[Union[Optional[datetime.datetime], Optional[datetime.date]]]:
            a_nullable_union: Optional[Union[Optional[datetime.datetime], Optional[datetime.date]]]
            try:
                a_nullable_union = None
                if d.get("a_nullable_union") is not None:
                    a_nullable_union = isoparse(cast(str, d.get("a_nullable_union")))

                return a_nullable_union
            except:  # noqa: E722
                pass
            a_nullable_union = None
            if d.get("a_nullable_union") is not None:
                a_nullable_union = isoparse(cast(str, d.get("a_nullable_union"))).date()

            return a_nullable_union

        a_nullable_union = None
        if d.get("a_nullable_union") is not None:
            a_nullable_union = _parse_a_nullable_union(d.get("a_nullable_union"))

        return AModel(
            an_enum_value=an_enum_value,
            some_dict=some_dict,
            a_camel_date_time=a_camel_date_time,
            a_date=a_date,
            nested_list_of_enums=nested_list_of_enums,
            attr_1_leading_digit=attr_1_leading_digit,
            a_nullable_union=a_nullable_union,
        )
