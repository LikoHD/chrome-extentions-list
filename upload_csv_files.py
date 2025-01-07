import os
import shutil
from datetime import datetime

def create_data_directory():
    """创建数据目录结构"""
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir

def get_desktop_csv_files():
    """获取桌面上的所有CSV文件"""
    desktop_path = os.path.expanduser("~/Desktop")
    csv_files = []
    for file in os.listdir(desktop_path):
        if file.endswith('.csv'):
            csv_files.append(os.path.join(desktop_path, file))
    return csv_files

def copy_files_to_data_dir(csv_files, data_dir):
    """复制文件到数据目录"""
    print("\n开始复制文件...")
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        destination = os.path.join(data_dir, file_name)
        shutil.copy2(file_path, destination)
        print(f"✓ 已复制: {file_name}")

def main():
    # 创建数据目录
    data_dir = create_data_directory()
    
    # 获取桌面CSV文件
    csv_files = get_desktop_csv_files()
    
    if not csv_files:
        print("未在桌面找到CSV文件！")
        return
    
    print(f"找到 {len(csv_files)} 个CSV文件:")
    for i, file_path in enumerate(csv_files, 1):
        print(f"{i}. {os.path.basename(file_path)}")
    
    # 复制文件
    copy_files_to_data_dir(csv_files, data_dir)
    
    print("\n✨ 所有文件已成功复制到 data 目录！")

if __name__ == "__main__":
    main() 