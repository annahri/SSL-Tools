from dataclasses import dataclass, field
from OpenSSL import crypto

@dataclass
class CSR:
    common_name: str 
    country: str
    state: str
    localty: str
    organization: str
    organizational_unit: str
    _private_key: str = field(init=False)
    _csr: str = field(init=False)
    key_size: int = 2048

    def __post_init__(self) -> None:
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, int(self.key_size))

        req = crypto.X509Req()
        req.get_subject().CN = self.common_name
        req.get_subject().C = self.country
        req.get_subject().ST = self.state
        req.get_subject().L = self.localty
        req.get_subject().O = self.organization
        req.get_subject().OU = self.organizational_unit

        req.set_pubkey(key)
        req.sign(key, 'sha256')

        self._private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode('utf-8')
        self._csr = crypto.dump_certificate_request(crypto.FILETYPE_PEM, req).decode('utf-8')

    def get_privkey(self) -> str:
        return self._private_key

    def get_csr(self) -> str:
        return self._csr

def decode_csr(csr):
    result = {}
    err = None

    try:
        req = crypto.load_certificate_request(crypto.FILETYPE_PEM, csr)
    except Exception as e:
        err = e
        print(type(e))
    else:
        subject = req.get_subject()
        components = dict(subject.get_components())

        result.update({"Common Name": components[b'CN'].decode('utf-8')})
        result.update({"Country": components[b'C'].decode('utf-8')})
        result.update({"State": components[b'ST'].decode('utf-8')})
        result.update({"Localty": components[b'L'].decode('utf-8')})
        result.update({"Organization": components[b'O'].decode('utf-8')})
        result.update({"Organizational Unit": components[b'OU'].decode('utf-8')})

    return result, err
