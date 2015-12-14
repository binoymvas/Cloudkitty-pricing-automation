#!/usr/bin/env python
#
# Creating a Pricing in Cloudkkity
# Automated script for Configuring prices in Cloudkitty
#
# Author: Muralidharan.S
#
from cloudkittyclient import client

import ConfigParser

# For importing details from config file
config = ConfigParser.RawConfigParser()
config.read('cloudkitty_pricing.config')

# Fetch details from config file
# For connection part
connection = dict(config.items("connection"))

# Initializing the connection
kwargs = {
    "tenant_name":connection['tenant_name'],
    "auth_url":connection['auth_url'],
    "username":connection['username'],
    "password":connection['password'],
}

# Establish the connection
ck = client.get_client("1", **kwargs)                                                                                                                                                                      

# module enable args
module_args = {
    "module_id": "hashmap",
}

# Enable Hashmap module
module = ck.modules.get(**module_args)
module.enable()

# creation of service args
service_args = {
    "name": "compute",
}
                                                                                                                                                                                                           
# service creation                                                                                                                                                                                   
service_creation = ck.hashmap.services.create(**service_args)                                                                                                                                            
                                                                                                                                                                                                           
# service id fetch                                                                                                                                                                                         
service_id = service_creation.service_id                                                                                                                                                                   
                                                                                                                                                                                                           
# flavor field args                                                                                                                                                                                        
fields_flavor = {                                                                                                                                                                                          
    "name": "flavor",
    "service_id": service_id,
}                                                                                                                                                                                                          
                                                                                                                                                                                                           
# flavor field creation                                                                                                                                                                                    
flavor_field_creation = ck.hashmap.fields.create(**fields_flavor)

# flavor id fetch
flavor_field_id = flavor_field_creation.field_id

# image_field args
image_field_args = {
    "name": "image_id",
    "service_id": service_id,
}

# image_field_id field creation
image_field_id_creation = ck.hashmap.fields.create(**image_field_args)

# image_field_id fetch
image_field_id = image_field_id_creation.field_id

# group field args
group_fields_args = {
    "name": "instance_uptime",
}

# group field creation
group_field_creation = ck.hashmap.groups.create(**group_fields_args)

# group_id fetch
group_id = group_field_creation.group_id

# group field args for image
group_fields_args_for_image = {
    "name": "instance_image",
}

# group field creation for image
group_field_creation_for_image = ck.hashmap.groups.create(**group_fields_args_for_image)

# group_id fetch for image
group_id_image = group_field_creation_for_image.group_id

# Fetch the arguments for Instance size section from conf file
instance_size_section = dict(config.items("instance_size_section"))

# create the mapping for instance size section with existing values
for size, cost in instance_size_section.items():

    # args for instance size section
    args_to_rate_creation_instance_size = {
        'cost': cost,
        'value': size,
        'field_id': flavor_field_id,
        'group_id': group_id,
    }

    # mapping creation for instance size price
    mapping_fields_instance = ck.hashmap.mappings.create(**args_to_rate_creation_instance_size)

# Fetch the arguments for image pricing section from conf file
image_section = dict(config.items("image_section"))

# create the mapping for image Pricing section with existing value
for id, cost in image_section.items():

    # mapping for image
    args_to_rate_image = {
        'cost': cost,
        'value': id,
        'field_id':image_field_id,
        'group_id': group_id_image,
    }

    # mapping creation for image price
    mapping_fields_image = ck.hashmap.mappings.create(**args_to_rate_image)
