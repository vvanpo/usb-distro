usb-distro
==========

A simple distribution meant for USB drives, based on the Nix package manager.

Goals:
	- Follow Lennart's description of stateless and/or reproducible systems: http://0pointer.de/blog/projects/stateless.html
	- More fine-grained rollbacks possible using the Nix package manager
	- Default to loading the system into RAM, or a subset, perhaps using zram as a method to increase viability on smaller systems
	- Allow transparent write-back to storage
	- Allow usb to be removed without affecting the system, write-back should get paused without notice until the same usb is plugged back in

