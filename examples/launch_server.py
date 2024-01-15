import os
from lambdalabs import LambdaLabsClient

API_KEY = os.environ['LAMBDALABS_API_KEY']

lambdalabs = LambdaLabsClient(API_KEY)

# Get all instance types
instance_types = lambdalabs.instance_types.get()

# Filter out instance types that are available
available_instance_types = [instance_type for instance_type in instance_types if len(instance_type.regions_with_capacity_available) > 0]
# Sort instance types by price and get the instance type with the lowest price
available_instance_types = sorted(available_instance_types, key=lambda instance_type: instance_type.price_cents_per_hour)

# Print the available instance types sorted by the lowest price
for instance_type in available_instance_types:
    print(instance_type)

# Launch the selected instance, change the parameters accordingly:
# region_name = 'us-tx-1'
# instance_type_name = 'gpu_8x_a100_80gb_sxm4'
# ssh_key_names = ['my-ssh-key']
# file_system_names = []
# quantity = 1
# name = 'lambda-test-1'
lambdalabs.instances.launch(region_name, instance_type_name, ssh_key_names, quantity, name)