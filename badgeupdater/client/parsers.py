from django.conf import settings
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.utils import json


class BodyJSONParser(JSONParser):
    """
    Parses JSON-serialized data.
    """

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        request = parser_context.get('request')

        try:
            raw_data = stream.read()
            setattr(request, 'raw_body', raw_data)
            decoded_data = raw_data.decode(encoding)
            parse_constant = json.strict_constant if self.strict else None

            return json.loads(decoded_data, parse_constant=parse_constant)
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % str(exc))
