import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class ConnectorManagement:
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
        
    def connect_card(self, request: operations.ConnectCardRequest) -> operations.ConnectCardResponse:
        r"""Connect Card
        Generates the Connect Card URI for the connector
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ConnectCardRequest, base_url, '/v1/connectors/{connectorId}/connect-card', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "connect_card_config_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConnectCardResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.connect_card_200_application_json_any = out

        return res

    def connector_details(self, request: operations.ConnectorDetailsRequest) -> operations.ConnectorDetailsResponse:
        r"""Retrieve Connector Details
        Returns a connector object if a valid identifier was provided
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ConnectorDetailsRequest, base_url, '/v1/connectors/{connectorId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ConnectorDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.connector_details_200_application_json_any = out

        return res

    def create_connector(self, request: operations.CreateConnectorRequest) -> operations.CreateConnectorResponse:
        r"""Create a Connector
        Creates a new connector within a specified group in your Fivetran account. Runs setup tests and returns testing results.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/connectors'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "new_connector_request_v1", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_connector_201_application_json_any = out
        elif http_res.status_code == 400:
            pass

        return res

    def delete_connector(self, request: operations.DeleteConnectorRequest) -> operations.DeleteConnectorResponse:
        r"""Delete a Connector
        Deletes a connector from your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteConnectorRequest, base_url, '/v1/connectors/{connectorId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_connector_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def metadata_connector_config(self, request: operations.MetadataConnectorConfigRequest) -> operations.MetadataConnectorConfigResponse:
        r"""Retrieve connector configuration metadata
        Returns metadata of configuration parameters and authorization parameters for a specified connector type.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.MetadataConnectorConfigRequest, base_url, '/v1/metadata/{name}/{service}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MetadataConnectorConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.metadata_connector_config_200_application_json_any = out

        return res

    def metadata_connectors(self, request: operations.MetadataConnectorsRequest) -> operations.MetadataConnectorsResponse:
        r"""Retrieve source metadata
        Returns all available source types within your Fivetran account. This endpoint makes it easier to display Fivetran connectors within your application because it provides metadata including the proper source name (‘Facebook Ad Account’ instead of facebook_ad_account), the source icon, and links to Fivetran resources. As we update source names and icons, that metadata will automatically update within this endpoint
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.MetadataConnectorsRequest, base_url, '/v1/metadata/{name}', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.MetadataConnectorsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MetadataConnectorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.metadata_connectors_200_application_json_any = out

        return res

    def modify_connector(self, request: operations.ModifyConnectorRequest) -> operations.ModifyConnectorResponse:
        r"""Modify a Connector
        Updates the information for an existing connector within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyConnectorRequest, base_url, '/v1/connectors/{connectorId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "update_connector_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_connector_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def resync_connector(self, request: operations.ResyncConnectorRequest) -> operations.ResyncConnectorResponse:
        r"""Re-sync Connector Data (Historical Sync)
        Triggers a full historical sync of a connector or multiple schema tables within a connector. If the connector is paused, the table sync will be scheduled to be performed when the connector is re-enabled. If there is a data sync already in progress, we will try to complete it. If it fails, the request will be declined and the HTTP 409 Conflict error will be returned.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ResyncConnectorRequest, base_url, '/v1/connectors/{connectorId}/resync', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "resync_connector_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ResyncConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.resync_connector_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def run_setup_tests(self, request: operations.RunSetupTestsRequest) -> operations.RunSetupTestsResponse:
        r"""Run connector setup tests
        Runs the setup tests for an existing connector within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.RunSetupTestsRequest, base_url, '/v1/connectors/{connectorId}/test', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "run_setup_tests_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RunSetupTestsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.run_setup_tests_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def sync_connector(self, request: operations.SyncConnectorRequest) -> operations.SyncConnectorResponse:
        r"""Sync Connector Data
        Triggers a data sync for an existing connector within your Fivetran account without waiting for the next scheduled sync. This action does not override the standard sync frequency you defined in the Fivetran dashboard.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SyncConnectorRequest, base_url, '/v1/connectors/{connectorId}/sync', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "sync_connector_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SyncConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.sync_connector_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    