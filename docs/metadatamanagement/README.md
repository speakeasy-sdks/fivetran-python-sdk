# metadata_management

### Available Operations

* [column_metadata](#column_metadata) - Retrieve column metadata
* [schema_metadata](#schema_metadata) - Retrieve schema metadata
* [table_metadata](#table_metadata) - Retrieve table metadata

## column_metadata

Returns column-level metadata for an existing connector within your Fivetran account.

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

req = operations.ColumnMetadataRequest(
    accept='application/json',
    connector_id='facilis',
    cursor='tempore',
    limit=288476,
)

res = s.metadata_management.column_metadata(req)

if res.column_metadata_200_application_json_object is not None:
    # handle response
```

## schema_metadata

Returns schema-level metadata for an existing connector within your Fivetran account.

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

req = operations.SchemaMetadataRequest(
    accept='application/json',
    connector_id='delectus',
    cursor='eum',
    limit=248753,
)

res = s.metadata_management.schema_metadata(req)

if res.schema_metadata_200_application_json_object is not None:
    # handle response
```

## table_metadata

Returns table-level metadata for an existing connector within your Fivetran account.

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

req = operations.TableMetadataRequest(
    accept='application/json',
    connector_id='eligendi',
    cursor='sint',
    limit=396098,
)

res = s.metadata_management.table_metadata(req)

if res.table_metadata_200_application_json_object is not None:
    # handle response
```
