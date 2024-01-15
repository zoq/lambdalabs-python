from typing import List, Union
from lambdalabs.instance_types.instance_types import InstanceType


class Instance:
    """An instance model class"""

    def __init__(self,
                 id: str,
                 region: dict,
                 ip: str,
                 instance_type: InstanceType,
                 status: str,
                 ssh_key_names: List[str],
                 file_system_names: List[str],
                 hostname: str,
                 jupyter_token: str,
                 jupyter_url: str
                 ) -> None:
        """Initialize the instance object

        :param id: instance id
        :type id: str
        :param region: instance region details
        :type region: dict
        :param ip: instance ip address
        :type ip: str
        :param instance_type: instance type details
        :type instance_type: InstanceType
        :param status: instance status
        :type status: str
        :param ssh_key_names: list of ssh key names
        :type ssh_key_names: List[str]
        :param file_system_names: list of file system names
        :type file_system_names: List[str]
        :param hostname: instance hostname
        :type hostname: str
        :param jupyter_token: instance jupyter token
        :type jupyter_token: str
        :param jupyter_url: instance jupyter url
        :type jupyter_url: str
        """
        self._id = id
        self._region = region
        self._ip = ip
        self._instance_type = instance_type
        self._status = status
        self._ssh_key_names = ssh_key_names
        self._file_system_names = file_system_names
        self._hostname = hostname
        self._jupyter_token = jupyter_token
        self._jupyter_url = jupyter_url

    @property
    def id(self) -> str:
        """Get the instance id

        :return: instance id
        :rtype: str
        """
        return self._id

    @property
    def ip(self) -> str:
        """Get the instance ip address

        :return: instance ip address
        :rtype: str
        """
        return self._ip

    @property
    def instance_type(self) -> InstanceType:
        """Get the instance type details

        :return: instance type details
        :rtype: str
        """
        return self._instance_type

    @property
    def status(self) -> str:
        """Get the instance status

        :return: instance status
        :rtype: str
        """
        return self._status

    @property
    def ssh_key_names(self) -> List[str]:
        """Get the instance ssh key names

        :return: instance ssh key names
        :rtype: List[str]
        """
        return self._ssh_key_names

    @property
    def file_system_names(self) -> List[str]:
        """Get the instance file system names

        :return: instance file system names
        :rtype: List[str]
        """
        return self._file_system_names

    @property
    def hostname(self) -> str:
        """Get the instance hostname

        :return: instance hostname
        :rtype: str
        """
        return self._hostname

    @property
    def jupyter_token(self) -> str:
        """Get the instance jupyter token

        :return: instance jupyter token
        :rtype: str
        """
        return self._jupyter_token

    @property
    def jupyter_url(self) -> str:
        """Get the instance jupyter url

        :return: instance jupyter url
        :rtype: str
        """
        return self._jupyter_url

    def __str__(self) -> str:
        """Print the instance

        :return: instance string representation
        :rtype: str
        """
        return (f'id: {self._id}\n'
                f'region: {self._region}\n'
                f'ip: {self._ip}\n'
                f'instance_type: {self._instance_type}\n'
                f'status: {self._status}\n'
                f'ssh_key_names: {self._ssh_key_names}\n'
                f'file_system_names: {self._file_system_names}\n'
                f'hostname: {self._hostname}\n'
                f'jupyter_token: {self._jupyter_token}\n'
                f'jupyter_url: {self._jupyter_url}\n'
                )


class InstancesService:
    """A service for interacting with the instances endpoint"""

    def __init__(self, http_client) -> None:
        self._http_client = http_client

    def get(self) -> List[Instance]:
        """Get all of the client's instances

        :return: list of instance objects
        :rtype: List[Instance]
        """
        instances_dict = self._http_client.get('/instances').json()
        instances = list(map(lambda instance_dict: Instance(
            id=instance_dict['id'] if 'id' in instance_dict else None,
            region=instance_dict['region'] if 'region' in instance_dict else None,
            ip=instance_dict['ip'] if 'ip' in instance_dict else None,
            instance_type=InstanceType(instance_dict['instance_type']['name'],
                                       instance_dict['instance_type']['price_cents_per_hour'],
                                       instance_dict['instance_type']['description'],
                                       instance_dict['instance_type']['specs']['vcpus'],
                                       instance_dict['instance_type']['specs']['memory_gib'],
                                       instance_dict['instance_type']['specs']['storage_gib'],
                                       None) if 'instance_type' in instance_dict else None,
            status=instance_dict['status'] if 'status' in instance_dict else None,
            ssh_key_names=instance_dict['ssh_key_names'] if 'ssh_key_names' in instance_dict else None,
            file_system_names=instance_dict['file_system_names'] if 'file_system_names' in instance_dict else None,
            hostname=instance_dict['hostname'] if 'hostname' in instance_dict else None,
            jupyter_token=instance_dict['jupyter_token'] if 'jupyter_token' in instance_dict else None,
            jupyter_url=instance_dict['jupyter_url'] if 'jupyter_url' in instance_dict else None
        ), instances_dict['data']))
        return instances

    def get_by_id(self, id: str) -> Instance:
        """Get an instance with specified id.

        :param id: instance id
        :type id: str
        :return: instance details object
        :rtype: Instance
        """
        instance_dict = self._http_client.get('/instances' + f'/{id}').json()
        print(instance_dict)
        if 'data' not in instance_dict:
            return None
        instance_dict = instance_dict['data']
        instance = Instance(
            id=instance_dict['id'] if 'id' in instance_dict else None,
            region=instance_dict['region'] if 'region' in instance_dict else None,
            ip=instance_dict['ip'] if 'ip' in instance_dict else None,
            instance_type=InstanceType(instance_dict['instance_type']['name'],
                                       instance_dict['instance_type']['price_cents_per_hour'],
                                       instance_dict['instance_type']['description'],
                                       instance_dict['instance_type']['specs']['vcpus'],
                                       instance_dict['instance_type']['specs']['memory_gib'],
                                       instance_dict['instance_type']['specs']['storage_gib'],
                                       None) if 'instance_type' in instance_dict else None,
            status=instance_dict['status'] if 'status' in instance_dict else None,
            ssh_key_names=instance_dict['ssh_key_names'] if 'ssh_key_names' in instance_dict else None,
            file_system_names=instance_dict['file_system_names'] if 'file_system_names' in instance_dict else None,
            hostname=instance_dict['hostname'] if 'hostname' in instance_dict else None,
            jupyter_token=instance_dict['jupyter_token'] if 'jupyter_token' in instance_dict else None,
            jupyter_url=instance_dict['jupyter_url'] if 'jupyter_url' in instance_dict else None
        )
        return instance

    def launch(self,
               region_name: str,
               instance_type_name: str,
               ssh_key_names: List[str],
               file_system_names: List[str] = [],
               quantity: int = 1,
               name: str = "") -> List[str]:
        """Launches one or more instances of a given instance type.

        :param region_name: short name of a region
        :type region_name: str
        :param instance_type_name: name of an instance type
        :type instance_type_name: str
        :param ssh_key_names: names of the SSH keys to allow access to the instances,
                currently, exactly one SSH key must be specified
        :type ssh_key_names: List[str]
        :param file_system_names: names of the file systems to attach to the instances.
                Currently, only one (if any) file system may be specified.
        :type file_system_names: List[str], optional
        :param quantity: number of instances to launch
        :type quantity: int, optional
        :param name: user-provided name for the instance
        :type name: str, optional
        :return: ids of the launched instances
        :rtype: List[str]
        """
        payload = {
            "region_name": region_name,
            "instance_type_name": instance_type_name,
            "ssh_key_names": ssh_key_names,
            "file_system_names": file_system_names,
            "quantity": quantity,
            "name": name
        }
        instance_ids = self._http_client.post('/instance-operations/launch', json=payload).json()

        if 'data' in instance_ids and 'instance_ids' in instance_ids['data']:
            return instance_ids['data']['instance_ids']
        return None

    def terminate(self, instance_ids: Union[List[str], str]) -> List[str]:
        """Terminate a list of instances / single instance

        :param id_list: list of instance ids, or an instance id
        :type id_list: Union[List[str], str]
        """
        if type(instance_ids) is str:
            instance_ids = [instance_ids]

        payload = {"instance_ids": instance_ids}
        instance_ids = self._http_client.post('/instance-operations/terminate', json=payload).json()

        if 'data' in instance_ids and 'terminated_instances' in instance_ids['data']:
            return instance_ids['data']['terminated_instances']
        return None

    def restart(self, instance_ids: Union[List[str], str]) -> List[str]:
        """Restart a list of instances / single instance

        :param id_list: list of instance ids, or an instance id
        :type id_list: Union[List[str], str]
        """
        if type(instance_ids) is str:
            instance_ids = [instance_ids]

        payload = {"instance_ids": instance_ids}
        instance_ids = self._http_client.post('/instance-operations/restart', json=payload).json()

        if 'data' in instance_ids and 'restarted_instances' in instance_ids['data']:
            return instance_ids['data']['restarted_instances']
        return None
