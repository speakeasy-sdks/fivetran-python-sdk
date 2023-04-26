# group_management

### Available Operations

* [add_user_to_group](#add_user_to_group) - Add a User to a Group
* [create_group](#create_group) - Create a Group
* [delete_group](#delete_group) - Delete a group
* [delete_user_from_group](#delete_user_from_group) - Remove a User from a Group
* [group_details](#group_details) - Retrieve Group Details
* [list_all_connectors_in_group](#list_all_connectors_in_group) - List All Connectors within a Group
* [list_all_groups](#list_all_groups) - List All Groups
* [list_all_users_in_group](#list_all_users_in_group) - List All Users within a Group
* [modify_group](#modify_group) - Modify a Group

## add_user_to_group

Adds an existing user to a group in your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.AddUserToGroupRequest(
    accept="application/json",
    add_user_to_group_request=shared.AddUserToGroupRequest(
        email="Roosevelt_Cole@hotmail.com",
        role="quibusdam",
    ),
    group_id="labore",
)

res = s.group_management.add_user_to_group(req)

if res.add_user_to_group_200_application_json_object is not None:
    # handle response
```

## create_group

Creates a new group in your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.CreateGroupRequest(
    accept="application/json",
    new_group_request=shared.NewGroupRequest(
        name="string",
    ),
)

res = s.group_management.create_group(req)

if res.create_group_201_application_json_object is not None:
    # handle response
```

## delete_group

Deletes a group from your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.DeleteGroupRequest(
    accept="application/json",
    group_id="modi",
)

res = s.group_management.delete_group(req)

if res.delete_group_200_application_json_object is not None:
    # handle response
```

## delete_user_from_group

Removes an existing user from a group in your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.DeleteUserFromGroupRequest(
    accept="application/json",
    group_id="qui",
    user_id="aliquid",
)

res = s.group_management.delete_user_from_group(req)

if res.delete_user_from_group_200_application_json_object is not None:
    # handle response
```

## group_details

Returns a group object if a valid identifier was provided.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.GroupDetailsRequest(
    accept="application/json",
    group_id="cupiditate",
)

res = s.group_management.group_details(req)

if res.group_details_200_application_json_object is not None:
    # handle response
```

## list_all_connectors_in_group

Returns a list of information about all connectors within a group in your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ListAllConnectorsInGroupRequest(
    accept="application/json",
    cursor="quos",
    group_id="perferendis",
    limit=164940,
    schema="assumenda",
)

res = s.group_management.list_all_connectors_in_group(req)

if res.list_all_connectors_in_group_200_application_json_object is not None:
    # handle response
```

## list_all_groups

Returns a list of all groups within your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ListAllGroupsRequest(
    accept="application/json",
    cursor="ipsam",
    limit=4695,
)

res = s.group_management.list_all_groups(req)

if res.list_all_groups_200_application_json_object is not None:
    # handle response
```

## list_all_users_in_group

Returns a list of information about all users within a group in your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ListAllUsersInGroupRequest(
    accept="application/json",
    cursor="fugit",
    group_id="dolorum",
    limit=569618,
)

res = s.group_management.list_all_users_in_group(req)

if res.list_all_users_in_group_200_application_json_object is not None:
    # handle response
```

## modify_group

Updates information for an existing group within your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ModifyGroupRequest(
    accept="application/json",
    update_group_request=shared.UpdateGroupRequest(
        name="string",
    ),
    group_id="tempora",
)

res = s.group_management.modify_group(req)

if res.modify_group_200_application_json_object is not None:
    # handle response
```
