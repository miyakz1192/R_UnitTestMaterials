#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, CGIHTTPRequestHandler

class MyHandler(CGIHTTPRequestHandler):
    def do_PUT(self):
        try:
            # PUTリクエストの対象のパスを取得
            path = "./" + self.path
        
            # PUTデータのサイズを取得
            content_length = int(self.headers['Content-Length'])

            print("受信データを読み込みます")
        
            # PUTデータを取得
            data = self.rfile.read(content_length)
            print("受信データ = ", data)
        
            # ここでパスとデータを処理できます
            # 例: パスに基づいてファイルにデータを書き込む
            with open(path, 'wb') as f:
                f.write(data)
        
            # 応答を返す
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'PUT req ok')
        except BrokenPipeError:
            print("クライアントが接続を閉じました")


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('サーバーがポート8000で実行中...')
    httpd.serve_forever()


