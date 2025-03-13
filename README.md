# PyCharm 指令與基本操作

## 1. 執行 Python 程式

### 1.1 直接執行程式

- 在 PyCharm 中開啟 `.py` 檔案，點擊右上角的 **▶ Run** 按鈕。
- 或者使用快捷鍵 `Shift + F10`。

### 1.2 使用 Configurations 設定執行細節

1. 在 `Run > Edit Configurations...` 中開啟設定頁面。
2. 點擊左上角 `+` 按鈕，選擇 `Python`。
3. 設定名稱、Interpreter、腳本路徑、參數，完成後按 `OK`。

### 1.3 什麼是 Interpreter？

Interpreter 指的是 Python 直譯器，它決定了：
1. 執行 Python 程式時所使用的 Python 版本（例如 Python 3.8、3.9、3.10）。
2. 使用哪個虛擬環境（Virtual Environment，如 venv、conda）。
3. 哪些已安裝的套件可以使用（例如 numpy、flask、django）。

## 2. Script 與 Module 的差別

| 主要差異           | Script（腳本）   | Module（模組） |
|----------------|--------------| -------------- |
| 主要用途           | 執行特定的任務      | 供其他程式導入使用   |
| 運行方式           | 直接執行         | 透過import導入     |
| \_\_name__ 變數值 | "\_\_main__" | 模組名稱     |

### 2.1 Script 範例

```python
# script_example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 2), subtract(1, 2))

```

執行方式：

```sh
python script_example.py
```

### 2.2 Module 範例

```python
# module_example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

在其他程式中使用此模組：

```python
import module_example

print(module_example.add(1, 2), module_example.subtract(1, 2))
```

## 3. 執行參數（Parameters）與環境變數（Environment Variables）

| 主要差異 | 執行參數（Parameters） | 環境變數（Environment Variables） |
| ---- |------------------|-----------------------------|
| 影響範圍 | 只影響當次執行          | 影響整個系統或當前環境                 |
| 適用場景 | 使用者指定的參數/變動的輸入值  | 機密資料、全域配置，如 API 金鑰、資料庫連線字串  |
| 存活時間 | 只在程式執行期間有效       | 只要系統不重啟或未被修改，就會一直存在         |

### 3.1 設定執行參數

```python
import sys
print(sys.argv)
```

執行方式：

```sh
python test.py hello
```

### 3.2 設定環境變數

在 `.env` 檔案中設定：

```sh
API_KEY="your_api_key"
```

在程式中使用：

```python
import os
from dotenv import load_dotenv

load_dotenv()

value = os.getenv("API_KEY")
print(f"環境變數 API_KEY: {value}")
```

## 4. PyCharm 與 Terminal 執行 Python 指令的對應

- PyCharm: 點擊 `▶ Run` 或 `Shift + F10`
- Terminal: 手動輸入 `python 檔案名稱 --參數 值`

## 5. 一般執行（Run）與偵錯模式（Debug）

| 模式          | 速度 | 適用場景     | 主要特點                  |
| ----------- | -- | -------- | --------------------- |
| 一般執行（Run）   | 快  | 已開發完成的程式 | 只顯示錯誤訊息，無法進一步分析       |
| 偵錯模式（Debug） | 慢  | 用於尋找程式錯誤 | 可逐行執行程式、檢查變數值、設定條件式斷點 |

## 6. 偵錯模式（Debug）介面功能

- **Resume Program**：繼續執行程式直到遇到下一個斷點。
- **Pause Program**：強制暫停程式。
- **Step Over**：執行當前行，但不進入函式內部。
- **Step Into**：進入函式內部。
- **Step Out**：執行完當前函式後回到上一層。
- **View Breakpoints**：查看所有斷點。
- **Mute Breakpoints**：暫時停用所有斷點。
- **Rerun**：重新執行。
- **Stop**：停止執行。

## 7. PyCharm 快速操作

### 7.1 快速找到方法或參數的源頭

- **查看方法定義**：`Ctrl + 左鍵` 或 `Ctrl + B`
- **查看方法實作內容**：`Ctrl + Shift + I`
- **查看參數在哪裡被使用**：`Alt + F7`

### 7.2 快速格式化程式碼

- **快捷鍵**：`Ctrl + Alt + L`

---
