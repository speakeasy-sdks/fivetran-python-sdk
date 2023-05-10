# team_management

### Available Operations

* [add_team_membership_in_connector](#add_team_membership_in_connector) - Add connector membership
* [add_team_membership_in_group](#add_team_membership_in_group) - Add group membership
* [add_user_to_team](#add_user_to_team) - Add a user to a team
* [create_team](#create_team) - Create a team
* [delete_team](#delete_team) - Delete a team
* [delete_team_membership_in_account](#delete_team_membership_in_account) - Delete team role in account
* [delete_team_membership_in_connector](#delete_team_membership_in_connector) - Delete connector membership
* [delete_team_membership_in_group](#delete_team_membership_in_group) - Delete group membership
* [delete_user_from_team](#delete_user_from_team) - Delete a user from a team
* [get_team_membership_in_connector](#get_team_membership_in_connector) - Retrieve connector membership
* [get_team_membership_in_group](#get_team_membership_in_group) - Retrieve group membership
* [get_team_memberships_in_connectors](#get_team_memberships_in_connectors) - List all connector memberships
* [get_team_memberships_in_groups](#get_team_memberships_in_groups) - List all group memberships
* [get_user_in_team](#get_user_in_team) - Retrieve user membership in a team
* [list_all_teams](#list_all_teams) - List all teams
* [list_users_in_team](#list_users_in_team) - List all user memberships
* [modify_team](#modify_team) - Modify a team
* [team_details](#team_details) - Retrieve team details
* [update_team_membership_in_connector](#update_team_membership_in_connector) - Update connector membership
* [update_team_membership_in_group](#update_team_membership_in_group) - Update group membership
* [update_user_membership](#update_user_membership) - Modify a user membership

## add_team_membership_in_connector

Adds a connector role within a team

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

req = operations.AddTeamMembershipInConnectorRequest(
    accept='application/json',
    membership_request=shared.MembershipRequest(
        id='9a3efa77-dfb1-44cd-a6ae-395efb9ba88f',
        role='amet',
    ),
    team_id='deserunt',
)

res = s.team_management.add_team_membership_in_connector(req)

if res.add_team_membership_in_connector_201_application_json_object is not None:
    # handle response
```

## add_team_membership_in_group

Adds a group membership in a team

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

req = operations.AddTeamMembershipInGroupRequest(
    accept='application/json',
    membership_request=shared.MembershipRequest(
        id='66997074-ba44-469b-ae21-41959890afa5',
        role='eum',
    ),
    team_id='dolor',
)

res = s.team_management.add_team_membership_in_group(req)

if res.add_team_membership_in_group_201_application_json_object is not None:
    # handle response
```

## add_user_to_team

Assigns a user role within a team

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

req = operations.AddUserToTeamRequest(
    accept='application/json',
    team_membership_request=shared.TeamMembershipRequest(
        role='necessitatibus',
        user_id='odit',
    ),
    team_id='nemo',
)

res = s.team_management.add_user_to_team(req)

if res.add_user_to_team_201_application_json_object is not None:
    # handle response
```

## create_team

Creates a new team in your Fivetran account

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

req = operations.CreateTeamRequest(
    accept='application/json',
    team_request=shared.TeamRequest(
        description='quasi',
        name='Melba Toy',
        role='deleniti',
    ),
)

res = s.team_management.create_team(req)

if res.create_team_201_application_json_object is not None:
    # handle response
```

## delete_team

Deletes a team from your Fivetran account

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

req = operations.DeleteTeamRequest(
    accept='application/json',
    team_id='facilis',
)

res = s.team_management.delete_team(req)

if res.delete_team_200_application_json_object is not None:
    # handle response
```

## delete_team_membership_in_account

Removes a team role within your Fivetran account

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

req = operations.DeleteTeamMembershipInAccountRequest(
    accept='application/json',
    team_id='in',
)

res = s.team_management.delete_team_membership_in_account(req)

if res.delete_team_membership_in_account_200_application_json_object is not None:
    # handle response
```

## delete_team_membership_in_connector

Removes connector membership in a team

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

req = operations.DeleteTeamMembershipInConnectorRequest(
    accept='application/json',
    connector_id='architecto',
    team_id='architecto',
)

res = s.team_management.delete_team_membership_in_connector(req)

if res.delete_team_membership_in_connector_200_application_json_object is not None:
    # handle response
```

## delete_team_membership_in_group

Removes group membership in a team

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

req = operations.DeleteTeamMembershipInGroupRequest(
    accept='application/json',
    group_id='repudiandae',
    team_id='ullam',
)

res = s.team_management.delete_team_membership_in_group(req)

if res.delete_team_membership_in_group_200_application_json_object is not None:
    # handle response
```

## delete_user_from_team

Removes a user from a team

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

req = operations.DeleteUserFromTeamRequest(
    accept='application/json',
    team_id='expedita',
    user_id='nihil',
)

res = s.team_management.delete_user_from_team(req)

if res.delete_user_from_team_200_application_json_object is not None:
    # handle response
```

## get_team_membership_in_connector

Returns a connector membership within a team

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

req = operations.GetTeamMembershipInConnectorRequest(
    accept='application/json',
    connector_id='repellat',
    team_id='quibusdam',
)

res = s.team_management.get_team_membership_in_connector(req)

if res.get_team_membership_in_connector_200_application_json_object is not None:
    # handle response
```

## get_team_membership_in_group

Returns a group membership within a team.

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

req = operations.GetTeamMembershipInGroupRequest(
    accept='application/json',
    group_id='sed',
    team_id='saepe',
)

res = s.team_management.get_team_membership_in_group(req)

if res.get_team_membership_in_group_200_application_json_object is not None:
    # handle response
```

## get_team_memberships_in_connectors

Returns connector memberships within a team.

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

req = operations.GetTeamMembershipsInConnectorsRequest(
    accept='application/json',
    cursor='pariatur',
    limit=37559,
    team_id='consequuntur',
)

res = s.team_management.get_team_memberships_in_connectors(req)

if res.get_team_memberships_in_connectors_200_application_json_object is not None:
    # handle response
```

## get_team_memberships_in_groups

Returns a group membership within a team

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

req = operations.GetTeamMembershipsInGroupsRequest(
    accept='application/json',
    cursor='praesentium',
    limit=615560,
    team_id='magni',
)

res = s.team_management.get_team_memberships_in_groups(req)

if res.get_team_memberships_in_groups_200_application_json_object is not None:
    # handle response
```

## get_user_in_team

Returns the user role a user has within a team

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

req = operations.GetUserInTeamRequest(
    accept='application/json',
    team_id='sunt',
    user_id='quo',
)

res = s.team_management.get_user_in_team(req)

if res.get_user_in_team_200_application_json_object is not None:
    # handle response
```

## list_all_teams

Returns a list of all teams within your Fivetran account

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

req = operations.ListAllTeamsRequest(
    accept='application/json',
    cursor='illum',
    limit=864934,
)

res = s.team_management.list_all_teams(req)

if res.list_all_teams_200_application_json_object is not None:
    # handle response
```

## list_users_in_team

Returns a list of users and their roles within a team in your Fivetran account

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

req = operations.ListUsersInTeamRequest(
    accept='application/json',
    cursor='maxime',
    limit=411397,
    team_id='excepturi',
)

res = s.team_management.list_users_in_team(req)

if res.list_users_in_team_200_application_json_object is not None:
    # handle response
```

## modify_team

Updates information for an existing team within your Fivetran account

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

req = operations.ModifyTeamRequest(
    accept='application/json',
    team_request=shared.TeamRequest(
        description='odit',
        name='Donna Bernhard',
        role='ipsam',
    ),
    team_id='voluptate',
)

res = s.team_management.modify_team(req)

if res.modify_team_200_application_json_object is not None:
    # handle response
```

## team_details

Returns information for a given team within your Fivetran account

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

req = operations.TeamDetailsRequest(
    accept='application/json',
    team_id='autem',
)

res = s.team_management.team_details(req)

if res.team_details_200_application_json_object is not None:
    # handle response
```

## update_team_membership_in_connector

Updates connector membership in a team

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

req = operations.UpdateTeamMembershipInConnectorRequest(
    accept='application/json',
    update_membership_request=shared.UpdateMembershipRequest(
        role='nam',
    ),
    connector_id='eaque',
    team_id='pariatur',
)

res = s.team_management.update_team_membership_in_connector(req)

if res.update_team_membership_in_connector_200_application_json_object is not None:
    # handle response
```

## update_team_membership_in_group

Updates group membership in a team

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

req = operations.UpdateTeamMembershipInGroupRequest(
    accept='application/json',
    update_membership_request=shared.UpdateMembershipRequest(
        role='nemo',
    ),
    group_id='voluptatibus',
    team_id='perferendis',
)

res = s.team_management.update_team_membership_in_group(req)

if res.update_team_membership_in_group_200_application_json_object is not None:
    # handle response
```

## update_user_membership

Updates a user role within a team in your Fivetran account

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

req = operations.UpdateUserMembershipRequest(
    accept='application/json',
    update_membership_request=shared.UpdateMembershipRequest(
        role='fugiat',
    ),
    team_id='amet',
    user_id='aut',
)

res = s.team_management.update_user_membership(req)

if res.update_user_membership_200_application_json_object is not None:
    # handle response
```
