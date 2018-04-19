import json
import yaml
import sys
from jsonschema import RefResolver

from galleon import Mapper


tender = json.loads(sys.stdin.read())
mapping = {}
schema = {}


for name, file in zip(
        ('pure', 'extended'),
        ('mapping/1.1-pure.yaml', 'mapping/1.1-extended.yaml')
        ):
    with open(file) as _in:
        mapping[name] = yaml.load(_in)

for name, file in zip(
        ('pure', 'extended'),
        ('schemas/1.1-schema.json', 'schemas/1.1-extended-schema.json')
        ):
    with open(file) as _in:
        schema[name] = json.load(_in)

try:
    name = sys.argv[1].strip()
    if (name not in schema) or (name not in mapping):
        raise
except:
    sys.stderr.write("Provide mapping name\n")
    sys.exit(1)

if __name__ == "__main__":
    resolver = RefResolver.from_schema(schema[name])
    mapper = Mapper(mapping[name], resolver)
    sys.stdout.write(json.dumps(mapper.apply(tender)))
