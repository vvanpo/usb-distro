#!/usr/bin/env python3

import argparse, os, tempfile, urlib.request

def arguments():
	parser = argparse.ArgumentParser(description='A simple command-line installer for usb-distro.')
	#parser.add_argument('device')
	return parser.parse_args()

def main():
	args = arguments()
	with tempfile.TemporaryDirectory() as path:
		os.chdir(path)
		os.mkdir('usr')
		os.mkdir('proc')
		os.mkdir('sys')
		os.mkdir('dev')
		os.mkdir('root')

if __name__ == '__main__':
	main()
