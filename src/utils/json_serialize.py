from fastapi import Response
import json


def json_serialize(obj):
    json_obj = json.dumps(obj, default=str)
    return Response(content=json_obj, media_type="application/json")
