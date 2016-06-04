from socketIO_client import SocketIO

socket = SocketIO('localhost', 3000)

chat_message = input('\n')
while chat_message != 'quit':
    msg = {"contents" : chat_message}
    socket.emit('chat', msg)
    chat_message = input('\n')
