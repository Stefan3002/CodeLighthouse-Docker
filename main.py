import os
import textwrap
import time
import docker

client = docker.from_env()

docker_config = {
    'detach': True,
    # 'command': 'sleep infinity',
    'image': 'img',
    # 'remove': False,
    'tty': True,
    # 'name': 'C1',
    'volumes': {
        '/volum': {
            'bind': '/app/vol',
            'mode': 'rw'
        }
    },
}

code = """
def user_function(a, b):
    return a + b + x
"""
container = None
try:
    code1 = code.strip()
    wrapped_code = textwrap.dedent(code1).strip()
    print(wrapped_code)
    with open('userFile.py', 'w') as file:
        file.write(wrapped_code)

    # os.system('docker cp authorFile.py dummyHelp:/app/vol/authorFile.py')
    # Copy in the volume
    container = client.containers.create(**docker_config)
    # container = client.containers.get('C1')
    print('Container: ', container)
    os.system(f'docker cp userFile.py {container.name}:/app/vol/userFile.py')


    container.start()
    logs = container.logs(stdout=True, stderr=True, stream=True)
    log_bytes = b''
    for line in logs:
        log_bytes += line

    logs_str = log_bytes.decode('utf-8')

    print(logs_str)

except Exception as e:
    print('NONO!', e)
finally:
    os.remove('userFile.py')
    container.stop()
    container.remove()
