from OpenSSL import crypto

def create_csr(common_name, country, state, localty, organization, organizational_unit, key_size):
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, int(key_size))

    req = crypto.X509Req()
    req.get_subject().CN = common_name
    req.get_subject().C = country
    req.get_subject().ST = state
    req.get_subject().L = localty
    req.get_subject().O = organization
    req.get_subject().OU = organizational_unit

    req.set_pubkey(key)
    req.sign(key, 'sha256')

    priv_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)
    csr = crypto.dump_certificate_request(crypto.FILETYPE_PEM, req)

    return priv_key, csr

def decode_csr(csr):
    result = {}
    err = None

    try:
        req = crypto.load_certificate_request(crypto.FILETYPE_PEM, csr)
    except Exception as e:
        if hasattr(e, 'message'):
            err = e.message
        else:
            err = e

        print(type(err))
    else:
        key = req.get_pubkey()
        key_type = 'RSA' if key.type() == crypto.TYPE_RSA else 'DSA'
        subject = req.get_subject()
        components = dict(subject.get_components())

        result.update({"Common Name": components[b'CN'].decode('utf-8')})
        result.update({"Country": components[b'C'].decode('utf-8')})
        result.update({"State": components[b'ST'].decode('utf-8')})
        result.update({"Localty": components[b'L'].decode('utf-8')})
        result.update({"Organization": components[b'O'].decode('utf-8')})
        result.update({"Organizational Unit": components[b'OU'].decode('utf-8')})

    return result, err
