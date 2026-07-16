# FastAPI + SQLite Demo

這個專案示範三種類型的 API：

- 純 API：不存取資料庫，例如 Hello API、API 2
- AI API：呼叫 Gemini 產生回答
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
│   ├── ai/
│   │   └── chat.py
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

`backend/api/http/` 放一般 API；`backend/api/ai/` 放 AI API；`backend/api/db/` 放會存取 DB 的 API。

修改目錄的 `.env.example` 為 `.env`，填入 Gemini API Key：(可以從Google AI Studio申請免費的來測試)

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

Item 欄位：

- `name`：String，必填
- `quantity`：Integer，選填，預設 `0`
- `price`：Float，選填，預設 `0`
- `is_active`：Boolean，選填，預設 `true`
