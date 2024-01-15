from typing import List


class SSHKey:
    """An ssh-key model class"""

    def __init__(self,
                 id: str,
                 name: str,
                 public_key: str,
                 private_key: str = None
                 ) -> None:
        """Initialize the ssh-key object

        :param id: ssh-key ud
        :type id: str
        :param name: ssh-key name
        :type name: str
        :param public_key: ssh-key public key
        :type public_key: str
        :param private_key: ssh-key private key
        :type private_key: str, optional
        """
        self._id = id
        self._name = name
        self._public_key = public_key
        self._private_key = private_key

    @property
    def id(self) -> str:
        """Get the ssh-key id

        :return: ssh-key id
        :rtype: str
        """
        return self._id

    @property
    def name(self) -> str:
        """Get the ssh-key name

        :return: ssh-key name
        :rtype: str
        """
        return self._name

    @property
    def public_key(self) -> str:
        """Get the ssh public key

        :return: ssh public key
        :rtype: str
        """
        return self._public_key

    @property
    def private_key(self) -> str:
        """Get the ssh private key

        :return: ssh private key
        :rtype: str
        """
        return self._private_key

    def __str__(self) -> str:
        """Print the ssh-key object

        :return: ssh-key string representation
        :rtype: str
        """
        return (f'id: {self._id}\n'
                f'name: {self._name}\n'
                f'public_key: {self._public_key}\n'
                f'private_key: {self._private_key}\n'
                )


class SSHKeysService:
    """A service for interacting with the ssh-keys endpoint"""

    def __init__(self, http_client) -> None:
        self._http_client = http_client

    def get(self) -> List[SSHKey]:
        """Retrieve the list of SSH keys

        :return: list of ssh-key objects
        :rtype: List[SSHKey]
        """
        ssh_keys_dict = self._http_client.get('/ssh-keys').json()
        ssh_key_objects = list(map(lambda ssh_keys_dict: SSHKey(
            id=ssh_keys_dict['id'],
            name=ssh_keys_dict['name'],
            public_key=ssh_keys_dict['public_key']
        ), ssh_keys_dict['data']))
        return ssh_key_objects

    def add(self, name: str, public_key: str = None) -> SSHKey:
        """Add an SSH key

        :param name: ssh-key name
        :type name: str
        :param public_key: ssh-key public key
        :type public_key: str, optional
        :return: ssh-key object
        :rtype: SSHKey
        """

        if public_key is None:
            payload = {"name": name}
        else:
            payload = {
                "name": name,
                "public_key": public_key
            }

        ssh_key_dict = self._http_client.post('/ssh-keys', json=payload).json()
        if 'data' in ssh_key_dict:
            ssh_key_object = SSHKey(
                id=ssh_key_dict['data']['id'],
                name=ssh_key_dict['data']['name'],
                public_key=ssh_key_dict['data']['public_key'],
                private_key=ssh_key_dict['data']['private_key'] if 'private_key' in ssh_key_dict['data'] else None
            )
            return ssh_key_object
        return None

    def delete(self, id: str) -> None:
        """Delete an ssh-key

        :param id: the unique identifier (ID) of the ssh-key
        :type id: str
        """
        return self._http_client.delete(f'/ssh-keys/{id}').text
