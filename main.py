from cloudkittyclient import client

# Initializing or establishing the connection
kwargs = {
    "tenant_name":"admin",
    "auth_url":"http://127.0.0.1:5000/v2.0",
    "username":"admin",
    "password":"sop52maw",
}

# creation of service args
fields_service = {
        "name": "compute",
}

# client get
ck = client.get_client("1", **kwargs)

# service creation
service_creation = ck.hashmap.services.create(**fields_service)

# service id
service_id = service_creation.service_id

# flavor field args
fields_flavor = {
        "name": "flavor",
        "service_id": service_id,
}

# flavor field creation
flavor_creation = ck.hashmap.fields.create(**fields_flavor)

# flavor id
flavor_id = flavor_creation.field_id

# image_id field args
fields_image = {
        "name": "image_id",
        "service_id": service_id,
}

# image_id field creation
image_id_field = ck.hashmap.fields.create(**fields_image)

# image_id field
image_id = image_id_field.field_id

# group field args
fields_group = {
        "name": "instance_uptime",
}

# group field creation
group_field = ck.hashmap.groups.create(**fields_group)

# group_id
group_id = group_field.group_id

# mapping for instance size args
args_to_rate_creation_instance_size = {
        'cost': '1.5',
        'value': 'm1.small',
        'field_id': flavor_id,
        'group_id': group_id,
}

# mapping creation for instance size price
mapping_fields_instance =  ck.hashmap.mappings.create(**args_to_rate_creation_instance_size)
