"""一鍵啟動本機 FastAPI 開發伺服器，並在就緒後開啟瀏覽器。"""

import socket
import threading
import time
import urllib.error
import urllib.request
import webbrowser

import uvicorn


HOST = "127.0.0.1"
PORT = 8000
URL = f"http://{HOST}:{PORT}"

def ensure_port_is_available() -> None:
    with socket.socket() as test_socket:
        try:
            test_socket.bind((HOST, PORT))
        except OSError as error:
            raise SystemExit(
                f"Port {PORT} is already in use. Stop the existing server and try again."
            ) from error

def open_browser_when_ready() -> None:
    while True:
        try:
            with urllib.request.urlopen(URL, timeout=1):
                break
        except (urllib.error.URLError, TimeoutError):
            time.sleep(0.2)

    webbrowser.open(URL)


if __name__ == "__main__":
    ensure_port_is_available()
    print(f"Starting server at {URL}")
    threading.Thread(target=open_browser_when_ready, daemon=True).start()
    uvicorn.run(
        "backend.main:app",
        host=HOST,
        port=PORT,
        reload=True,
    )
