import socketserver
import pidfile
import time

from router import Router

if __name__ == '__main__':
    try:
        with pidfile.PIDFile():
            print('Process started')

            PORT = 8080
            print('Server listen at ' + str(PORT))
            my_server = socketserver.TCPServer(("", PORT), Router)
            try:
                my_server.serve_forever()
            except KeyboardInterrupt:
                pass
            finally:
                my_server.server_close()
                print("Server stopped.")

    except pidfile.AlreadyRunningError:
        print('Already running.')

    print('Exiting')
