"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .certificate_management import CertificateManagement
from .connector_management import ConnectorManagement
from .connector_schema_management import ConnectorSchemaManagement
from .dbt_transformation_management import DBTTransformationManagement
from .destination_management import DestinationManagement
from .group_management import GroupManagement
from .metadata_management import MetadataManagement
from .role_management import RoleManagement
from .team_management import TeamManagement
from .user_management import UserManagement
from .webhook_management import WebhookManagement
from fivetran.models import shared

SERVERS = [
    "https://api.fivetran.com",
]
"""Contains the list of servers available to the SDK"""

class Fivetran:
    r"""The OpenAPI Specification is a standard format to define the structure and syntax of REST APIs. OpenAPI documents are both machine and human-readable, which enables anyone to easily determine how each API works. [More details](https://www.openapis.org/faq)"""
    certificate_management: CertificateManagement
    connector_management: ConnectorManagement
    connector_schema_management: ConnectorSchemaManagement
    dbt_transformation_management: DBTTransformationManagement
    destination_management: DestinationManagement
    group_management: GroupManagement
    metadata_management: MetadataManagement
    role_management: RoleManagement
    team_management: TeamManagement
    user_management: UserManagement
    webhook_management: WebhookManagement

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.7.0"
    _gen_version: str = "2.13.1"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.certificate_management = CertificateManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.connector_management = ConnectorManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.connector_schema_management = ConnectorSchemaManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.dbt_transformation_management = DBTTransformationManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.destination_management = DestinationManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.group_management = GroupManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.metadata_management = MetadataManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.role_management = RoleManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.team_management = TeamManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user_management = UserManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhook_management = WebhookManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    