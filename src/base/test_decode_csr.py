from .csrtools import decode_csr

data = '''-----BEGIN CERTIFICATE REQUEST-----
MIICtzCCAZ8CAQAwcjEYMBYGA1UEAwwPd3d3LmV4YW1wbGUuY29tMQswCQYDVQQG
EwJJRDESMBAGA1UECAwJRWFzdCBKYXZhMREwDwYDVQQHDAhTdXJhYmF5YTEVMBMG
A1UECgwMRXhhbXBsZSBJbmMuMQswCQYDVQQLDAJJVDCCASIwDQYJKoZIhvcNAQEB
BQADggEPADCCAQoCggEBAKW9djfi2dydxzK12HTPJOLgWUrrhSAdh6eGI7I2FW2n
do+TTcvUUaTMsMbreJRLH9nyK5sutyNr1fgqjkuCMYFqIrycmHmt7qpMeZz6tekt
HIbqevYIA3gUZrS2xL6uMq1sCztMIuM09eHGwiZdptwnICj24+z0WGodylCCKTBa
0H5oUUNI59goztRGTyyVfuQlgRCUjHyvzhERHIEieRXSAHwUT4nmIND3j/AkJW6x
j503z3imZKVgaIB8pUnr+te58Dl2JFkoXnlZ/GJNE7PKRf6d31n2d9JjY5B+4p5U
VnnpbyqX1yioyxMt2DYJOYt1BXBu+p4722OyWnjITuUCAwEAAaAAMA0GCSqGSIb3
DQEBCwUAA4IBAQBGRT+gcjwKa5OQkAUnolkFKqSf4D2G8Wflq5ztlWvmKo/eNDni
ChCn4GFIfEkvqiY6mc0xAvpYdClKlR4FNPpbpCWFfbZ1AQb8bqWJgsLU8dq/DbDi
4aIJ9JKInXJMFYS/Te8le4JDLoBxwCy3Rq9RI48S5Q0fs5vzdQeM+2sMNcG1e+sY
v+WrrwoSXPdici8c07aqodH2zVPrIqHGnPr2K9x6JNd3N6uxS1R4p7mySmaOvMbI
J7Eq3N1X0naslk3mjwwQsW3XM9/tZd6aKNvP5ZSbsyoP3GwIZlx842/7Q8Q7yrRK
kOcmvqlVGuujvI1YMl0uVlX7fjmVk7f4R0Pw
-----END CERTIFICATE REQUEST-----'''

data_incorrect = '''-----BEGIN CERTIFICATE REQUEST-----
MIICtzCCAZ8CAQAwcjEYMBYGA1UEAwwPd3d3LmV4YW1wbGUuY29tMQswCQYDVQQG
BQADggEPADCCAQoCggEBAKW9djfi2dydxzK12HTPJOLgWUrrhSAdh6eGI7I2FW2n
do+TTcvUUaTMsMbreJRLH9nyK5sutyNr1fgqjkuCMYFqIrycmHmt7qpMeZz6tekt
kOcmvqlVGuujvI1YMl0uVlX7fjmVk7f4R0Pw
-----END CERTIFICATE REQUEST-----'''

def test_csr_common_name():    
    assert decode_csr(bytes(data, 'utf-8'))['Common Name'] == 'www.example.com'

def test_csr_country():    
    assert decode_csr(bytes(data, 'utf-8'))['Country'] == 'ID'

def test_csr_state():    
    assert decode_csr(bytes(data, 'utf-8'))['State'] == 'East Java'

def test_csr_localty():    
    assert decode_csr(bytes(data, 'utf-8'))['Localty'] == 'Surabaya'

def test_csr_organization():     
    assert decode_csr(bytes(data, 'utf-8'))['Organization'] == 'Example Inc.'

def test_csr_organizational_unit():    
    assert decode_csr(bytes(data, 'utf-8'))['Organizational Unit'] == 'IT'
