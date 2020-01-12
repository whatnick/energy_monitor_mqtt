# Demo code to publish 3-phase energy monitor readings to AWS IoT
This is a demo implementation for Onion Omega 2 based energy monitor
host for publishing 3-phase energy monitor readings to AWS IoT and subscribing
to messages to switch loads on and off.

## Implementation Roadmap
- Read ATM90E26/36 over the SPI bus (Pending consolidation and PyPi setup)
- Push local display to OLED over the I2C bus (Pending cosolidation)
- Push remote sink via MQTT over TLS (WIP)
- Subscribe to remote commands via MQTT subscribe and toggle relays to shed/enable load as appropriate. (WIP)