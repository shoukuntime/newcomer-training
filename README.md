# PyCharm 指令與基本操作

## 1. 執行 Python 程式

### 1.1 直接執行程式

- 在 PyCharm 中開啟 `.py` 檔案，點擊右上角的 **▶ Run** 按鈕。
- 或者使用快捷鍵 `Shift + F10`。

### 1.2 使用 Configurations 設定執行細節

1. 在 `Run > Edit Configurations...` 中開啟設定頁面。
2. 點擊左上角 `+` 按鈕，選擇 `Python`。
3. 設定名稱、Interpreter、腳本、執行參數與環境變數，完成後按 `OK`。

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

if len(sys.argv) > 1:
    print(f"輸入的參數是: {sys.argv[1]}")
else:
    print("沒有輸入參數！")
```

執行方式：

```sh
python 檔案名.py 參數
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

Terminal: 手動輸入 `python 檔案名稱 --參數 值`

## 5. 一般執行（Run）與偵錯模式（Debug）

| 模式          | 速度 | 適用場景     | 主要特點                  |
| ----------- | -- | -------- | --------------------- |
| 一般執行（Run）   | 快  | 已開發完成的程式 | 只顯示錯誤訊息，無法進一步分析       |
| 偵錯模式（Debug） | 慢  | 用於尋找程式錯誤 | 可逐行執行程式、檢查變數值、設定條件式斷點 |

## 6. 偵錯模式（Debug）介面功能
- **Rerun**：重新執行。
- **Stop**：停止執行。
- **Resume Program**：繼續執行直到下一個斷點或結束。
- **Pause Program**：強制暫停。
- **Step Over**：執行當前行，但不進入函式內部。
- **Step Into**：進入函式內部。
- **Step Into My Code**：只進入自己寫的程式碼
- **Step Out**：執行完當前函式後回到上一層。
- **View Breakpoints**：顯示所有斷點。
- **Mute Breakpoints**：停用所有斷點。


## 7. PyCharm 快速操作

### 7.1 快速找到方法或參數的源頭

- **查看方法定義**：`Ctrl + 左鍵` 或 `Ctrl + B`
- **查看方法實作內容**：`Ctrl + Shift + I`
- **查看參數在哪裡被使用**：`Alt + F7`

### 7.2 快速格式化程式碼

- **快捷鍵**：`Ctrl + Alt + L`

---

# Python 程式基礎訓練

## 1. 虛擬環境操作

### 1.1 確認目前所在的 Python 虛擬環境
**方法 1：使用指令查詢**
```sh
where python
```
**方法 2：使用 sys 模組查看 Python 解釋器路徑**
```python
import sys
print(sys.executable)
```

### 1.2 requirements.txt 的用途
`requirements.txt` 用於記錄 Python 專案所需的套件及版本，適用於環境管理、專案部署及共享。

**建立 requirements.txt**
```sh
pip freeze > requirements.txt
```

**使用 requirements.txt 安裝套件**
```sh
pip install -r requirements.txt
```

### 1.3 使用 venv 和 Poetry 建立虛擬環境
**venv 建立與啟動**
```sh
python -m venv myenv
myenv\Scripts\activate
```

**Poetry 建立與啟動**
```sh
poetry new myproject
cd myproject
poetry install
poetry shell
```

---

## 2. Python 基本概念與語法

### 2.1 資料結構

| 資料結構 | 特性 | 適用情境 |
|----------|------|----------|
| List（串列） | 可變動、有序 | 儲存多筆資料、需頻繁修改 |
| Tuple（元組） | 不可變動、有序 | 保持固定數據，如設定值 |
| Set（集合） | 唯一元素、無序 | 去除重複值、集合運算 |
| Dictionary（字典） | 鍵值對存取數據 | 快速查找、JSON 轉換 |

### 2.2 表達式
**List Comprehension（串列解析式）**

List Comprehension 是一種簡潔的方法來建立 list，可用於：
- 產生新列表
- 過濾元素
- 進行轉換
```python
# 基本語法
new_list = [運算式 for 變數 in 可迭代對象 if 條件]

# 範例
squares = [x**2 for x in range(10) if x % 2 == 0]
```

**Dictionary Comprehension（字典解析式）**

Dictionary Comprehension 是一種快速建立 dict 的方法，可用於：

- 建立新字典
- 過濾鍵值對
- 轉換數據格式
```python
# 基本語法
new_dict = {鍵: 值 for 變數 in 可迭代對象 if 條件}

# 範例
squared_dict = {x: x**2 for x in range(5)}
```

### 2.3 函式 (Function)
**`*args` 與 `**kwargs`**

**在 Python 中，`*args` 和 `**kwargs` 用於函式的參數處理，允許函式接受不確定數量的參數。**

`*args`允許函式接受**可變數量**的**位置參數**，這些參數將被存儲為**tuple**。

適用於當參數數量不固定時，例如數學計算或動態數據處理。

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # 輸出 10
print(add_numbers(5, 10))       # 輸出 15
```

`**kwargs`允許函式接受**可變數量**的**關鍵字參數**（key=value），這些參數將被存儲為**字典**(dict）。

適用於當函式需要處理不同的**命名參數**，例如設定值或 API 請求參數。

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Shou", age=23, city="Taipei")
# 輸出：
# name: Shou
# age: 23
# city: Taipei
```

**`return` 與 `yield`**

**return**
- **立即**返回結果並終止函式執行。
- 適用於**一次性計算**,例如簡單數學函式。
```python
def square(n):
    return n * n

print(square(5))  # 輸出 25
```
**yield**
- 會讓函式成為**生成器**(generator)，它不會一次性返回所有結果，而是**暫停執行**並**記住當前狀態**，在下次調用時繼續執行。
- 適用於需要**逐步產生數據**的場景，例如讀取大文件、無限序列或高效能迭代計算。
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # 暫停函式，返回當前值
        count += 1

gen = count_up_to(3)
print(next(gen))  # 輸出 1
print(next(gen))  # 輸出 2
print(next(gen))  # 輸出 3
# print(next(gen))  # 會拋出 StopIteration
```

### 2.4 型別註記（Type Hint）
- 使開發者在函式中標註**參數**和**回傳值**的型別，提高程式碼的可讀性與可維護性
- 透過 :(冒號)來標註函式參數的型別，並用 ->(箭頭) 來標註回傳值的型別
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))  # 輸出 8
```
**常見型別標註**:
- int（整數）
- float（浮點數）
- str（字串）
- bool（布林值）
- list（列表）
- tuple（元組）
- dict（字典）
- set（集合）

優勢: Type Hint 不會影響 Python 程式執行，但可以幫助開發者撰寫更清晰、易維護的程式碼
### 2.5 套件與模組（Package & Module）
| 項目 |  Module(模組)  | 	Package（套件）        |
|----|---------------------|---------------------|
| 結構 | 單一的 Python 檔案（.py)  | 包含多個模組的資料夾          |
| 用途 | 儲存可重複使用的函式、類別、變數等 | 組織與管理多個模組           |
| 使用方式 | `import module_name` | `import package_name.module_name` |

**`if __name__ == '__main__'` 的作用**

**目的:** 
- 確保程式碼只在當前檔案執行時才會執行，不會在被其他模組導入時運行。

**優點:**
- 防止模組被導入時執行內部測試程式
- 可以在模組內進行測試或調試
- 提高程式的可重用性與模組化設計

---

## 3. Logging（日誌記錄）

| 層級 | 用途                               |
|------|----------------------------------|
| DEBUG | 記錄詳細的調試資訊，通常用於開發與除錯階段。           |
| INFO | 記錄一般資訊，例如程式流程、狀態變化等。             |
| WARNING | 表示可能會發生問題，但程式仍能執行，例如「快要達到記憶體限制」。 |
| ERROR | 代表有錯誤發生，某些功能可能無法正常運作，但程式仍可繼續運行。         |
| CRITICAL | 表示重大錯誤，導致程式可能無法繼續執行。                    |

**輸出日誌到 Console**
```python
import logging

# 設定日誌輸出到檔案
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 測試不同層級的日誌
logging.debug('這是 Debug 訊息')
logging.info('這是一般的資訊')
logging.warning('這是警告訊息')
logging.error('這是錯誤訊息')
logging.critical('這是致命錯誤')
```

**輸出日誌到檔案**
```python
import logging

# 設定日誌輸出到檔案
logging.basicConfig(filename='app.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 測試不同層級的日誌
logging.debug('這是 Debug 訊息')
logging.info('這是一般的資訊')
logging.warning('這是警告訊息')
logging.error('這是錯誤訊息')
logging.critical('這是致命錯誤')
```

---

## 4. Python 命名規範（PEP 8）

| 項目 | 命名規則 |
|------|--------|
| Package | 小寫字母，底線可選，如 `my_package` |
| Module | 小寫字母，底線可讀性，如 `my_module.py` |
| Class | `CamelCase`，如 `MyClass` |
| Function & Variable | `snake_case`，如 `my_function` |

---

## 5. 物件導向程式設計（OOP）
一種程式設計範式，它透過類別(Class)和物件(Object)來組織程式碼

### 5.1 類別 (Class) 與 物件 (Object)

使用 class 關鍵字來定義類別，並使用它來建立物件
```python
# 定義 Animal 類別
class Animal:
    def __init__(self, name: str):
        self.name = name

# 建立物件
animal1 = Animal("Dog")
```

### 5.2 繼承（Inheritance）與多型（Polymorphism）
**繼承:**
允許子類別繼承父類別(Parent Class)的屬性和方法，並根據需要進行擴充或覆寫。
```python
# 定義父類別
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass  # 這是抽象方法，由子類別實作

# 定義子類別，繼承 Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# 使用子類別
dog = Dog("Buddy")

print(dog.make_sound())  # Woof!
```
**多型:**
允許子類別在繼承父類別的同時，重新定義其行為。
```python
# 定義父類別
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# 多型範例
dog = Dog("Buddy")

print(dog.make_sound())  # Woof!
```

### 5.3 封裝（Encapsulation）與抽象（Abstraction）
**封裝:**
將數據和行為封裝在類別內部，限制外部直接訪問。
```python
class Animal:
    def __init__(self, name: str,sex: str,age: int):
        self.name = name # 公開屬性
        self._sex=sex # 受保護屬性
        self.__age=age # 私有屬性（外部無法直接存取）

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog("Buddy","F",12)

print(dog.name)    # ✅ 可存取 (公開屬性)
print(dog._sex) #✅ 可存取 (受保護屬性, 但不建議)
# print(dog.__age)  # ❌ 會報錯，私有屬性無法直接存取
```
**抽象:**
隱藏具體實作，只暴露必要的功能給使用者。
```python
from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self, name: str):
        self.name = name
    @abstractmethod
    def make_sound(self):
        pass  # 這是抽象方法，由子類別實作

# 定義子類別，繼承 Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# 使用子類別
dog = Dog("Buddy")

print(dog.make_sound())  # Woof!
```
---
# Python 程式邏輯訓練
### 1. Palindrome Number
判斷數字是否為回文
1. 轉換為字串: 將數字轉換為字串格式
2. 反轉字串: 反轉字串已進行比較
3. 比較: 檢查原始和反轉字串是否相同

```python
def check_is_palindrome(x: int) -> bool:
    str_x = str(x)
    str_changed = str_x[::-1]
    if str_x == str_changed:
        return True
    else:
        return False

print(check_is_palindrome(121))
print(check_is_palindrome(-121))
print(check_is_palindrome(10))
```
### 2. Longest Palindromic Substring
找出最長回文子字串
1. 判斷回文性: 建立function檢查字串是否為回文
2. 檢查子字串: 判斷所有子字串是否為回文
3. 更新: 如果找到更長的回文，則更新
```python
def longest_palindrome(s: str) -> str:
    def check_is_palindrome_string(sub_s: str) -> bool:
        sub_s_changed = sub_s[::-1]
        if sub_s_changed == sub_s:
            return True
        else:
            return False
    len_of_s=len(s)
    longest_s=''
    for i in range(len_of_s):
        for j in range(i,len_of_s):
            if check_is_palindrome_string(s[i:j]) and (len(s[i:j])>len(longest_s)):
                longest_s=s[i:j]
    return longest_s

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
```
### 3. Remove Duplicates from Sorted List
使用遞迴創建唯一元素列表
1. 遍歷原列表: 檢查list中每個元素是否在前面已出現過
2. 添加唯一元素: 將新元素添加到新列表中
3. 計數檢查: 計算元素在列表前段中的出現次數是否為0
```python
def delete_duplicates(head: list[int]) -> list[int]:
    result = [head[i] for i in range(len(head)) if head[0:i].count(head[i]) == 0]
    return  result

print(delete_duplicates([1,1,2]))
print(delete_duplicates([1,1,2,3,3]))
```

---

# Git 版本控制基本操作

### 什麼是git
Git 是一種**分散式版本控制系統**，用來跟蹤和管理源代碼的變更，適用於個人專案或團隊協作開發。它可以讓開發者記錄程式碼的歷史變更，並且提供branch、merge、revert等功能，使多人協作時能有效管理代碼。
### 建立全新的Git Repository
1. 進入專案目錄並開啟終端機
2. 初始化 Git (git init)
3. 新增文件並提交 (git add/git commit)
4. 連結遠端倉庫 (git remote add origin `https://github.com/帳號名稱/專案名稱.git`)
### 複製已有的Git Repository
如果這個專案已經使用 Git 版控，可以從遠端倉庫複製到本地端
1. 使用 git clone 下載專案 (git clone `https://github.com/帳號名稱/專案名稱.git`)
2. 進入專案目錄
3. 確認當前狀態
### .gitignore的意義
.gitignore 是 Git 的設定檔，用來指定哪些檔案或資料夾不應該被 Git 追蹤或提交。
### 如何還原到某個commit的狀態
1. 臨時還原:  `git checkout <commit-id>`
   - 回到最新版本:  `git switch master`
2. 正式還原:  `git reset --hard <commit-id>`
### 如何切換branch
1. 切換到已存在的分支:  `git checkout <分支名稱>`
2. 創建並切換到新分支:  `git checkout -b <新分支名稱>`
### 何為衝突(conflict)
當Git**無法自動合併**兩個不同分支的變更時，就會發生**衝突**。這通常發生在**同一個檔案的相同區域被多個人修改**，導致 Git 不知道應該選擇哪個版本。


