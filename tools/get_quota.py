from typing import Any, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from .seventeentrack_client import SeventeenTrackClient


class GetQuotaTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        client = SeventeenTrackClient(
            self.runtime.credentials["seventeen_track_api_key"]
        )
        result = client.get_quota()
        for key, value in result.items():
            yield self.create_variable_message(key, value)
        yield self.create_json_message(result)
