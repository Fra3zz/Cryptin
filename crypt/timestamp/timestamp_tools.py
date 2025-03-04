import asn1tools
from base64 import b64encode
from hashlib import sha256
import pathlib


def make_timestamp_request(message:bytes):

    # Step 1: Compile the ASN.1 schema blueprint
    tsp = asn1tools.compile_files(str(pathlib.Path(__file__).parent / "tsp.asn"))

    # Step 2: Define the data to be encoded
    data = {
        'version': 1,
        'messageImprint': {
            'hashAlgorithm': {
                'algorithm': '1.3.14.3.2.26'  # OID for SHA-1 256
                # 'parameters': None  # Remove this line if parameters are not needed
            },
            'hashedMessage': sha256(message).digest() # Example hash value
        },
        #'reqPolicy': '1.3.6.1.4.1.12345.67.89.1',  # Example policy OID wors without it
        'nonce': 1234567890,
        'certReq': True,
        'extensions': []  # Use an empty list for optional extensions
    }

    return tsp.encode('TimeStampReq', data)

#Example usage
# with open("request.der", "wb") as f:
#     f.write(make_timestamp_request(b"Test"))
#     f.close()