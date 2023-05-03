# destination_management

### Available Operations

* [create_destination](#create_destination) - Create destination
* [delete_destination](#delete_destination) - Delete a destination
* [destination_details](#destination_details) - Retrieve Destination Details
* [modify_destination](#modify_destination) - Modify a Destination
* [run_destination_setup_tests](#run_destination_setup_tests) - Run Destination Setup Tests

## create_destination

Creates a new destination within a specified group in your Fivetran account.

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


req = operations.CreateDestinationRequest(
    accept='application/json;version=2',
    new_destination_request=shared.NewDestinationRequest(
        group_id='String',
        region=shared.NewDestinationRequestRegionEnum.AZURE_AUSTRALIAEAST,
        run_setup_tests=True,
        service='String',
        time_zone_offset='integer: -11, 10 ... ,0 , ... +11, +12',
        trust_certificates=False,
        trust_fingerprints=False,
    ),
)

res = s.destination_management.create_destination(req)

if res.create_destination_201_application_json_object is not None:
    # handle response
```

## delete_destination

Deletes a destination from your Fivetran account.

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


req = operations.DeleteDestinationRequest(
    accept='application/json;version=2',
    destination_id='sint',
)

res = s.destination_management.delete_destination(req)

if res.delete_destination_200_application_json_object is not None:
    # handle response
```

## destination_details

Returns a destination object if a valid identifier was provided.

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


req = operations.DestinationDetailsRequest(
    accept='application/json;version=2',
    destination_id='veritatis',
)

res = s.destination_management.destination_details(req)

if res.destination_details_200_application_json_object is not None:
    # handle response
```

## modify_destination

Updates information for an existing destination within your Fivetran account.

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


req = operations.ModifyDestinationRequest(
    accept='application/json;version=2',
    update_destination_request=shared.UpdateDestinationRequest(
        config='itaque',
        region=shared.UpdateDestinationRequestRegionEnum.GCP_NORTHAMERICA_NORTHEAST1,
        run_setup_tests=True,
        time_zone_offset='integer: -11, 10 ... ,0 , ... +11, +12',
        trust_certificates=False,
        trust_fingerprints=False,
    ),
    destination_id='enim',
)

res = s.destination_management.modify_destination(req)

if res.modify_destination_200_application_json_object is not None:
    # handle response
```

## run_destination_setup_tests

Runs the setup tests for an existing destination within your Fivetran account.

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


req = operations.RunDestinationSetupTestsRequest(
    accept='application/json;version=2',
    run_setup_tests_request=shared.RunSetupTestsRequest(
        trust_certificates=False,
        trust_fingerprints=False,
    ),
    destination_id='consequatur',
)

res = s.destination_management.run_destination_setup_tests(req)

if res.run_destination_setup_tests_200_application_json_object is not None:
    # handle response
```
