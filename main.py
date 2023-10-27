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
        "source_codes": {
            'bind': '/app/vol',
            'mode': 'rw'
        }
    }
}


code = """
def add_numbers(a, b):
    return a + b
"""
container = None
try:
    code1 = code.strip()
    wrapped_code = textwrap.dedent(code1).strip()
    print(wrapped_code)
    with open('userFile.py', 'w') as file:
        file.write(wrapped_code)


    os.system('docker cp userFile.py dummyHelp:/app/vol/userFile.py')
    # os.system('docker cp authorFile.py dummyHelp:/app/vol/authorFile.py')
    # Copy in the volume
    container = client.containers.run(**docker_config)
    # container = client.containers.get('C1')
    print('Container: ', container)

    print(container.logs())
    for line in container.logs(stream=True):
        print(line.strip())
except Exception as e:
    print('NONO!', e)
finally:
    os.remove('userFile.py')
    container.stop()
    container.remove()