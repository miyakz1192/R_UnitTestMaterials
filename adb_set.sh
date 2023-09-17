#!/bin/bash

if [ $# -ne 3 ]; then
	echo "USAGE: device_wait_port device_pair_port device_key"
	exit 1
fi

device_wait_port=$1
device_pair_port=$2
device_key=$3
device_ip="192.168.110.178"

ADB_PATH="/home/miyakz/Unity/Hub/Editor/2021.3.21f1/Editor/Data/PlaybackEngines/AndroidPlayer/SDK/platform-tools/adb"

# デバイスをペアリング
$ADB_PATH pair ${device_ip}:${device_pair_port} ${device_key}

# デバイスに接続
$ADB_PATH connect ${device_ip}:${device_wait_port}

# 接続されたデバイスを表示
$ADB_PATH devices
