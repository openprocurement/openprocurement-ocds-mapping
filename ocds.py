import json
import yaml
import sys
from jsonschema import RefResolver

from galleon import Mapper


with open('test-data/tender-with-lots.json') as _in:
    tender = json.load(_in)

with open('schemas/1.1-extended-schema.json') as _in:
    schema = json.load(_in)


with open('mapping/1.1-pure.yaml') as _in:
    mapping = yaml.load(_in)

resolver = RefResolver.from_schema(schema)

mapper = Mapper(mapping, resolver)
sys.stdout.write(json.dumps(mapper.apply(tender)))
