# role_management

### Available Operations

* [list_all_roles](#list_all_roles) - List all roles

## list_all_roles

Returns a list of all predefined and custom roles within your Fivetran account.

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


req = operations.ListAllRolesRequest(
    accept='application/json',
    cursor='provident',
    limit=896039,
)

res = s.role_management.list_all_roles(req)

if res.list_all_roles_200_application_json_object is not None:
    # handle response
```
