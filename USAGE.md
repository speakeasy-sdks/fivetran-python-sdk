<!-- Start SDK Example Usage -->
```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran()
s.config_security(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    )
)
   
req = operations.ApproveCertificateRequest(
    headers=operations.ApproveCertificateHeaders(
        accept="unde",
    ),
    request=shared.TrustCertificateRequest(
        connector_id="deserunt",
        destination_id="porro",
        encoded_cert="nulla",
        hash="id",
    ),
)
    
res = s.certificate_management.approve_certificate(req)

if res.approve_certificate_200_application_json_any is not None:
    # handle response
```
<!-- End SDK Example Usage -->