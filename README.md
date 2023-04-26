<div align="center">
    <img src="https://user-images.githubusercontent.com/68016351/223284832-d571065b-026c-46d4-88a6-a895afeb8c97.png" width="500">
    <p>Fivetran makes access to data as simple and reliable as electricity, and our REST API makes it automatable! With our API, you can build a data-driven applications on top of our platform with Powered by Fivetran </p>
    <a href="https://developers.fivetran.com/openapi/reference/v1/overview/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
    <a href="https://github.com/speakeasy-sdks/fivetran-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/fivetran-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
    <a href="https://github.com/speakeasy-sdks/fivetran-python-sdk/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/fivetran-python-sdk?sort=semver&style=for-the-badge"/></a>
</div>

[![Run on Repl.it](https://repl.it/badge/github/speakeasy-sdks/fivetran-python-sdk)](https://replit.com/join/bgzdebsgjh-sagarbatchu1)

## Authentication

Account Administrators in Free, Standard, Enterprise, and Business Critical accounts can manage the API configuration settings. To access the API configuration settings:

1) Log in to [Fivetran](https://fivetran.com/login).
2) In the bottom left menu, click on your username, then click API Key to access your user-level API key and secret.

Fivetran REST API uses API Key authentication. For each request to the API provide an Authorization HTTP header with the following value: Basic `{api_key}:{api_secret}`. The `{api_key}:{api_secret}` part should be base64 encoded.

For instance, for API key `d9c4511349dd4b86` and API secret `1f6f2d161365888a1943160ccdb8d968`, encode d`9c4511349dd4b86:1f6f2d161365888a1943160ccdb8d968` to base64 `(ZDljNDUxMTM0OWRkNGI4NjoxZjZmMmQxNjEzNjU4ODhhMTk0MzE2MGNjZGI4ZDk2OA==)` and use the following Authorization HTTP header value:

`Basic ZDljNDUxMTM0OWRkNGI4NjoxZjZmMmQxNjEzNjU4ODhhMTk0MzE2MGNjZGI4ZDk2OA==`

NOTE: The API key is unique for the account and Account Administrator user pair. Different Account Administrators have different API keys.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ApproveCertificateRequest(
    accept="application/json",
    trust_certificate_request=shared.TrustCertificateRequest(
        connector_id="corrupti",
        destination_id="provident",
        encoded_cert="distinctio",
        hash="quibusdam",
    ),
)

res = s.certificate_management.approve_certificate(req)

if res.approve_certificate_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [certificate_management](docs/certificatemanagement/README.md)

* [approve_certificate](docs/certificatemanagement/README.md#approve_certificate) - Approve a certificate
* [approve_fingerprint](docs/certificatemanagement/README.md#approve_fingerprint) - Approve a fingerprint

### [connector_management](docs/connectormanagement/README.md)

* [connect_card](docs/connectormanagement/README.md#connect_card) - Connect Card
* [connector_details](docs/connectormanagement/README.md#connector_details) - Retrieve Connector Details
* [create_connector](docs/connectormanagement/README.md#create_connector) - Create a Connector
* [delete_connector](docs/connectormanagement/README.md#delete_connector) - Delete a Connector
* [metadata_connector_config](docs/connectormanagement/README.md#metadata_connector_config) - Retrieve connector configuration metadata
* [metadata_connectors](docs/connectormanagement/README.md#metadata_connectors) - Retrieve source metadata
* [modify_connector](docs/connectormanagement/README.md#modify_connector) - Modify a Connector
* [resync_connector](docs/connectormanagement/README.md#resync_connector) - Re-sync Connector Data (Historical Sync)
* [run_setup_tests](docs/connectormanagement/README.md#run_setup_tests) - Run connector setup tests
* [sync_connector](docs/connectormanagement/README.md#sync_connector) - Sync Connector Data

### [connector_schema_management](docs/connectorschemamanagement/README.md)

* [connector_column_config](docs/connectorschemamanagement/README.md#connector_column_config) - Retrieve Source Table Columns Config
* [connector_schema_config](docs/connectorschemamanagement/README.md#connector_schema_config) - Retrieve a Connector Schema Config
* [modify_connector_column_config](docs/connectorschemamanagement/README.md#modify_connector_column_config) - Modify a Connector Column Config
* [modify_connector_database_schema_config](docs/connectorschemamanagement/README.md#modify_connector_database_schema_config) - Modify a Connector Database Schema Config
* [modify_connector_schema_config](docs/connectorschemamanagement/README.md#modify_connector_schema_config) - Modify a Connector Schema Config
* [modify_connector_table_config](docs/connectorschemamanagement/README.md#modify_connector_table_config) - Modify a Connector Table Config
* [reload_connector_schema_config](docs/connectorschemamanagement/README.md#reload_connector_schema_config) - Reload a Connector Schema Config
* [resync_tables](docs/connectorschemamanagement/README.md#resync_tables) - Re-sync Connector Table Data

### [dbt_transformation_management](docs/dbttransformationmanagement/README.md)

* [create_dbt_project](docs/dbttransformationmanagement/README.md#create_dbt_project) - Create DBT Project
* [create_dbt_transformation](docs/dbttransformationmanagement/README.md#create_dbt_transformation) - Create DBT Transformation
* [dbt_model_details](docs/dbttransformationmanagement/README.md#dbt_model_details) - Retrieve DBT Model Details
* [dbt_project_details](docs/dbttransformationmanagement/README.md#dbt_project_details) - Retrieve DBT Project Details
* [dbt_transformation_details](docs/dbttransformationmanagement/README.md#dbt_transformation_details) - Retrieve DBT Transformation Details
* [delete_dbt_transformation](docs/dbttransformationmanagement/README.md#delete_dbt_transformation) - Delete DBT Transformation
* [list_dbt_project_models](docs/dbttransformationmanagement/README.md#list_dbt_project_models) - List All DBT Models
* [list_dbt_project_transformations](docs/dbttransformationmanagement/README.md#list_dbt_project_transformations) - List All DBT Transformations
* [list_dbt_projects](docs/dbttransformationmanagement/README.md#list_dbt_projects) - List All DBT Projects
* [modify_dbt_transformation](docs/dbttransformationmanagement/README.md#modify_dbt_transformation) - Modify DBT Transformation
* [test_dbt_project](docs/dbttransformationmanagement/README.md#test_dbt_project) - Test DBT Project

### [destination_management](docs/destinationmanagement/README.md)

* [create_destination](docs/destinationmanagement/README.md#create_destination) - Create destination
* [delete_destination](docs/destinationmanagement/README.md#delete_destination) - Delete a destination
* [destination_details](docs/destinationmanagement/README.md#destination_details) - Retrieve Destination Details
* [modify_destination](docs/destinationmanagement/README.md#modify_destination) - Modify a Destination
* [run_destination_setup_tests](docs/destinationmanagement/README.md#run_destination_setup_tests) - Run Destination Setup Tests

### [group_management](docs/groupmanagement/README.md)

* [add_user_to_group](docs/groupmanagement/README.md#add_user_to_group) - Add a User to a Group
* [create_group](docs/groupmanagement/README.md#create_group) - Create a Group
* [delete_group](docs/groupmanagement/README.md#delete_group) - Delete a group
* [delete_user_from_group](docs/groupmanagement/README.md#delete_user_from_group) - Remove a User from a Group
* [group_details](docs/groupmanagement/README.md#group_details) - Retrieve Group Details
* [list_all_connectors_in_group](docs/groupmanagement/README.md#list_all_connectors_in_group) - List All Connectors within a Group
* [list_all_groups](docs/groupmanagement/README.md#list_all_groups) - List All Groups
* [list_all_users_in_group](docs/groupmanagement/README.md#list_all_users_in_group) - List All Users within a Group
* [modify_group](docs/groupmanagement/README.md#modify_group) - Modify a Group

### [metadata_management](docs/metadatamanagement/README.md)

* [column_metadata](docs/metadatamanagement/README.md#column_metadata) - Retrieve column metadata
* [schema_metadata](docs/metadatamanagement/README.md#schema_metadata) - Retrieve schema metadata
* [table_metadata](docs/metadatamanagement/README.md#table_metadata) - Retrieve table metadata

### [role_management](docs/rolemanagement/README.md)

* [list_all_roles](docs/rolemanagement/README.md#list_all_roles) - List all roles

### [team_management](docs/teammanagement/README.md)

* [add_team_membership_in_connector](docs/teammanagement/README.md#add_team_membership_in_connector) - Add connector membership
* [add_team_membership_in_group](docs/teammanagement/README.md#add_team_membership_in_group) - Add group membership
* [add_user_to_team](docs/teammanagement/README.md#add_user_to_team) - Add a user to a team
* [create_team](docs/teammanagement/README.md#create_team) - Create a team
* [delete_team](docs/teammanagement/README.md#delete_team) - Delete a team
* [delete_team_membership_in_account](docs/teammanagement/README.md#delete_team_membership_in_account) - Delete team role in account
* [delete_team_membership_in_connector](docs/teammanagement/README.md#delete_team_membership_in_connector) - Delete connector membership
* [delete_team_membership_in_group](docs/teammanagement/README.md#delete_team_membership_in_group) - Delete group membership
* [delete_user_from_team](docs/teammanagement/README.md#delete_user_from_team) - Delete a user from a team
* [get_team_membership_in_connector](docs/teammanagement/README.md#get_team_membership_in_connector) - Retrieve connector membership
* [get_team_membership_in_group](docs/teammanagement/README.md#get_team_membership_in_group) - Retrieve group membership
* [get_team_memberships_in_connectors](docs/teammanagement/README.md#get_team_memberships_in_connectors) - List all connector memberships
* [get_team_memberships_in_groups](docs/teammanagement/README.md#get_team_memberships_in_groups) - List all group memberships
* [get_user_in_team](docs/teammanagement/README.md#get_user_in_team) - Retrieve user membership in a team
* [list_all_teams](docs/teammanagement/README.md#list_all_teams) - List all teams
* [list_users_in_team](docs/teammanagement/README.md#list_users_in_team) - List all user memberships
* [modify_team](docs/teammanagement/README.md#modify_team) - Modify a team
* [team_details](docs/teammanagement/README.md#team_details) - Retrieve team details
* [update_team_membership_in_connector](docs/teammanagement/README.md#update_team_membership_in_connector) - Update connector membership
* [update_team_membership_in_group](docs/teammanagement/README.md#update_team_membership_in_group) - Update group membership
* [update_user_membership](docs/teammanagement/README.md#update_user_membership) - Modify a user membership

### [user_management](docs/usermanagement/README.md)

* [add_user_membership_in_connector](docs/usermanagement/README.md#add_user_membership_in_connector) - Add connector membership
* [add_user_membership_in_group](docs/usermanagement/README.md#add_user_membership_in_group) - Add group membership
* [create_user](docs/usermanagement/README.md#create_user) - Invite a User
* [delete_user](docs/usermanagement/README.md#delete_user) - Delete a user
* [delete_user_membership_in_account](docs/usermanagement/README.md#delete_user_membership_in_account) - Delete user role in account
* [delete_user_membership_in_connector](docs/usermanagement/README.md#delete_user_membership_in_connector) - Delete connector membership
* [delete_user_membership_in_group](docs/usermanagement/README.md#delete_user_membership_in_group) - Delete group membership
* [get_user_membership_in_connector](docs/usermanagement/README.md#get_user_membership_in_connector) - Retrieve connector membership
* [get_user_membership_in_group](docs/usermanagement/README.md#get_user_membership_in_group) - Retrieve group membership
* [get_user_memberships_in_connectors](docs/usermanagement/README.md#get_user_memberships_in_connectors) - List all connector memberships
* [get_user_memberships_in_groups](docs/usermanagement/README.md#get_user_memberships_in_groups) - List all group memberships
* [list_all_users](docs/usermanagement/README.md#list_all_users) - List All Users
* [modify_user](docs/usermanagement/README.md#modify_user) - Modify a User
* [update_user_membership_in_connector](docs/usermanagement/README.md#update_user_membership_in_connector) - Update connector membership
* [update_user_membership_in_group](docs/usermanagement/README.md#update_user_membership_in_group) - Update group membership
* [user_details](docs/usermanagement/README.md#user_details) - Retrieve User Details

### [webhook_management](docs/webhookmanagement/README.md)

* [create_account_webhook](docs/webhookmanagement/README.md#create_account_webhook) - Create account webhook
* [create_group_webhook](docs/webhookmanagement/README.md#create_group_webhook) - Create group webhook
* [delete_webhook](docs/webhookmanagement/README.md#delete_webhook) - Delete webhook
* [list_all_webhooks](docs/webhookmanagement/README.md#list_all_webhooks) - Retrieve the list of webhooks
* [modify_webhook](docs/webhookmanagement/README.md#modify_webhook) - Update webhook
* [test_webhook](docs/webhookmanagement/README.md#test_webhook) - Test webhook
* [webhook_details](docs/webhookmanagement/README.md#webhook_details) - Retrieve webhook details
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
