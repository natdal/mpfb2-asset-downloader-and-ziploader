import bpy
import os
import time
from config import ASSET_DIR, LICENSE_TYPES

def load_asset(filepath):
    """단일 에셋을 로드합니다."""
    try:
        result = bpy.ops.mpfb.load_pack(filepath=filepath)
        return result == {'FINISHED'}
    except Exception as e:
        print(f"Error loading {filepath}: {str(e)}")
        return False

def process_directory(base_dir):
    """디렉토리 내의 모든 zip 파일을 처리합니다."""
    success_files = []
    failed_files = []
    
    # 모든 zip 파일 찾기
    zip_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.zip'):
                zip_files.append((os.path.join(root, file), os.path.relpath(os.path.join(root, file), base_dir)))
    
    total_files = len(zip_files)
    print(f"\nFound {total_files} zip files in {os.path.basename(base_dir)}")
    
    # 각 파일 처리
    for i, (filepath, relpath) in enumerate(zip_files, 1):
        print(f"\nProcessing [{i}/{total_files}]: {relpath}")
        if load_asset(filepath):
            print(f"Successfully loaded: {relpath}")
            success_files.append(relpath)
        else:
            print(f"Failed to load: {relpath}")
            failed_files.append(relpath)
    
    return success_files, failed_files

def main():
    if not os.path.exists(ASSET_DIR):
        print(f"Error: Asset directory not found: {ASSET_DIR}")
        print("Please check your config.py file and make sure ASSET_DIR is set correctly.")
        return
    
    all_success = []
    all_failed = []
    
    # 각 라이선스 타입 처리
    for license_type in LICENSE_TYPES:
        license_dir = os.path.join(ASSET_DIR, license_type)
        if os.path.exists(license_dir):
            print(f"\n{'='*20} Processing {license_type.upper()} assets {'='*20}")
            success, failed = process_directory(license_dir)
            all_success.extend(success)
            all_failed.extend(failed)
    
    # 최종 결과 출력
    print("\n" + "="*60)
    print("Final Results:")
    print(f"Successfully loaded: {len(all_success)} files")
    print(f"Failed to load: {len(all_failed)} files")
    
    if all_failed:
        print("\nFailed files:")
        for file in all_failed:
            print(f"  - {file}")
    
    print("\nProcessing complete! You may need to restart Blender to see all loaded assets.")

if __name__ == "__main__":
    main()