from flask import (Blueprint, jsonify, request)
from url_shortening_app.utils import url_utils

bp = Blueprint('url', __name__, url_prefix='/url')

"""
This is our 'database' of id to url and id to encoded.
When we restart app, it will get cleared. In the future, use a DB for persistence
"""
index_to_url = {}
index_to_encoded = {}

# I decided to use 2 routes to avoid overloading in 1 single route
"""
Input:
{
    "url": "https://my-very-long-url.com/this-here-is-a-very-long-url"
}

Output:
{
    "output": "https://change.co/b"
}
"""
@bp.route('/encode', methods=('POST',))
def encode():
    url = request.json['url']
    # encoded_value will be predictable
    # encoded_value could also be foul language
    d = url_utils.url_conversion('encode', url)
    encoded_value = d['encoded_value']
    unique_index = d['unique_index']

    index_to_url[unique_index] = url
    index_to_encoded[unique_index] = encoded_value

    shortened_url = 'https://change.co/{}'.format(encoded_value)
    return jsonify(output=shortened_url)

"""
Input:
{
    "url": "https://change.co/b"
}

Output:
{
    "output": "https://my-very-long-url.com/this-here-is-a-very-long-url"
}
"""
@bp.route('/decode', methods=('POST',))
def decode():
    url = request.json['url']
    decoded_value = url_utils.url_conversion('decode', url)
    original_url = 'Error in decoding'

    # The encoded value could not be our dictionary resulting in KeyError when finding it
    try:
        original_url = index_to_url[decoded_value]
    except KeyError as e:
        print('Key {} is not set'.format(e))
        return jsonify(output=original_url), 400

    return jsonify(output=original_url)

