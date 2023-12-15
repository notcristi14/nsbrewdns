import socket
import time

print('Getting Homebrew DNS');

DNS = socket.gethostbyname('homebrew.heartium0.repl.co')


print('Your DNS Adress Is: ' + DNS)

print('Automatically closing in 60 seconds')

time.sleep(60)