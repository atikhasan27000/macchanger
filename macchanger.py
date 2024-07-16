import subprocess

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def get_user_input(prompt):
    """Get user input."""
    return input(prompt)

def main():

    logo = """
\033[32m __  __                _                         
|  \/  |              | |                                
| \  / | __ _  ___ ___| |__   __ _ _ __   __ _  ___ _ __ 
| |\/| |/ _` |/ __/ __| '_ \ / _` | '_ \ / _` |/ _ \ '__|
| |  | | (_| | (_| (__| | | | (_| | | | | (_| |  __/ |   
|_|  |_|\__,_|\___\___|_| |_|\__,_|_| |_|\__, |\___|_|   
Author: ATik HaSan                        __/ | 2.7.0v   
Python: 3.12.4                           |___/           
\033[0m"""
    print(logo)
    # Show the current IP address
    current_ip = run_command("ifconfig eth0 | grep 'inet ' | awk '{print $2}'")

    # Ask the user for the IP address
    ip_address = get_user_input(f"Enter the IP address you want to use (Your current IP address is - {current_ip}): ")

    # Ask the user for the MAC address, or generate one automatically
    custom_mac = get_user_input("Enter the MAC address you want to set (leave blank for random): ")

    # Run commands to change IP and MAC addresses
    print("\nChanging IP and MAC addresses...\n")

    # Bring the interface down
    run_command("sudo ifconfig eth0 down")

    # Change the IP address
    run_command(f"sudo ifconfig eth0 {ip_address}")

    if custom_mac:
        # Set the custom MAC address
        run_command(f"sudo ifconfig eth0 hw ether {custom_mac}")
    else:
        # Generate a random MAC address
        run_command("sudo macchanger -A eth0")

    # Bring the interface up
    run_command("sudo ifconfig eth0 up")

    # Show the final IP and MAC addresses
    final_ip = run_command("ifconfig eth0 | grep 'inet ' | awk '{print $2}'")
    final_mac = run_command("ifconfig eth0 | grep 'ether ' | awk '{print $2}'")

    print("\nChanged IP and MAC addresses:\n")
    print(f"IP Address: {final_ip}")
    print(f"MAC Address: {final_mac}")

if __name__ == "__main__":
    main()