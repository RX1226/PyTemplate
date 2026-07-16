"""定義 Item API 的輸入欄位、型態、預設值與驗證規則。"""

from pydantic import BaseModel, Field


class ItemInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    quantity: int = Field(default=0, ge=0)
    price: float = Field(default=0, ge=0)
    is_active: bool = True
