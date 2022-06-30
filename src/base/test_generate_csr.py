from base.csrtools import CSR

data = {
    'common_name': 'www.example.com',
    'country': 'ID',
    'state': 'Jawa Timur',
    'localty': 'Surabaya',
    'organization': 'Example inc.',
    'organizational_unit': 'IT'
}

def test_common_name():
    csr = CSR(**data, key_size=2048)
    assert csr.common_name == 'www.example.com'

def test_keysize_4096():
    csr = CSR(**data, key_size=4096)
    assert csr.key_size == 4096

def test_keysize_default():
    csr = CSR(**data)
    assert csr.key_size == 2048

def test_csr_header():
    csr = CSR(**data, key_size=2048)
    assert csr.request.startswith('-----BEGIN CERTIFICATE REQUEST-----')

def test_csr_footer():
    csr = CSR(**data, key_size=2048)
    assert csr.request.endswith('-----END CERTIFICATE REQUEST-----\n')

def test_privkey_header():
    csr = CSR(**data, key_size=2048)
    assert csr.private_key.startswith('-----BEGIN PRIVATE KEY-----')

def test_privkey_footer():
    csr = CSR(**data, key_size=2048)
    assert csr.private_key.endswith('-----END PRIVATE KEY-----\n')
