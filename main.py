from QuickProject.Commander import Commander
import json

app = Commander()

def adjust(filepath: str):
    with open(filepath, 'r') as f:
        data = json.load(f)
    if 'server_target' not in data:
        return
    server_target = data.pop('server_target')
    if server_target[0]:
        ls = server_target[0].split('@')
        if len(ls) == 2:
            user, target = ls
        else:
            user, target = '', ls[0]
        target = target.split(':')
        host = ':'.join(target[:-1])
        path = target[-1]
        data['server_targets'] = [{
            'user': user,
            'host': host,
            'path': path,
            'port': server_target[1]
        }]
    else:
        data['server_targets'] = [{
            'user': '',
            'host': '',
            'path': '',
            'port': '22'
        }]
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.command()
def allFormat(filepath: list):
    for file in filepath:
        try:
            adjust(file)
        except:
            continue


if __name__ == '__main__':
    app()
