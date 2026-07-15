# FastAPI 最小雛形

安裝套件：
```powershell
pip install -r requirements.txt
```
請在專案根目錄啟動：
```powershell
python -m uvicorn backend.main:app --reload
``
開啟 <http://127.0.0.1:8000>。

## 開發模式一鍵啟動
建立虛擬環境並安裝套件後，之後只需在專案根目錄執行：
```powershell
python run_dev.py
```
伺服器準備完成後，會自動開啟瀏覽器。
