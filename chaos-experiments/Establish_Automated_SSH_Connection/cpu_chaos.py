import paramiko
from establish_con import establish_ssh_connection

def get_cpu_utilization(ssh_client):
    if ssh_client:
        try:
            # Run the 'top' command to get CPU utilization information
            stdin, stdout, stderr = ssh_client.exec_command("top -n 1 -b | grep 'Cpu(s)'")
            cpu_info = stdout.read().decode('utf-8')
            print("CPU Utilization:")
            print(cpu_info)
        except Exception as e:
            print(f"Failed to get CPU utilization: {str(e)}")

if __name__ == "__main__":
    config_filename = "D:\establish_con_ODS\PythonGenAIChaos_Solution\chaos-experiments\Establish_Automated_SSH_Connection\config.properties"
    ssh_connection = establish_ssh_connection(config_filename)

    # Get and display CPU utilization
    get_cpu_utilization(ssh_connection)

    # Remember to close the SSH connection when done
    if ssh_connection:
        ssh_connection.close()
