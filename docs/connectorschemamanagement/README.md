# connector_schema_management

### Available Operations

* [connector_column_config](#connector_column_config) - Retrieve Source Table Columns Config
* [connector_schema_config](#connector_schema_config) - Retrieve a Connector Schema Config
* [modify_connector_column_config](#modify_connector_column_config) - Modify a Connector Column Config
* [modify_connector_database_schema_config](#modify_connector_database_schema_config) - Modify a Connector Database Schema Config
* [modify_connector_schema_config](#modify_connector_schema_config) - Modify a Connector Schema Config
* [modify_connector_table_config](#modify_connector_table_config) - Modify a Connector Table Config
* [reload_connector_schema_config](#reload_connector_schema_config) - Reload a Connector Schema Config
* [resync_tables](#resync_tables) - Re-sync Connector Table Data

## connector_column_config

Returns the source table columns config for an existing connector within your Fivetran account

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


req = operations.ConnectorColumnConfigRequest(
    accept='application/json',
    connector_id='cum',
    schema='esse',
    table='ipsum',
)

res = s.connector_schema_management.connector_column_config(req)

if res.connector_column_config_200_application_json_object is not None:
    # handle response
```

## connector_schema_config

Returns the connector schema config for an existing connector within your Fivetran account

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


req = operations.ConnectorSchemaConfigRequest(
    accept='application/json',
    connector_id='excepturi',
)

res = s.connector_schema_management.connector_schema_config(req)

if res.connector_schema_config_200_application_json_object is not None:
    # handle response
```

## modify_connector_column_config

Updates the column config within your table for an existing connector within your Fivetran account

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


req = operations.ModifyConnectorColumnConfigRequest(
    accept='application/json',
    column_update_request=shared.ColumnUpdateRequest(
        enabled=False,
        hashed=False,
    ),
    column_name='aspernatur',
    connector_id='perferendis',
    schema_name='ad',
    table_name='natus',
)

res = s.connector_schema_management.modify_connector_column_config(req)

if res.modify_connector_column_config_200_application_json_object is not None:
    # handle response
```

## modify_connector_database_schema_config

Updates the database schema config for an existing connector within your Fivetran account (for a single schema within a connector with multiple schemas)

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


req = operations.ModifyConnectorDatabaseSchemaConfigRequest(
    accept='application/json',
    schema_update_request=shared.SchemaUpdateRequest(
        enabled=False,
        tables={
            "iste": shared.TableUpdateRequest(
                columns={
                    "natus": shared.ColumnUpdateRequest(
                        enabled=False,
                        hashed=False,
                    ),
                },
                enabled=False,
                sync_mode=shared.TableUpdateRequestSyncModeEnum.HISTORY,
            ),
        },
    ),
    connector_id='hic',
    schema_name='saepe',
)

res = s.connector_schema_management.modify_connector_database_schema_config(req)

if res.modify_connector_database_schema_config_200_application_json_object is not None:
    # handle response
```

## modify_connector_schema_config

Updates the schema config for an existing connector within your Fivetran account (for a single schema for a connector with multiple schemas)

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


req = operations.ModifyConnectorSchemaConfigRequest(
    accept='application/json',
    standard_config_update_request=shared.StandardConfigUpdateRequest(
        schema_change_handling=shared.StandardConfigUpdateRequestSchemaChangeHandlingEnum.BLOCK_ALL,
        schemas={
            "corporis": shared.SchemaUpdateRequest(
                enabled=False,
                tables={
                    "iure": shared.TableUpdateRequest(
                        columns={
                            "quidem": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "architecto": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "ipsa": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "reiciendis": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                        },
                        enabled=False,
                        sync_mode=shared.TableUpdateRequestSyncModeEnum.LIVE,
                    ),
                    "mollitia": shared.TableUpdateRequest(
                        columns={
                            "dolores": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "dolorem": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "corporis": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                        },
                        enabled=False,
                        sync_mode=shared.TableUpdateRequestSyncModeEnum.SOFT_DELETE,
                    ),
                    "nobis": shared.TableUpdateRequest(
                        columns={
                            "omnis": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "nemo": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                        },
                        enabled=False,
                        sync_mode=shared.TableUpdateRequestSyncModeEnum.SOFT_DELETE,
                    ),
                },
            ),
            "excepturi": shared.SchemaUpdateRequest(
                enabled=False,
                tables={
                    "iure": shared.TableUpdateRequest(
                        columns={
                            "doloribus": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "sapiente": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                            "architecto": shared.ColumnUpdateRequest(
                                enabled=False,
                                hashed=False,
                            ),
                        },
                        enabled=False,
                        sync_mode=shared.TableUpdateRequestSyncModeEnum.HISTORY,
                    ),
                },
            ),
        },
    ),
    connector_id='dolorem',
)

res = s.connector_schema_management.modify_connector_schema_config(req)

if res.modify_connector_schema_config_200_application_json_object is not None:
    # handle response
```

## modify_connector_table_config

Updates the table config within your database schema for an existing connector within your Fivetran account

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


req = operations.ModifyConnectorTableConfigRequest(
    accept='application/json',
    table_update_request=shared.TableUpdateRequest(
        columns={
            "consequuntur": shared.ColumnUpdateRequest(
                enabled=False,
                hashed=False,
            ),
            "repellat": shared.ColumnUpdateRequest(
                enabled=False,
                hashed=False,
            ),
            "mollitia": shared.ColumnUpdateRequest(
                enabled=False,
                hashed=False,
            ),
        },
        enabled=False,
        sync_mode=shared.TableUpdateRequestSyncModeEnum.HISTORY,
    ),
    connector_id='numquam',
    schema_name='commodi',
    table_name='quam',
)

res = s.connector_schema_management.modify_connector_table_config(req)

if res.modify_connector_table_config_200_application_json_object is not None:
    # handle response
```

## reload_connector_schema_config

Reloads the connector schema config for an existing connector within your Fivetran account

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


req = operations.ReloadConnectorSchemaConfigRequest(
    accept='application/json',
    reload_standard_config_request=shared.ReloadStandardConfigRequest(
        exclude_mode='molestiae',
    ),
    connector_id='velit',
)

res = s.connector_schema_management.reload_connector_schema_config(req)

if res.reload_connector_schema_config_200_application_json_object is not None:
    # handle response
```

## resync_tables

Triggers a historical sync of all data for multiple schema tables within a connector. This action does not override the standard sync frequency you defined in the Fivetran dashboard.

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


req = operations.ResyncTablesRequest(
    accept='application/json',
    request_body={
        "quia": [
            'vitae',
            'laborum',
        ],
        "animi": [
            'odit',
            'quo',
        ],
        "sequi": [
            'ipsam',
            'id',
            'possimus',
            'aut',
        ],
    },
    connector_id='quasi',
)

res = s.connector_schema_management.resync_tables(req)

if res.resync_tables_200_application_json_object is not None:
    # handle response
```
