import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class RoleManagement:
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
        
    def list_all_roles(self, request: operations.ListAllRolesRequest) -> operations.ListAllRolesResponse:
        r"""List all roles
        Returns a list of all predefined and custom roles within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/roles'
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ListAllRolesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllRolesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_roles_200_application_json_any = out

        return res

    