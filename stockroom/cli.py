import json
import sys

from stockroom.entity import Order
from stockroom.serializer import to_dict


def run(argv):
    opts = {}
    it = iter(argv)
    for flag in it:
        opts[flag.lstrip("-")] = next(it)
    rec = Order(
        id=int(opts.get("id", 0)),
        title=opts["title"],
        status=opts.get("status", "open"),
    )
    return json.dumps(to_dict(rec), sort_keys=True)


if __name__ == "__main__":
    print(run(sys.argv[1:]))
