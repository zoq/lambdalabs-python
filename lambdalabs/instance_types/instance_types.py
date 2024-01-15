from typing import List


class InstanceType:
    """A instance type class"""

    def __init__(self,
                 name: str,
                 price_cents_per_hour: int,
                 description: str,
                 vcpus: int,
                 memory_gib: int,
                 storage_gib: int,
                 regions_with_capacity_available: List[str]
                 ) -> None:
        """Initialize a instance type object

        :param name: instance name
        :type name: str
        :param price_cents_per_hour: price in cents per hour
        :type price_cents_per_hour: int
        :param description: instance type description
        :type description: str
        :param vcpus: cpu details
        :type vcpus: int
        :param memory_gib: memory details
        :type memory_gib: int
        :param storage_gib: storage details
        :type storage_gib: int
        :param regions_with_capacity_available: list of available regions with capacity
        :type regions_with_capacity_available: List[str]
        """
        self._name = name
        self._price_cents_per_hour = price_cents_per_hour
        self._description = description
        self._vcpus = vcpus
        self._memory_gib = memory_gib
        self._storage_gib = storage_gib
        self._regions_with_capacity_available = regions_with_capacity_available

    @property
    def name(self) -> str:
        """Get the instance name

        :return: instance name
        :rtype: str
        """
        return self._name

    @property
    def price_cents_per_hour(self) -> int:
        """Get the instance type price in cents per hour

        :return: price in cents per hour
        :rtype: int
        """
        return self._price_cents_per_hour

    @property
    def description(self) -> str:
        """Get the instance type description

        :return: instance type description
        :rtype: str
        """
        return self._description

    @property
    def vcpus(self) -> int:
        """Get the instance type cpu details

        :return: instance type cpu details
        :rtype: int
        """
        return self._vcpus

    @property
    def memory_gib(self) -> int:
        """Get the instance type memory details

        :return: instance type memory details
        :rtype: int
        """
        return self._memory_gib

    @property
    def storage_gib(self) -> int:
        """Get the instance type storage details

        :return: instance type storage details
        :rtype: int
        """
        return self._storage_gib

    @property
    def regions_with_capacity_available(self) -> List[str]:
        """Get the instance type available regions with capacity

        :return: instance type available regions with capacity
        :rtype: str
        """
        return self._regions_with_capacity_available

    def __str__(self) -> str:
        """Print the instance type object

        :return: instance type string representation
        :rtype: str
        """
        return (f'name: {self._name}\n'
                f'price_cents_per_hour: {self._price_cents_per_hour}\n'
                f'description: {self._description}\n'
                f'vcpus: {self._vcpus}\n'
                f'memory_gib: {self._memory_gib}\n'
                f'storage_gib: {self._storage_gib}\n'
                f'regions_with_capacity_available: {self._regions_with_capacity_available}\n'
                )


class InstanceTypesService:
    """A service for interacting with the instance types endpoint"""

    def __init__(self, http_client) -> None:
        """Initialize a instance types service object

        :param http_client: http client to interact with the HTTP API
        :type http_client: HTTPClient
        """
        self._http_client = http_client

    def get(self) -> List[InstanceType]:
        """Returns a list of instance types

        :return: list of instance types
        :rtype: List[InstanceType]
        """
        instance_types = self._http_client.get('/instance-types').json()["data"]
        instance_type_objects = list(map(lambda instance_type: InstanceType(
            name=instance_type[1]['instance_type']['name'],
            price_cents_per_hour=instance_type[1]['instance_type']['price_cents_per_hour'],
            description=instance_type[1]['instance_type']['description'],
            vcpus=instance_type[1]['instance_type']['specs']['vcpus'],
            memory_gib=instance_type[1]['instance_type']['specs']['memory_gib'],
            storage_gib=instance_type[1]['instance_type']['specs']['storage_gib'],
            regions_with_capacity_available=instance_type[1]['regions_with_capacity_available']
        ), instance_types.items()))
        return instance_type_objects
