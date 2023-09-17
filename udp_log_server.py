#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket

# UDPソケットを作成し、指定のポートで待ち受けます
server_ip = "0.0.0.0"# すべてのネットワークインターフェースで待ち受ける
server_port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((server_ip, server_port)) 
    print(f"UDPサーバーがポート{server_port}で待ち受け中...")
    while True:
        data, addr = server_socket.recvfrom(1024)  # 1024バイトまでのデータを受信
        print(f"受信したメッセージ: {data.decode()} 送信元アドレス: {addr}")
