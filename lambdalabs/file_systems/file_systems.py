from typing import List


class FileSystem:
    """A file-system model class"""

    def __init__(self,
                 id: str,
                 name: str,
                 created: str,
                 created_by: dict,
                 mount_point: str,
                 region: dict,
                 is_in_use: bool,
                 bytes_used: int
                 ) -> None:
        """Initialize the file-system object

        :param id: file-system id
        :type id: str
        :param name: file-system name
        :type name: str
        :param created: file-system created date
        :type created: str
        :param created_by: file-system created by
        :type created_by: dict
        :param mount_point: file-system mount point
        :type mount_point: str
        :param region: file-system region
        :type region: dict
        :param is_in_use: file-system in use
        :type is_in_use: bool
        :param bytes_used: file-system bytes used
        :type bytes_used: int
        """
        self._id = id
        self._name = name
        self._created = created
        self._created_by = created_by
        self._mount_point = mount_point
        self._region = region
        self._is_in_use = is_in_use
        self._bytes_used = bytes_used

    @property
    def id(self) -> str:
        """Get the file-system id

        :return: file-system id
        :rtype: str
        """
        return self._id

    @property
    def name(self) -> str:
        """Get the file-system name

        :return: file-system name
        :rtype: str
        """
        return self._name

    @property
    def created(self) -> str:
        """Get the file-system created date

        :return: file-system created date
        :rtype: str
        """
        return self._created

    @property
    def created_by(self) -> dict:
        """Get the file-system created by

        :return: file-system created by
        :rtype: dict
        """
        return self._created_by

    @property
    def mount_point(self) -> str:
        """Get the file-system mount point

        :return: file-system mount point
        :rtype: str
        """
        return self._mount_point

    @property
    def region(self) -> dict:
        """Get the file-system region

        :return: file-system region
        :rtype: dict
        """
        return self._region

    @property
    def is_in_use(self) -> bool:
        """Get the file-system in use

        :return: file-system in use
        :rtype: bool
        """
        return self._is_in_use

    @property
    def bytes_used(self) -> int:
        """Get the file-system bytes used

        :return: file-system bytes used
        :rtype: int
        """
        return self._bytes_used

    def __str__(self) -> str:
        """Print the ssh-key object

        :return: ssh-key string representation
        :rtype: str
        """
        return (f'id: {self._id}\n'
                f'name: {self._name}\n'
                f'created: {self._created}\n'
                f'created_by: {self._created_by}\n'
                f'mount_point: {self._mount_point}\n'
                f'region: {self._region}\n'
                f'is_in_use: {self._is_in_use}\n'
                f'bytes_used: {self._bytes_used}\n'
                )


class FileSystemsService:
    """A service for interacting with the file systems endpoint"""

    def __init__(self, http_client) -> None:
        self._http_client = http_client

    def get(self) -> List[FileSystem]:
        """Retrieve the list of file systems

        :return: list of file-system objects
        :rtype: List[FileSystem]
        """
        file_systems_dict = self._http_client.get('/file-systems').json()
        file_system_objects = list(map(lambda file_systems_dict: FileSystem(
            id=file_systems_dict['id'],
            name=file_systems_dict['name'],
            created=file_systems_dict['created'],
            created_by=file_systems_dict['created_by'],
            mount_point=file_systems_dict['mount_point'],
            region=file_systems_dict['region'],
            is_in_use=file_systems_dict['is_in_use'],
            bytes_used=file_systems_dict['bytes_used'],
        ), file_systems_dict['data']))
        return file_system_objects
