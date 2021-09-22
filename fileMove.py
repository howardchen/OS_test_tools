import os
import shutil
from getHostname import getHostname

class FileMove:
    __doc__ = """這是一個用來做檔案複製以及將結果上傳的類別"""

    def __init__(self):
        # share_ip 可由外部設定
        self.share_ip = '192.168.10.5'
        # \\192.168.10.5\高鳳國際物流
        self.path = os.path.join('//', self.share_ip, '高鳳國際物流', '電腦室')
        self.upload_folder_name = getHostname()
        self.local_path = "D:/"
        self.download_folder_name = "downDir"

    @property
    def fileCopy(self):
        # download from nas server
        src = os.path.join(self.path, self.download_folder_name)
        dest = os.path.join(self.local_path, self.upload_folder_name)
        shutil.copytree(src, dest)
        return "files copy completed!"

    @property
    def uploadResult(self):
        # upload to nas server
        file_list = os.listdir(os.path.join(self.local_path, self.upload_folder_name))
        os.mkdir(os.path.join(self.path, self.upload_folder_name))
        for file in file_list:
            src = os.path.join(self.local_path, self.upload_folder_name, file)
            dest = os.path.join(self.path, self.upload_folder_name, file)
            shutil.move(src, dest)
        os.rmdir(os.path.join(self.local_path, self.upload_folder_name))
        return "report upload completed!"