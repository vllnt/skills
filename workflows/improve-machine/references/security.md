# Security lens

Check, within the approved scope:

1. The OS's default security configuration: updates, firewall, disk encryption, built-in protections, sign-in settings, and remote access or sharing.
2. Hidden, disguised, or dormant processes, including anything set to start or wake later.
3. This machine's network configuration and exposure, including listening ports and their owners.
4. Local network, only after the user approves and confirms they own or administer it: unknown or impersonating devices and signs of attack. Use passive data first; active scans need separate approval, stay on the local subnet, use low-impact probes, and never capture others' traffic. Never exploit, brute-force, log in to, or change other devices; recommend actions the user can take.
5. Accounts and credentials: administrators, remote-access keys, and exposed secrets.

Root cause: for a process or port, the PID, parent chain, app, binary, signer, start time, and launch reason; for a setting or account, what set it and when; for a device, its network identity and connections to this machine.
