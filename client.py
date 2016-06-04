from socketIO_client import SocketIO

socket = SocketIO('localhost', 3000)

username = input('What is your username?')

chat_message = input('\n')
while chat_message != 'quit':
    msg = {"contents" : chat_message, "username" : username}
    socket.emit('chat', msg)
    chat_message = input()
