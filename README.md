# Cloudkitty-pricing-automation

This is the script which helps us to configure the Cloudkitty pricing in automated way.

Using this you can be able to configure pricing based on the following two Heads.

- Pricing based on instance size (m1.tiny, m1.small etc.,).

- Pricing based on the Image selected.

What you need to do is simply edit the cloudkitty_pricing.config file with necessary details.

Consider our config file is having content is as follows:

```
[connection]
tenant_name=admin
auth_url=http://127.0.0.1:5000/v2.0
username=admin
password=sop52maw

[instance_size_section]
m1.tiny=1.5
m1.small=2.5
m1.medium=3.5
m1.large=4.5
m1.xlarge=5.5


[image_section]
591c008a-6833-4167-9749-e5e5a74d1de4=7.5
sdfe008a-6833-4167-9749-e5e5a74d1de4=8.5
```

So in the above section you need to edit the necessary portions.

**[connection]** section is responsible for configuring the connection here as needed.
Edit the necessary details here such as 'tenant_name', 'auth_url', 'username', 'password'.


**[instance_size_section]** is responsible for configuration of price based on the instance size.
For example m1.tiny, m1.small etc will be the instance size which needs to be created.
So we can edit the price value as needed for configuring the same.

```
m1.tiny=1.5
```
We can edit the value as needed(2.5, 3.5 etc)


**[image_section]** is responsible for configuration of price based on the image provided.
We need to take the image id from the devstack admin panel and provide it here with the cost as follows:

```
591c008a-6833-4167-9749-e5e5a74d1de4=7.5
```

We can be able to provide 'n' number of image id's here to configure pricing.
