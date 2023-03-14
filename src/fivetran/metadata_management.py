import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class MetadataManagement:
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
        
    def column_metadata(self, request: operations.ColumnMetadataRequest) -> operations.ColumnMetadataResponse:
        r"""Retrieve column metadata
        Returns column-level metadata for an existing connector within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ColumnMetadataRequest, base_url, '/v1/metadata/connectors/{connectorId}/columns', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ColumnMetadataRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ColumnMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.column_metadata_200_application_json_any = out

        return res

    def schema_metadata(self, request: operations.SchemaMetadataRequest) -> operations.SchemaMetadataResponse:
        r"""Retrieve schema metadata
        Returns schema-level metadata for an existing connector within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.SchemaMetadataRequest, base_url, '/v1/metadata/connectors/{connectorId}/schemas', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.SchemaMetadataRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SchemaMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.schema_metadata_200_application_json_any = out

        return res

    def table_metadata(self, request: operations.TableMetadataRequest) -> operations.TableMetadataResponse:
        r"""Retrieve table metadata
        Returns table-level metadata for an existing connector within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TableMetadataRequest, base_url, '/v1/metadata/connectors/{connectorId}/tables', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.TableMetadataRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TableMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.table_metadata_200_application_json_any = out

        return res

    