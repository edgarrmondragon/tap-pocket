"""Pocket tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_pocket.streams import Items

STREAM_TYPES = [
    Items,
]


class TapPocket(Tap):
    """Pocket tap class."""

    name = "tap-pocket"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "consumer_key",
            th.StringType,
            required=True,
            description="Pocket application key",
        ),
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            description="Pocket user access token",
        ),
        th.Property(
            "start_date",
            th.StringType,
            description="The earliest record datetime to sync as a UNIX timestamp",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of all the streams discovered for this tap.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
