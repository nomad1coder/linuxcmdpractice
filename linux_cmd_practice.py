import random

commands= {
    "ssh": "Secure Shell (SSH) protocol is used to securely access a remote server.",
    "ls": "Lists files and directories in a directory.",
    "pwd": "Displays the current working directory.",
    "cd": "Changes directory.",
    "touch": "Updates the modification time of a file or creates a new file.",
    "echo": "Prints text to standard output.",
    "nano": "Opens the nano text editor.",
    "vim": "Opens the vim text editor.",
    "cat": "Prints the contents of a file to standard output.",
    "shred": "Securely deletes a file.",
    "mkdir": "Creates a new directory.",
    "cp": "Copies files.",
    "mv": "Moves files.",
    "rm": "Removes files or directories.",
    "rmdir": "Removes a directory.",
    "ln": "Creates links.",
    "clear": "Clears the terminal screen.",
    "useradd": "Creates a new user account.",
    "sudo": "Runs a command as a superuser.",
    "adduser": "Creates a new user account.",
    "su": "Changes user session.",
    "exit": "Exits the current session.",
    "sudo passwd": "Changes the superuser password.",
    "sudo passwd [username]": "Changes the password of the specified user.",
    "sudo apt": "Runs package manager commands.",
    "2sudo apt update & install": "Updates the package database and installs the specified packages.",
    "finger": "Displays user information.",
    "man": "Displays the manual page for a command.",
    "whatis": "Provides a brief description of a command.",
    "which": "Shows the full path of a command.",
    "whereis": "Shows the locations of a command's binaries and manual pages.",
    "wget": "Downloads files from the internet.",
    "curl": "Sends requests to a URL.",
    "zip": "Compresses files.",
    "unzip": "Unzips files.",
    "less": "Displays the contents of a file one page at a time.",
    "head": "Displays the beginning of a file.",
    "tail": "Displays the end of a file.",
    "cmp": "Compares two files.",
    "diff": "Shows differences between two files.",
    "sort": "Sorts lines.",
    "find": "Finds files.",
    "chmod": "Changes file permissions.",
    "chown": "Changes file ownership.",
    "ifconfig": "Shows network interface configuration information.",
    "ip address": "Shows IP addresses of network interfaces.",
    "ip address | grep eth0": "Shows IP addresses for eth0 interface.",
    "ip address | grep eth0 | grep inet | awk": "Shows IPv4 addresses for eth0 interface.",
    "resolvectl status": "Shows DNS configuration information.",
    "ping": "Sends ICMP packets to a network device.",
    "netstat": "Shows network connections, routing tables, interface statistics, etc.",
    "-tulpn": "Shows applications listening on specified ports.",
    "ss": "Shows network connections.",
    "ipstables": "Filters and routes network traffic.",
    "ufw": "Manages Uncomplicated Firewall.",
    "uname": "Shows system information.",
    "neofetch": "Shows system information and logo.",
    "cal": "Displays the calendar.",
    "free": "Shows memory usage.",
    "df and df-h": "Shows disk usage.",
    "ps": "Shows running processes.",
    "top": "Watches system resources in real-time.",
    "kill": "Terminates processes.",
    "systemctl": "Controls the system manager.",
    "history": "Displays command history.",
    "sudo reboot": "Reboots the system.",
    "shutdown": "Shuts down the system."
}


while True:
    key = random.choice(list(commands.keys()))
    print(key)
    input()
    print(commands[key])
    again = input('n to close\n')

    if again == 'n':
        break