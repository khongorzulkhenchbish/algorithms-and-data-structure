File system:

|location|name|can write|note|
|---------|---------|---------|---------|
|/|root|||
|/bin|binary|do not modify|contains essential cmd tools for the system during boot, 'ls', 'cp', 'mv', 'cat'... are located here. "/root" is under "/" and not same as "/"|
|/sbin|system binary|do not modify|contains specialized system utilities, used by root or system adm|
|/lib|library|do not modify|contains support files for bin, sbin. These file provides common functionality like reading files, handling I/O. lib32, lib64 - stores 32,64 bits library. Also it has kernel modules that is loaded into linux kernel on demand|
|/usr|unix system resources|do not modify|to hold non-essential contains user space applications, installed programs. it mirrors /usr/bin, /usr/lib, /user/sbin|
|/boot|boot|interacting with the devices can directly affect the hardware!|all the files needed for initial boot, grub.cfg tells the system to how to load the OS. contains initrd, inittramfs, GRUB|
|/dev|device|do not modify|contains device files act as interfaces to hardware. /dev/sda - represent the first hard drive, /dev/null - virtual devices. 2 main types block devices - like hard drives, handles the data in chunks, Character devices - like keyboards, handles the data as stream of characters. These files are handled dynamically as hardware changes.|
|/etc|et cetera, editable text config|allowed by sys admin|central location for system wide config files, from network settings to user accounts, to startup scripts to server configs. /etc/passwd - basic user info, /etc/fstab - how drives are mounted at boot|
|/home|home|allowed by the user|keep user data separate from system files, user spec configs are hidden by default as ".", .bashrc for example. Root user has /root for their own home|
|/media|media|can be edited|designed for usb, dvd removable devices, under /media/${volume} the user can access handled automatically by the system|
|/mnt|mounting file systems|allowed by sys admin|reserved for manual temporary mounts, typically used by root user or advanced scripts|
|/proc|processes|n/a|virtual filesystem, no real file, live interface to the linux kernel in running processes, contains process ids, system info files, /proc/cpuinfo, /proc/meminfo|
|/sys|pseudo file system|n/a|dynamic interface between linux kernel and hardware|
|/run|runtime|n/a|temporary runtime data used by the system applications right after the boot, these files disappears after reboot, /run/user, /run/lock|
|/srv|service|n/a|data for services (shared with others) provided for systems are stored|
|/var|variable|n/a|storing files that change frequently, /var/log - rotated,caches, /var/lib - important metadata, sensible infos are stored|
|/tmp|temporary|n/a, writable by user though|used for lightweight temp data only|
|/opt|optional|n/a|optional or 3rd party software is installed, /opt/google/chrome, safe space without interfering system files|


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

How do you **list open files**?

    lsof +L1    # list files that have been deleted but are still open
    

#### P95 latency
is the 95th percentile of request response times, meaning 95% of all requests are completed in less than this amount of time, while 5% take longer.

Example: If the P95 latency is 90 milliseconds, it means 95 out of 100 requests were faster than 90 ms, and 5 requests took longer than 90 ms.


#### Kafka lag
is the difference between the latest messages produced and the last messages consumed by a consumer group, indicating how far behind the consumer is in processing data. **High lag** means a **delay in message processing**, which can lead to performance issues, while **low lag** indicates **efficient processing**. Causes include high incoming traffic, slow processing, and data skew, and it can be managed by scaling consumers, tuning configurations, and optimizing processing logic.

