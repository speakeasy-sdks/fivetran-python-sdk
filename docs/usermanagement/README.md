# user_management

### Available Operations

* [add_user_membership_in_connector](#add_user_membership_in_connector) - Add connector membership
* [add_user_membership_in_group](#add_user_membership_in_group) - Add group membership
* [create_user](#create_user) - Invite a User
* [delete_user](#delete_user) - Delete a user
* [delete_user_membership_in_account](#delete_user_membership_in_account) - Delete user role in account
* [delete_user_membership_in_connector](#delete_user_membership_in_connector) - Delete connector membership
* [delete_user_membership_in_group](#delete_user_membership_in_group) - Delete group membership
* [get_user_membership_in_connector](#get_user_membership_in_connector) - Retrieve connector membership
* [get_user_membership_in_group](#get_user_membership_in_group) - Retrieve group membership
* [get_user_memberships_in_connectors](#get_user_memberships_in_connectors) - List all connector memberships
* [get_user_memberships_in_groups](#get_user_memberships_in_groups) - List all group memberships
* [list_all_users](#list_all_users) - List All Users
* [modify_user](#modify_user) - Modify a User
* [update_user_membership_in_connector](#update_user_membership_in_connector) - Update connector membership
* [update_user_membership_in_group](#update_user_membership_in_group) - Update group membership
* [user_details](#user_details) - Retrieve User Details

## add_user_membership_in_connector

Adds a connector membership

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

req = operations.AddUserMembershipInConnectorRequest(
    accept='application/json',
    membership_request=shared.MembershipRequest(
        id='c5fbb258-7053-4202-873d-5fe9b90c2890',
        role='occaecati',
    ),
    user_id='rerum',
)

res = s.user_management.add_user_membership_in_connector(req)

if res.membership_response is not None:
    # handle response
```

## add_user_membership_in_group

Adds a group membership.

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

req = operations.AddUserMembershipInGroupRequest(
    accept='application/json',
    membership_request=shared.MembershipRequest(
        id='3fe49a8d-9cbf-4486-b332-3f9b77f3a410',
        role='ipsa',
    ),
    user_id='iure',
)

res = s.user_management.add_user_membership_in_group(req)

if res.add_user_membership_in_group_201_application_json_object is not None:
    # handle response
```

## create_user

Invites a new user to your Fivetran account. The invited user will have access to the account only after accepting the invitation. Invited user details are still accessible through the API.

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

req = operations.CreateUserRequest(
    accept='application/json',
    new_user_request=shared.NewUserRequest(
        email='string',
        family_name='string',
        given_name='string',
        phone='string',
        picture='string',
        role='odio',
    ),
)

res = s.user_management.create_user(req)

if res.create_user_201_application_json_object is not None:
    # handle response
```

## delete_user

Deletes a user from your Fivetran account. You will be unable to delete an account owner user if there is only one remaining.

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

req = operations.DeleteUserRequest(
    accept='application/json',
    user_id='quaerat',
)

res = s.user_management.delete_user(req)

if res.delete_user_200_application_json_object is not None:
    # handle response
```

## delete_user_membership_in_account

Removes a user's role in account.

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

req = operations.DeleteUserMembershipInAccountRequest(
    accept='application/json',
    user_id='accusamus',
)

res = s.user_management.delete_user_membership_in_account(req)

if res.delete_user_membership_in_account_200_application_json_object is not None:
    # handle response
```

## delete_user_membership_in_connector

Removes connector membership.

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

req = operations.DeleteUserMembershipInConnectorRequest(
    accept='application/json',
    connector_id='quidem',
    user_id='voluptatibus',
)

res = s.user_management.delete_user_membership_in_connector(req)

if res.delete_user_membership_in_connector_200_application_json_object is not None:
    # handle response
```

## delete_user_membership_in_group

Removes group membership.

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

req = operations.DeleteUserMembershipInGroupRequest(
    accept='application/json',
    group_id='voluptas',
    user_id='natus',
)

res = s.user_management.delete_user_membership_in_group(req)

if res.delete_user_membership_in_group_200_application_json_object is not None:
    # handle response
```

## get_user_membership_in_connector

Returns a connector membership object.

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

req = operations.GetUserMembershipInConnectorRequest(
    accept='application/json',
    connector_id='eos',
    user_id='atque',
)

res = s.user_management.get_user_membership_in_connector(req)

if res.get_user_membership_in_connector_200_application_json_object is not None:
    # handle response
```

## get_user_membership_in_group

Returns a group membership object.

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

req = operations.GetUserMembershipInGroupRequest(
    accept='application/json',
    group_id='sit',
    user_id='fugiat',
)

res = s.user_management.get_user_membership_in_group(req)

if res.get_user_membership_in_group_200_application_json_object is not None:
    # handle response
```

## get_user_memberships_in_connectors

Returns all connector membership objects for a user within your Fivetran account

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

req = operations.GetUserMembershipsInConnectorsRequest(
    accept='application/json',
    cursor='ab',
    limit=743835,
    user_id='dolorum',
)

res = s.user_management.get_user_memberships_in_connectors(req)

if res.get_user_memberships_in_connectors_200_application_json_object is not None:
    # handle response
```

## get_user_memberships_in_groups

Returns all group membership objects for a user within your Fivetran account.

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

req = operations.GetUserMembershipsInGroupsRequest(
    accept='application/json',
    cursor='iusto',
    limit=453697,
    user_id='dolorum',
)

res = s.user_management.get_user_memberships_in_groups(req)

if res.get_user_memberships_in_groups_200_application_json_object is not None:
    # handle response
```

## list_all_users

Returns a list of all users within your Fivetran account.

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

req = operations.ListAllUsersRequest(
    accept='application/json',
    cursor='deleniti',
    limit=607045,
)

res = s.user_management.list_all_users(req)

if res.list_all_users_200_application_json_object is not None:
    # handle response
```

## modify_user

Updates information for an existing user within your Fivetran account.

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

req = operations.ModifyUserRequest(
    accept='application/json',
    update_user_request=shared.UpdateUserRequest(
        family_name='string',
        given_name='string',
        phone='string',
        picture='string',
        role='necessitatibus',
    ),
    user_id='distinctio',
)

res = s.user_management.modify_user(req)

if res.modify_user_200_application_json_object is not None:
    # handle response
```

## update_user_membership_in_connector

Updates connector membership.

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

req = operations.UpdateUserMembershipInConnectorRequest(
    accept='application/json',
    update_membership_request=shared.UpdateMembershipRequest(
        role='asperiores',
    ),
    connector_id='nihil',
    user_id='ipsum',
)

res = s.user_management.update_user_membership_in_connector(req)

if res.update_user_membership_in_connector_200_application_json_object is not None:
    # handle response
```

## update_user_membership_in_group

Updates group membership.

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

req = operations.UpdateUserMembershipInGroupRequest(
    accept='application/json',
    update_membership_request=shared.UpdateMembershipRequest(
        role='voluptate',
    ),
    group_id='id',
    user_id='saepe',
)

res = s.user_management.update_user_membership_in_group(req)

if res.update_user_membership_in_group_200_application_json_object is not None:
    # handle response
```

## user_details

Returns a user object if a valid identifier was provided.

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

req = operations.UserDetailsRequest(
    accept='application/json',
    user_id='eius',
)

res = s.user_management.user_details(req)

if res.user_details_200_application_json_object is not None:
    # handle response
```
