

import paramiko

import configparser

 

def read_config(filename):

    config = configparser.ConfigParser()

    config.read(filename)

    ssh_config = config['SSH']

    return ssh_config

 

def establish_ssh_connection(config):

    hostname = config.get('hostname')

    port = int(config.get('port'))

    username = config.get('username')

    password = config.get('password')

 

    try:

        ssh_client = paramiko.SSHClient()

        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_client.connect(hostname, port=port, username=username, password=password)

        return ssh_client

    except Exception as e:

        print(f"Error establishing SSH connection: {str(e)}")

        return None

 

def main():

    config_filename = "config.properties"

    config = read_config(config_filename)

    ssh_connection = establish_ssh_connection(config)

 

    if ssh_connection:

        print("SSH connection established successfully.")

        return ssh_connection

    else:

        print("Failed to establish SSH connection.")

        return None

 

if __name__ == "__main__":

    ssh_connection = main()
try:
    # Run a remote command
    stdin, stdout, stderr = ssh_connection.exec_command("ls")

    # Print the command output
    print("Command Output:")
    print(stdout.read().decode())

    # Close the SSH connection when done
    ssh_connection.close()
except Exception as e:
    print(f"Error during SSH operation: {str(e)}")    

