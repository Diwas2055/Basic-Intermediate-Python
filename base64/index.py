import base64

file = "base64/download.png"

def encode(file):
    """
    It opens the file in binary mode, reads the data, encodes it, and returns the encoded data as a
    string.
    
    :param file: The file to be encoded
    :return: the encoded_utf8 variable.
    """
    with open(file, 'rb') as file_binary:
        data = file_binary.read()
        encoded = base64.b64encode(data)
        encoded_utf8 = encoded.decode('utf-8')
        return encoded_utf8


def decode(file_base64):
    """
    It takes a base64 string, encodes it to utf-8, decodes it, and writes it to a file
    
    :param file_base64: The base64 string that you want to decode
    """
    file = "base64/testing.png"
    encoded = file_base64.encode('utf-8')
    with open(file, 'wb') as file:
        decoded_data = base64.decodebytes(encoded)
        file.write(decoded_data)

decode(encode(file))
