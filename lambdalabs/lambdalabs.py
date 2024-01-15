from lambdalabs.http_client.http_client import HTTPClient
from lambdalabs.instance_types.instance_types import InstanceTypesService
from lambdalabs.instances.instances import InstancesService
from lambdalabs.ssh_keys.ssh_keys import SSHKeysService
from lambdalabs.file_systems.file_systems import FileSystemsService


class LambdaLabsClient:
    """Client for interacting with Lambda Labs's public API"""

    def __init__(self, api_key: str, base_url: str = "https://cloud.lambdalabs.com/api/v1") -> None:
        """The Lambda Labs client

        :param api_key: API key
        :type api_key: str
        :param base_url: base url for all the endpoints, optional, defaults to "https://cloud.lambdalabs.com/api/v1"
        :type base_url: str, optional
        """
        self._http_client: HTTPClient = HTTPClient(api_key, base_url=base_url)
        self.instance_types: InstanceTypesService = InstanceTypesService(self._http_client)
        self.instances: InstancesService = InstancesService(self._http_client)
        self.ssh_keys: SSHKeysService = SSHKeysService(self._http_client)
        self.file_systems: FileSystemsService = FileSystemsService(self._http_client)
