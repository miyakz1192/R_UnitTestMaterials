echo "booting UnitTest Web Server..."
echo "initializin 7038eb77-2913-4615-9522-caeaa3271bcc/souchan/log"
echo sample_log | tr -d "\n" > 7038eb77-2913-4615-9522-caeaa3271bcc/souchan/log
#python -m SimpleHTTPServer

#python3 -m http.server --cgi 8000

./python_http_server.py

