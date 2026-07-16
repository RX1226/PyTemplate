# FastAPI + SQLite Demo

這個專案示範兩種類型的 API：

- 純 API：不存取資料庫，例如 Hello API、API 2
- DB API：操作 SQLite Database、Table 與 Item

## 啟動

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run_dev.py
```

啟動後會自動開啟 <http://127.0.0.1:8000>，API 文件位於 <http://127.0.0.1:8000/docs>。

## 結構

```text
backend/
├── api/
│   ├── routes.py
│   ├── http/
│   │   ├── hello.py
│   │   └── api2.py
│   └── db/
│       ├── database.py
│       ├── table.py
│       └── item.py
└── db/
    ├── database.py
    ├── table.py
    ├── dao/item_dao.py
    └── models/item.py
```

`backend/api/http/` 放不存取 DB 的一般 API；`backend/api/db/` 放會存取 DB 的 API；`backend/db/` 負責實際資料庫操作。

Item 欄位：

- `name`：String，必填
- `quantity`：Integer，選填，預設 `0`
- `price`：Float，選填，預設 `0`
- `is_active`：Boolean，選填，預設 `true`
