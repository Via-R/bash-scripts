import json, argparse

parser = argparse.ArgumentParser(description="Specify the target you want to connect to")
parser.add_argument("--target", type=str, default=None, required=True)
args = parser.parse_args()

def read_entry():
    with open("json/ssh.json", "r") as f:
        db = json.loads(f.read())
        target = db.get(args.target)
        if target is None:
            return None
        return f'{target["username"]} {target["ip"]} {target["password"]} {target["is_pem"]}'
        f.close()

print(read_entry())