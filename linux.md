How to check **kernel version** a system is currently running?

    $uname -a 
    Linux blabla 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux

    $ uname -v      # kernel version
    #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025

    $ uname -r      # release
    6.6.87.2-microsoft-standard-WSL2

How can you check systems' current **IP Address**?

    $ifconfig       # deprecated
    $ ip addr show
    $ ip addr show <interface name>

How do you check **free disk space**?

    $df -ah     # disk free, show all in human-readable format

How do you **manage services** on a system? (run, start, stop, reload service)

    $systemctl status <service_name>
    $systemctl stop <service_name>
    $systemctl start <service_name>
    $systemctl reload <service_name>    # reload configs
    $systemctl restart <service_name>   # stop + start

How would you check the **total size of a directory**'s content on disk?

    $du -sh     # disk usage, summarize (1 line total space), in human-readable format.

    # folder tales 32kb space alltogether
    $ du file_handling/ -hs 32K  file_handling/

How would you check for **open ports** on a Linux machine?

    $sudo netstat -tulpn
    # shows network statistics on 
    -t -> TCP sockets
    -u -> UDP sockets
    -l -> only listening sockets
    -p -> show PID/program name owning the socket
    -n -> show numeric addresses/ports (no DNS or service name lookup)

    0.0.0.0:80 means all public addr

How to check **CPU usage** for a process?

    $ps aux     # shows all the process with nice details
    ps - process status
    a - all users processes
    u - user-oriented format(CPU%, MEM%)
    x - include processes without a controlling terminal

    $ps aux | grep nginx

    $ top   # descending order by CPU

How do you look up something you **don't know**?

    use man <command>


    

