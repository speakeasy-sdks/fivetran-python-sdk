import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class ConnectorSchemaManagement:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def connector_column_config(self, request: operations.ConnectorColumnConfigRequest) -> operations.ConnectorColumnConfigResponse:
        r"""Retrieve Source Table Columns Config
        Returns the source table columns config for an existing connector within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ConnectorColumnConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas/{schema}/tables/{table}/columns', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConnectorColumnConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.connector_column_config_200_application_json_any = out

        return res

    def connector_schema_config(self, request: operations.ConnectorSchemaConfigRequest) -> operations.ConnectorSchemaConfigResponse:
        r"""Retrieve a Connector Schema Config
        Returns the connector schema config for an existing connector within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ConnectorSchemaConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConnectorSchemaConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.connector_schema_config_200_application_json_any = out

        return res

    def modify_connector_column_config(self, request: operations.ModifyConnectorColumnConfigRequest) -> operations.ModifyConnectorColumnConfigResponse:
        r"""Modify a Connector Column Config
        Updates the column config within your table for an existing connector within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyConnectorColumnConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas/{schemaName}/tables/{tableName}/columns/{columnName}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyConnectorColumnConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_connector_column_config_200_application_json_any = out

        return res

    def modify_connector_database_schema_config(self, request: operations.ModifyConnectorDatabaseSchemaConfigRequest) -> operations.ModifyConnectorDatabaseSchemaConfigResponse:
        r"""Modify a Connector Database Schema Config
        Updates the database schema config for an existing connector within your Fivetran account (for a single schema within a connector with multiple schemas)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyConnectorDatabaseSchemaConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas/{schemaName}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyConnectorDatabaseSchemaConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_connector_database_schema_config_200_application_json_any = out

        return res

    def modify_connector_schema_config(self, request: operations.ModifyConnectorSchemaConfigRequest) -> operations.ModifyConnectorSchemaConfigResponse:
        r"""Modify a Connector Schema Config
        Updates the schema config for an existing connector within your Fivetran account (for a single schema for a connector with multiple schemas)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyConnectorSchemaConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyConnectorSchemaConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_connector_schema_config_200_application_json_any = out

        return res

    def modify_connector_table_config(self, request: operations.ModifyConnectorTableConfigRequest) -> operations.ModifyConnectorTableConfigResponse:
        r"""Modify a Connector Table Config
        Updates the table config within your database schema for an existing connector within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyConnectorTableConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas/{schemaName}/tables/{tableName}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyConnectorTableConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_connector_table_config_200_application_json_any = out

        return res

    def reload_connector_schema_config(self, request: operations.ReloadConnectorSchemaConfigRequest) -> operations.ReloadConnectorSchemaConfigResponse:
        r"""Reload a Connector Schema Config
        Reloads the connector schema config for an existing connector within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ReloadConnectorSchemaConfigRequest, base_url, '/v1/connectors/{connectorId}/schemas/reload', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReloadConnectorSchemaConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.reload_connector_schema_config_200_application_json_any = out

        return res

    def resync_tables(self, request: operations.ResyncTablesRequest) -> operations.ResyncTablesResponse:
        r"""Re-sync Connector Table Data
        Triggers a historical sync of all data for multiple schema tables within a connector. This action does not override the standard sync frequency you defined in the Fivetran dashboard.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ResyncTablesRequest, base_url, '/v1/connectors/{connectorId}/schemas/tables/resync', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ResyncTablesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.resync_tables_200_application_json_any = out

        return res

    