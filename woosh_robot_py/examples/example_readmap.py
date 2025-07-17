import sys
import os
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))
print(f"Project root added to sys.path: {project_root}")

# 修改导入语句，使用正确的模块路径
try:
    from woosh.proto.map.mark_pb2 import MarkInfo  # 改用 mark_pb2 中的 MarkInfo
except ImportError as e:
    print(f"Error importing proto module: {e}")
    print("Please make sure proto files are compiled and in the correct location")
    sys.exit(1)

def read_map_info(filepath):
    """读取并解析 MarkInfo protobuf 文件"""
    mark_info = MarkInfo()
    
    try:
        # 读取二进制 protobuf 文件
        with open(filepath, 'rb') as f:
            mark_info.ParseFromString(f.read())
            
        print("\nMark Info Details:")
        print("-" * 50)
        print(f"版本: {mark_info.version}")
        print(f"SDK版本: {mark_info.sdkv}")
        
        for i, storage in enumerate(mark_info.storages, 1):
            print(f"\n储位 {i}:")
            print(f"  ID: {storage.identity.id}")
            print(f"  编号: {storage.identity.no}")
            print(f"  描述: {storage.identity.desc}")
            
            print("  Dock位置:")
            print(f"    x: {storage.pose.dock.x}")
            print(f"    y: {storage.pose.dock.y}")
            
            print("  实际位置:")
            print(f"    x: {storage.pose.real.x}")
            print(f"    y: {storage.pose.real.y}")
            
            print("  导航设置:")
            print(f"    到达方式: {storage.nav.arr}")
            
            print("  对接设置:")
            print(f"    识别参数: {storage.dock.identify}")
            print(f"    验证参数: {storage.dock.verify}")
        print("-" * 50)
        
        return mark_info
        
    except Exception as e:
        print(f"Error reading map info: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <map_info_file>")
        sys.exit(1)
        
    map_file = sys.argv[1]
    if not os.path.exists(map_file):
        print(f"Error: File {map_file} does not exist")
        sys.exit(1)
        
    map_info = read_map_info(map_file)
    if map_info is None:
        sys.exit(1)

if __name__ == "__main__":
    main()
