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

            print("受信データを読み込みます. content_length=", content_length)
        
        
            # ここでパスとデータを処理できます
            # 例: パスに基づいてファイルにデータを書き込む
            with open(path, 'wb') as f:
                # データを少しずつ読み取り、ファイルに書き込む
                while content_length > 0:
                    chunk = self.rfile.read(min(1024, content_length))  # 最大1024バイトずつ読み取る
                    if not chunk:
                        print("not chunk")
                        break
                    print("受信データtype = ", type(chunk))
                    print("受信データlen = ", len(chunk))
                    f.write(chunk)
                    content_length -= len(chunk)

        
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


