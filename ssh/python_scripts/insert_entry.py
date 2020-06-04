import json, argparse
import os

parser = argparse.ArgumentParser(description="Specify the target you want to connect to")
parser.add_argument("--target", type=str, default=None, required=True)
parser.add_argument("--ip", type=str, default=None, required=True)
parser.add_argument("--username", type=str, default=None, required=True)
parser.add_argument("--password", type=str, default=None, required=True)
parser.add_argument("--is_pem", type=bool, default=False)
args = parser.parse_args()

ssh_file = "json/ssh.json"
ssh_folder = "json"
pem_folder = "pem"

if not os.path.exists(ssh_folder):
    os.makedirs(ssh_folder)

if not os.path.isfile(ssh_file):
    with open(ssh_file, "w") as fd:
        fd.write(json.dumps(dict()))
        fd.close()

with open(ssh_file, "r+") as frp:
    db = json.loads(frp.read())
    password = args.password
    if args.is_pem:
        password = f"{pem_folder}/{password}.pem"
    db[args.target] = {"ip":args.ip, "username":args.username, "password":password, "is_pem":args.is_pem}
    frp.seek(0)
    frp.write(json.dumps(db))
    frp.close()