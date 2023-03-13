__doc__ = """ SDK Documentation: The OpenAPI Specification is a standard format to define the structure and syntax of REST APIs. OpenAPI documents are both machine and human-readable, which enables anyone to easily determine how each API works. [More details](https://www.openapis.org/faq)"""
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

class Fivetran:
    r"""SDK Documentation: The OpenAPI Specification is a standard format to define the structure and syntax of REST APIs. OpenAPI documents are both machine and human-readable, which enables anyone to easily determine how each API works. [More details](https://www.openapis.org/faq)"""
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
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.2.1"
    _gen_version: str = "1.9.2"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
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
        
    