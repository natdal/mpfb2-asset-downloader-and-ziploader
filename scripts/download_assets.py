import os
import requests
from pathlib import Path
import shutil
import logging
from typing import Dict, List, Tuple
from config import ASSET_DIR, DOWNLOAD_DIR, MIRROR1_BASE, MIRROR2_BASE

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 에셋 정의
ASSETS = {
    "cc0": {
        # 시스템 에셋
        "makehuman_system_assets": "System assets",
        "system_clothes_materials01": "Extra materials for system clothes",
        "system_hair_materials01": "Extra materials for system hair",
        
        # 타겟 에셋
        "animal01": "Various animal and furry transforms",
        "arms01": "Realistic arm deformations",
        "cheek01": "Realistic cheek deformations",
        "ears01": "Realistic ears deformations",
        "hands01": "Realistic hand deformations",
        "nose01": "Realistic nose deformations",
        
        # 포즈 에셋
        "poses01": "Various sitting poses",
        "poses02": "Various sports poses",
        
        # 머티리얼 에셋
        "skins01": "A set of natural female skins",
        "skins02": "A set of natural male skins",
        "skins03": "A set of non-natural skins",
        
        # 메시 에셋
        "bodyparts01": "A set of horns",
        "bodyparts04": "A set of nails",
        "bodyparts05": "A set of beards and moustaches",
        "dress01": "A set of female gowns and dresses",
        "equipment01": "A set of weapons",
        "eyebrows01": "A set of high-res eyebrows by Mindfront",
        "eyelashes01": "A set of high-res eyebrows by Mindfront",
        "glasses01": "A set of glasses",
        "gloves01": "A set of gloves",
        "hair01": "A set of mostly low-poly and stylized hair",
        "hats01": "A set of hats and caps",
        "hats02": "A set of helmets",
        "masks01": "A set of masks",
        "pants01": "A set of pants",
        "shirts01": "A set of t-shirts, sweaters and tops",
        "shoes01": "A set of shoes and boots",
        "skirts01": "A set of skirts",
        "suits01": "A set of formal suits by Margaret Toigo",
        "suits02": "A set of sci-fi and fantasy suits",
        "underwear01": "A set of female underwear",
        "underwear04": "A set of socks"
    },
    "ccby": {
        # 타겟 에셋
        "animal02": "Various animal and furry details by JALdMIC",
        "animal03": "Animal and furry head deforms by JALdMIC",
        "animal04": "Animal and furry full body transforms by JALdMIC",
        
        # 메시 에셋
        "bodyparts02": "A set of horns",
        "bodyparts03": "A set of tails and wings",
        "bodyparts06": "A set of beards and moustaches",
        "dress02": "A set of female gowns and dresses by Elvaerwyn",
        "dress03": "A set of female gowns and dresses",
        "equipment02": "A set of weapons",
        "equipment03": "Various equipment such as bags and tools",
        "glasses02": "A set of glasses",
        "hats03": "A set of hats and caps",
        "hats04": "A set of helmets",
        "hair02": "A set of mostly high-poly hair by Elvaerwyn",
        "hair03": "A set of alpha 7 hair adaptations and misc hair",
        "masks02": "A set of masks",
        "pants02": "A set of long-legged pants",
        "pants03": "A set of short legged pants swimming trunks",
        "shirts02": "A set of long sleeved cardigans, sweaters and shirts",
        "shirts03": "A set of short sleeved shirts, tunics and tops",
        "shoes02": "A set of low shoes, sneakers and sandals",
        "shoes03": "A set of boots",
        "skirts02": "A set of skirts",
        "suits03": "A set of thematic suits",
        "underwear02": "A set of female underwear and bikinis",
        "underwear03": "A set of underwear and swimwear"
    }
}

def create_directories() -> None:
    """필요한 디렉토리들을 생성합니다."""
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(ASSET_DIR, exist_ok=True)
    
    # 라이선스별 디렉토리 생성
    for license_type in ASSETS.keys():
        license_dir = os.path.join(ASSET_DIR, license_type)
        os.makedirs(license_dir, exist_ok=True)
        
        # 각 에셋별 하위 디렉토리 생성
        for asset_name in ASSETS[license_type].keys():
            asset_dir = os.path.join(license_dir, asset_name)
            os.makedirs(asset_dir, exist_ok=True)

def download_asset(license_type: str, asset_name: str) -> bool:
    """에셋을 다운로드하고 적절한 위치로 이동합니다."""
    # 대상 디렉토리의 파일 확인
    target_dir = os.path.join(ASSET_DIR, license_type, asset_name)
    if os.path.exists(target_dir):
        existing_files = os.listdir(target_dir)
        if any(f.endswith('.zip') for f in existing_files):
            logging.info(f"Skipping {asset_name} - already downloaded")
            return True

    # underwear02의 특수한 경우 처리 (CC-BY 라이선스이지만 파일명이 cc0로 되어있음)
    if asset_name == "underwear02" and license_type == "ccby":
        zip_names = ["underwear02_cc0.zip"]
    # CC-BY 라이선스의 경우 두 가지 파일명 형식 시도
    elif license_type == "ccby":
        zip_names = [f"{asset_name}_ccby.zip", f"{asset_name}_cc-by.zip"]
    else:
        zip_names = [f"{asset_name}_{license_type}.zip"]
    
    for zip_name in zip_names:
        download_path = os.path.join(DOWNLOAD_DIR, zip_name)
        
        for mirror_base in [MIRROR1_BASE, MIRROR2_BASE]:
            url = f"{mirror_base}/{asset_name}/{zip_name}"
            try:
                mirror_num = "1" if mirror_base == MIRROR1_BASE else "2"
                logging.info(f"Downloading {asset_name} from Mirror {mirror_num}...")
                
                # 헤더 먼저 확인
                response = requests.head(url, timeout=5)
                if response.status_code == 404:
                    continue
                    
                # 파일 크기 확인
                total_size = int(response.headers.get('content-length', 0))
                
                response = requests.get(url, stream=True, timeout=10)
                if response.status_code == 200:
                    downloaded_size = 0
                    with open(download_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                downloaded_size += len(chunk)
                                # 진행률 표시
                                if total_size:
                                    percent = (downloaded_size / total_size) * 100
                                    print(f"\rDownloading {asset_name}: {percent:.1f}% ({downloaded_size}/{total_size} bytes)", end="")
                    
                    print()  # 줄바꿈
                    
                    # 다운로드 성공 시 해당 라이선스/에셋 폴더로 이동
                    target_path = os.path.join(ASSET_DIR, license_type, asset_name, zip_name)
                    shutil.move(download_path, target_path)
                    logging.info(f"Successfully downloaded and moved {asset_name}")
                    return True
                    
            except requests.exceptions.Timeout:
                logging.warning(f"Timeout occurred while downloading from Mirror {mirror_num}")
            except requests.exceptions.RequestException as e:
                logging.warning(f"Mirror {mirror_num} failed for {asset_name}: {str(e)}")
            except Exception as e:
                logging.error(f"Unexpected error for {asset_name}: {str(e)}")
            
            # 실패시 임시 파일 삭제
            if os.path.exists(download_path):
                os.remove(download_path)
    
    return False

def main():
    """메인 실행 함수"""
    logging.info("Starting asset download process...")
    
    # 필요한 디렉토리 생성
    create_directories()
    
    # 성공/실패 카운터
    success_count = 0
    failed_assets = []
    
    # 라이선스별로 에셋 다운로드
    for license_type, assets in ASSETS.items():
        logging.info(f"\nProcessing {license_type} assets:")
        for asset_name, description in assets.items():
            if download_asset(license_type, asset_name):
                success_count += 1
            else:
                failed_assets.append(f"{license_type}/{asset_name}")
    
    # 결과 보고
    logging.info(f"\nDownload Summary:")
    logging.info(f"Successfully downloaded: {success_count} assets")
    if failed_assets:
        logging.warning(f"Failed to download {len(failed_assets)} assets:")
        for asset in failed_assets:
            logging.warning(f"- {asset}")
    else:
        logging.info("All assets were downloaded successfully!")

if __name__ == "__main__":
    main()