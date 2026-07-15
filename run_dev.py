import threading
import time
import urllib.error
import urllib.request
import webbrowser

import uvicorn


URL = "http://127.0.0.1:8000"


def open_browser_when_ready() -> None:
    while True:
        try:
            with urllib.request.urlopen(URL, timeout=1):
                break
        except (urllib.error.URLError, TimeoutError):
            time.sleep(0.2)

    webbrowser.open(URL)


if __name__ == "__main__":
    print(f"Starting server at {URL}")
    threading.Thread(target=open_browser_when_ready, daemon=True).start()
    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
