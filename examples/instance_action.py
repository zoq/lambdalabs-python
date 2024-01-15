import os
from lambdalabs import LambdaLabsClient

API_KEY = os.environ['LAMBDALABS_API_KEY']

lambdalabs = LambdaLabsClient(API_KEY)

# Retrieves details of the ordered instances, including whether or not the instance is running
instances = lambdalabs.instances.get()

# Go through all instances and perform the given action
for instance in instances:
    # Terminates the given instance
    lambdalabs.instances.stop(instance.id)

    # Restarts the given instance
    lambdalabs.instances.stop(instance.id)
    
