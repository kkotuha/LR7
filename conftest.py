import paramiko
import subprocess
import pytest

server_ip = '10.0.2.15'
username = 'm'
password = 'm'


@pytest.fixture(scope='function')
def server():
    command = 'iperf -s -u & echo $!'

    ssh_client = paramiko.client.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_ip, username=username, password=password)

    stdin, stdout, stderr = ssh_client.exec_command(command)
    pid = int(stdout.readline())

    yield

    ssh_client.exec_command(f'kill -9 {pid}')
    ssh_client.close()


@pytest.fixture(scope='function')
def client():
    start_command = f'iperf -c {server_ip} -u'

    with subprocess.Popen(start_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p:
        result, error = p.communicate()

    decoded_result = result.decode("utf-8")
    decoded_error = error.decode("utf-8")

    if error:
        print(
            f'Error while executing {start_command} command:\n{decoded_message}')

    return decoded_result, decoded_error
