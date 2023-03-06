import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Any, Optional

class CertificateManagement:
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
        
    def approve_certificate(self, request: operations.ApproveCertificateRequest) -> operations.ApproveCertificateResponse:
        r"""Approve a certificate
        Approves a certificate for a connector/destination, so Fivetran trusts this certificate for a source/destination database. The connector/destination setup tests will fail if a non-approved certificate is provided.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/certificates'
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ApproveCertificateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.approve_certificate_200_application_json_any = out

        return res

    def approve_fingerprint(self, request: operations.ApproveFingerprintRequest) -> operations.ApproveFingerprintResponse:
        r"""Approve a fingerprint
        Approves a fingerprint, so Fivetran trusts this fingerprint for a source/destination database, and connectors can connect to the source/destination through an SSH tunnel
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/fingerprints'
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ApproveFingerprintResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.approve_fingerprint_200_application_json_any = out

        return res

    