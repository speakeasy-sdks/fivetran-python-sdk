# certificate_management

### Available Operations

* [approve_certificate](#approve_certificate) - Approve a certificate
* [approve_fingerprint](#approve_fingerprint) - Approve a fingerprint

## approve_certificate

Approves a certificate for a connector/destination, so Fivetran trusts this certificate for a source/destination database. The connector/destination setup tests will fail if a non-approved certificate is provided.

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

req = operations.ApproveCertificateRequest(
    accept='application/json',
    trust_certificate_request=shared.TrustCertificateRequest(
        connector_id='unde',
        destination_id='nulla',
        encoded_cert='corrupti',
        hash='illum',
    ),
)

res = s.certificate_management.approve_certificate(req)

if res.approve_certificate_200_application_json_object is not None:
    # handle response
```

## approve_fingerprint

Approves a fingerprint, so Fivetran trusts this fingerprint for a source/destination database, and connectors can connect to the source/destination through an SSH tunnel

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

req = operations.ApproveFingerprintRequest(
    accept='application/json',
    trust_fingerprint_request=shared.TrustFingerprintRequest(
        connector_id='vel',
        destination_id='error',
        hash='deserunt',
        public_key='suscipit',
    ),
)

res = s.certificate_management.approve_fingerprint(req)

if res.approve_fingerprint_200_application_json_object is not None:
    # handle response
```
