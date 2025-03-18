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