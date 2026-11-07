# Privacy lens

Check, within the approved scope:

1. Identifiers the machine reveals: device and host names, hardware addresses, mDNS/Bonjour and other service advertising, Bluetooth names, and the known Wi-Fi networks it searches for.
2. Network leaks: DNS resolvers and encryption, VPN, IPv6, and WebRTC leaks.
3. Telemetry, analytics, ad identifiers, crash reporting, and which apps can use location, camera, microphone, and screen capture.
4. Sync, sharing, and discoverability (nearby file sharing, device handoff, clipboard sync), browser tracking settings, and personal metadata, such as location or author names, in files the user plans to share.

Risky privacy changes include MAC address randomization (breaks captive portals, MAC filtering, DHCP reservations, network access control), DNS changes, disabling mDNS, and VPN kill switches.

Root cause: what exposes it (app, setting, or service), since when, and why.
