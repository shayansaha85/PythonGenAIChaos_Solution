import subprocess


# Define the full path to VBoxManage based on your findings
vboxmanage_path = r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'

# Define the name of the virtual machine
vm_name = "CentOS_ODS"  # Replace with the name of your CentOS VM

# Command to start the virtual machine using VBoxManage
start_command = f'"{vboxmanage_path}" startvm {vm_name} --type headless'

try:


    # Execute the command to start the VM
    subprocess.run(start_command, shell=True, check=True)
    print(f"Starting virtual machine '{vm_name}'...")

except subprocess.CalledProcessError:


    print(f"Failed to start virtual machine '{vm_name}'.")

