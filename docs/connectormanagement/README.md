# connector_management

### Available Operations

* [connect_card](#connect_card) - Connect Card
* [connector_details](#connector_details) - Retrieve Connector Details
* [create_connector](#create_connector) - Create a Connector
* [delete_connector](#delete_connector) - Delete a Connector
* [metadata_connector_config](#metadata_connector_config) - Retrieve connector configuration metadata
* [metadata_connectors](#metadata_connectors) - Retrieve source metadata
* [modify_connector](#modify_connector) - Modify a Connector
* [resync_connector](#resync_connector) - Re-sync Connector Data (Historical Sync)
* [run_setup_tests](#run_setup_tests) - Run connector setup tests
* [sync_connector](#sync_connector) - Sync Connector Data

## connect_card

Generates the Connect Card URI for the connector

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


req = operations.ConnectCardRequest(
    accept="application/json;version=2",
    connect_card_config_request=shared.ConnectCardConfigRequest(
        connect_card_config=shared.ConnectCardConfig(
            hide_setup_guide=False,
            redirect_uri="iure",
        ),
    ),
    connector_id="magnam",
)

res = s.connector_management.connect_card(req)

if res.connect_card_200_application_json_object is not None:
    # handle response
```

## connector_details

Returns a connector object if a valid identifier was provided

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


req = operations.ConnectorDetailsRequest(
    accept="application/json;version=2",
    connector_id="debitis",
)

res = s.connector_management.connector_details(req)

if res.connector_details_200_application_json_object is not None:
    # handle response
```

## create_connector

Creates a new connector within a specified group in your Fivetran account. Runs setup tests and returns testing results.

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


req = operations.CreateConnectorRequest(
    accept="application/json;version=2",
    new_connector_request_v1=shared.NewConnectorRequestV1(
        connect_card_config=shared.ConnectCardConfig(
            hide_setup_guide=False,
            redirect_uri="ipsa",
        ),
        daily_sync_time="delectus",
        group_id="tempora",
        pause_after_trial=False,
        paused=False,
        run_setup_tests=False,
        schedule_type="suscipit",
        service="molestiae",
        sync_frequency="480",
        trust_certificates=False,
        trust_fingerprints=False,
    ),
)

res = s.connector_management.create_connector(req)

if res.create_connector_201_application_json_object is not None:
    # handle response
```

## delete_connector

Deletes a connector from your Fivetran account.

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


req = operations.DeleteConnectorRequest(
    accept="application/json;version=2",
    connector_id="placeat",
)

res = s.connector_management.delete_connector(req)

if res.delete_connector_200_application_json_object is not None:
    # handle response
```

## metadata_connector_config

Returns metadata of configuration parameters and authorization parameters for a specified connector type.

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


req = operations.MetadataConnectorConfigRequest(
    accept="application/json;version=2",
    name="Ted Mante",
    service="temporibus",
)

res = s.connector_management.metadata_connector_config(req)

if res.metadata_connector_config_200_application_json_object is not None:
    # handle response
```

## metadata_connectors

Returns all available source types within your Fivetran account. This endpoint makes it easier to display Fivetran connectors within your application because it provides metadata including the proper source name (‘Facebook Ad Account’ instead of facebook_ad_account), the source icon, and links to Fivetran resources. As we update source names and icons, that metadata will automatically update within this endpoint

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


req = operations.MetadataConnectorsRequest(
    accept="application/json;version=2",
    cursor="ab",
    limit=337396,
    name="Iris Aufderhar",
)

res = s.connector_management.metadata_connectors(req)

if res.metadata_connectors_200_application_json_object is not None:
    # handle response
```

## modify_connector

Updates the information for an existing connector within your Fivetran account.

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


req = operations.ModifyConnectorRequest(
    accept="application/json;version=2",
    update_connector_request=shared.UpdateConnectorRequest(
        auth="sapiente",
        config="quo",
        daily_sync_time="odit",
        is_historical_sync=False,
        pause_after_trial=False,
        paused=False,
        paused_after_trial=False,
        run_setup_tests=False,
        schedule_type="manual",
        schema_status="at",
        sync_frequency="1440",
        trust_certificates=False,
        trust_fingerprints=False,
    ),
    connector_id="molestiae",
)

res = s.connector_management.modify_connector(req)

if res.modify_connector_200_application_json_object is not None:
    # handle response
```

## resync_connector

Triggers a full historical sync of a connector or multiple schema tables within a connector. If the connector is paused, the table sync will be scheduled to be performed when the connector is re-enabled. If there is a data sync already in progress, we will try to complete it. If it fails, the request will be declined and the HTTP 409 Conflict error will be returned.

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


req = operations.ResyncConnectorRequest(
    accept="application/json;version=2",
    resync_connector_request=shared.ResyncConnectorRequest(
        scope={
            "quod": [
                "totam",
                "porro",
            ],
            "dolorum": [
                "nam",
            ],
            "officia": [
                "fugit",
                "deleniti",
                "hic",
            ],
            "optio": [
                "beatae",
                "commodi",
                "molestiae",
            ],
        },
    ),
    connector_id="modi",
)

res = s.connector_management.resync_connector(req)

if res.resync_connector_200_application_json_object is not None:
    # handle response
```

## run_setup_tests

Runs the setup tests for an existing connector within your Fivetran account.

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


req = operations.RunSetupTestsRequest(
    accept="application/json;version=2",
    run_setup_tests_request=shared.RunSetupTestsRequest(
        trust_certificates=False,
        trust_fingerprints=False,
    ),
    connector_id="qui",
)

res = s.connector_management.run_setup_tests(req)

if res.run_setup_tests_200_application_json_object is not None:
    # handle response
```

## sync_connector

Triggers a data sync for an existing connector within your Fivetran account without waiting for the next scheduled sync. This action does not override the standard sync frequency you defined in the Fivetran dashboard.

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


req = operations.SyncConnectorRequest(
    accept="application/json;version=2",
    sync_connector_request=shared.SyncConnectorRequest(
        force=False,
    ),
    connector_id="impedit",
)

res = s.connector_management.sync_connector(req)

if res.sync_connector_200_application_json_object is not None:
    # handle response
```
