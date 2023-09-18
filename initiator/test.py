import subprocess
import paramiko

# Define the full path to VBoxManage based on your findings
vboxmanage_path = r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'

# Define the name of the virtual machine
vm_name = "CentOS_ODS"  # Replace with the name of your CentOS VM

# Command to start the virtual machine using VBoxManage
start_command = f'"{vboxmanage_path}" startvm {vm_name} --type headless'

# Define SSH parameters
vm_ip = "192.168.218.199"  # Replace with the actual IP address of your VM
ssh_username = "rajkumarbarnwal"
ssh_password = "Ayush@12345"

try:
    # Execute the command to start the VM
    subprocess.run(start_command, shell=True, check=True)
    print(f"Starting virtual machine '{vm_name}'...")

    # Add a delay to allow the VM to fully start (you can adjust the time as needed)
    import time
    time.sleep(120)  # Wait for 120 seconds (adjust as needed)

    # SSH into the VM and execute a command to check if it's running
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(vm_ip, username=ssh_username, password=ssh_password)

    # Example command to execute on the VM (you can change this as needed)
    command_to_execute = "ls /"

    stdin, stdout, stderr = ssh_client.exec_command(command_to_execute)

    # Check if the command was successful
    if stdout.channel.recv_exit_status() == 0:
        print("CentOS VM is running.")
        print("Command output:")
        print(stdout.read().decode())
    else:
        print("Failed to execute command on CentOS VM.")

    # Close the SSH connection
    ssh_client.close()

except subprocess.CalledProcessError:
    print(f"Failed to start virtual machine '{vm_name}'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

