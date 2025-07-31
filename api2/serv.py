import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 5002))
s.listen(1)
print("listening on 5002")

while True:
	conn, addr = s.accept()
	request = conn.recv(1024)

	body = b"pong"
	response = (
		b"HTTP/1.1 200 OK\r\n"
		b"Content-Type: text/plain\r\n"
		b"Connect-Length: " + str(len(body)).encode() + b"\r\n"
		b"Connection: close\r\n"
		b"\r\n" +
		body
	)

	conn.sendall(response)
	conn.close()
