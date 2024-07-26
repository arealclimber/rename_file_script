
import os
import shutil

# 寫死輸入資料夾跟輸出資料夾
def rename_and_move_files(source_folder, destination_folder):
    # 確保來源資料夾路徑存在
    if not os.path.exists(source_folder):
        print(f"來源資料夾 '{source_folder}' 不存在")
        return

    # 確保目標資料夾存在，如果不存在則創建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"已創建目標資料夾 '{destination_folder}'")

    # 定義要排除的檔案名稱
    excluded_files = ['.DS_Store']

    # 獲取來源資料夾中的所有檔案，排除指定檔案
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f not in excluded_files]

    # 排序檔案名稱
    files.sort()

    # 重命名檔案並移動到目標資料夾
    for index, file in enumerate(files, start=1):
        old_path = os.path.join(source_folder, file)
        new_name = f"report_thumbnail_{index}{os.path.splitext(file)[1]}"
        new_path = os.path.join(destination_folder, new_name)

        try:
            shutil.copy2(old_path, new_path)
            print(f"已將 '{file}' 複製並重命名為 '{new_name}'")
        except Exception as e:
            print(f"處理 '{file}' 時發生錯誤: {str(e)}")

# 設定來源和目標資料夾路徑
source_folder = "/Users/cafeca/cafeca/python/rename_file_name/input"
destination_folder = "/Users/cafeca/cafeca/python/rename_file_name/output"

rename_and_move_files(source_folder, destination_folder)

# 指定目標資料夾，直接更改資料夾內所有檔案的檔名
# import os
# def rename_files(folder_path):
#     # 確保資料夾路徑存在
#     if not os.path.exists(folder_path):
#         print(f"資料夾 '{folder_path}' 不存在")
#         return

#     # 獲取資料夾中的所有檔案
#     files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

#     # 排序檔案名稱
#     files.sort()

#     # 重命名檔案
#     for index, file in enumerate(files, start=1):
#         old_path = os.path.join(folder_path, file)
#         new_name = f"report_thumbnail_{index}.png"
#         new_path = os.path.join(folder_path, new_name)

#         try:
#             os.rename(old_path, new_path)
#             print(f"已將 '{file}' 重命名為 '{new_name}'")
#         except Exception as e:
#             print(f"重命名 '{file}' 時發生錯誤: {str(e)}")

# # 從使用者輸入獲取資料夾路徑
# folder_path = input("請輸入目標資料夾的路徑：")
# rename_files(folder_path)