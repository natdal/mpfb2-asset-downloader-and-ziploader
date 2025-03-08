# MPFB2 Asset Downloader / MPFB2 에셋 다운로더

[EN] An unofficial utility to automate downloading assets from [MakeHuman Community Asset Packs](https://static.makehumancommunity.org/assets/assetpacks.html) and loading them into Blender using MPFB2.

[KR] [MakeHuman Community의 에셋팩 페이지](https://static.makehumancommunity.org/assets/assetpacks.html)에서 제공하는 에셋들을 자동으로 다운로드하고 Blender에서 로드할 수 있도록 도와주는 비공식 도구입니다.

> **Note**: This is a personal utility, not an official tool of MakeHuman Community or MPFB2.
> 
> **참고**: 이 도구는 MakeHuman Community나 MPFB2의 공식 도구가 아닌, 개인이 제작한 유틸리티입니다.

## What This Tool Can Do / 이 도구로 할 수 있는 것

1. Automatic Asset Pack Downloads / 에셋팩 자동 다운로드:
   - [EN] Automatically downloads all CC0 and CC-BY licensed asset packs
   - [EN] Automatically categorizes by license type
   - [EN] Auto-retry on download failure
   - [KR] CC0 및 CC-BY 라이선스의 모든 에셋팩을 자동으로 다운로드
   - [KR] 라이선스 타입별로 자동 분류
   - [KR] 다운로드 실패 시 자동 재시도

2. Automatic Asset Loading in Blender / Blender 자동 로드:
   - [EN] Automates MPFB2's "Load pack from zip file" feature
   - [EN] Sequentially loads all downloaded asset packs
   - [EN] Tracks loading success/failure status
   - [KR] MPFB2의 "Load pack from zip file" 기능을 자동화
   - [KR] 다운로드된 모든 에셋팩을 순차적으로 로드
   - [KR] 로드 성공/실패 상태 추적

## Requirements / 필요 조건

- Blender 4.0+
- MPFB2 addon installed and activated / MPFB2 애드온 설치 및 활성화
- Python 3.7+
- requests library / requests 라이브러리 (`pip install requests`)

## Installation / 설치 방법

[EN] 1. Clone this repository:
[KR] 1. 저장소를 클론합니다:
```bash
git clone https://github.com/natdal/mpfb2-asset-downloader-and-ziploader.git
```

[EN] 2. Copy and modify config file:
[KR] 2. 설정 파일을 복사하고 수정합니다:
```bash
cp config.py.example config.py
```

## Configuration / 설정 방법

[EN] Edit `config.py` with your settings:
[KR] `config.py` 파일을 열고 설정을 수정하세요:

```python
# Asset pack directory path / 에셋팩이 저장될 디렉토리 경로
ASSET_DIR = "your/asset/directory/path"  # ex: "C:/Users/YourUsername/Documents/BlenderProjects/mpfb_data/assetpacks"

# Download settings / 다운로드 설정
DOWNLOAD_DIR = "your/download/directory"  # Temporary download path / 임시 다운로드 경로

# License type settings / 라이선스 타입 설정
LICENSE_TYPES = ["cc0", "ccby"]
```

## Usage / 사용 방법

### 1. Asset Pack Downloads / 에셋팩 다운로드

[EN] 1. Open a terminal/command prompt and navigate to the script directory:
[KR] 1. 터미널/명령 프롬프트를 열고 스크립트 디렉토리로 이동합니다:
```bash
cd scripts
```

[EN] 2. Run the download script:
[KR] 2. 다운로드 스크립트를 실행합니다:
```bash
python download_assets.py
```

[EN]
- All asset packs will be downloaded and automatically categorized in the specified directory
- Progress will be displayed in the terminal
- Download time may vary depending on network status

[KR]
- 모든 에셋팩이 지정된 디렉토리에 다운로드되고 자동으로 분류됩니다
- 진행 상황이 터미널에 표시됩니다
- 다운로드는 시간이 걸릴 수 있으며, 네트워크 상태에 따라 다릅니다

### 2. Asset Loading in Blender / Blender에서 에셋 로드

[EN]
1. Launch Blender and ensure MPFB2 addon is activated
2. Open Blender's text editor and load the `bulk_load_assets.py` script
3. Run the script
4. You can check progress in System Console (Window + Alt + C)
5. Restart Blender after all assets are loaded

[KR]
1. Blender를 실행하고 MPFB2 애드온이 활성화되어 있는지 확인합니다
2. Blender의 텍스트 에디터를 열고 `bulk_load_assets.py` 스크립트를 불러옵니다
3. 스크립트를 실행합니다
4. System Console(Window + Alt + C)에서 진행 상황을 확인할 수 있습니다
5. 모든 에셋이 로드되면 Blender를 재시작합니다

## Directory Structure / 디렉토리 구조

[EN] After downloading, the directory structure will look like this:
[KR] 다운로드 후 디렉토리 구조는 다음과 같습니다:
```
mpfb_data/assetpacks/
├─cc0/
│  ├─animal01/
│  │  └─animal01_cc0.zip
│  ├─bodyparts01/
│  │  └─bodyparts01_cc0.zip
│  └─...
└─ccby/
   ├─animal02/
   │  └─animal02_ccby.zip
   ├─bodyparts02/
   │  └─bodyparts02_cc-by.zip
   └─...
```

## Notes / 주의사항

[EN]
- Downloading assets can take a significant amount of time (approximately 1GB+)
- If a download fails, re-running the script will continue from where it left off
- After loading assets, you must restart Blender
- Loading a large number of assets at once may use a lot of system resources

[KR]
- 에셋 다운로드에는 상당한 시간이 소요될 수 있습니다 (전체 약 3GB+)
- 다운로드 중 네트워크 오류가 발생할 경우, 스크립트를 다시 실행하면 이어서 다운로드됩니다
- 에셋 로드 후에는 반드시 Blender를 재시작해야 합니다
- 대용량의 에셋을 한번에 로드할 경우 시스템 자원을 많이 사용할 수 있습니다

## Troubleshooting / 문제 해결

### Download Issues / 다운로드 문제
[EN]
- "Connection error" - Check your internet connection and try again
- "File not found" - Mirror server may be temporarily unavailable. Please try again later

[KR]
- "Connection error" - 인터넷 연결을 확인하고 다시 시도하세요
- "File not found" - 미러 서버가 일시적으로 불가능할 수 있습니다. 잠시 후 다시 시도하세요

### Loading Issues / 로드 문제
[EN]
- Assets not appearing - Restart Blender
- Memory shortage - Load fewer assets at once

[KR]
- 에셋이 보이지 않음 - Blender를 재시작하세요
- 메모리 부족 - 더 적은 수의 에셋을 한 번에 로드하세요

## ~~Contribution / 기여 방법~~ *(Not Yet Available / 아직 지원하지 않음)*

<details>
<summary>[EN/KR] Future contribution guide / 향후 기여 가이드</summary>

[EN]
> ~~1. Fork this repository~~
> ~~2. Create a new branch (`git checkout -b feature/amazing-feature`)~~
> ~~3. Commit your changes (`git commit -m 'Add some amazing feature'`)~~
> ~~4. Push your branch (`git push origin feature/amazing-feature`)~~
> ~~5. Create a Pull Request~~

[KR]
> ~~1. 이 저장소를 포크합니다~~
> ~~2. 새로운 브랜치를 만듭니다 (`git checkout -b feature/amazing-feature`)~~
> ~~3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)~~
> ~~4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)~~
> ~~5. Pull Request를 생성합니다~~

</details>

## License / 라이선스

[EN] This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

[KR] 이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## Acknowledgments / 감사의 글

[EN]
- [MPFB2](https://github.com/makehumancommunity/mpfb2) - MakeHuman Plugin For Blender 2
- [MakeHuman Community](https://static.makehumancommunity.org/assets/assetpacks.html) - Asset Pack Provider
- All asset creators

[KR]
- [MPFB2](https://github.com/makehumancommunity/mpfb2) - MakeHuman Plugin For Blender 2
- [MakeHuman Community](https://static.makehumancommunity.org/assets/assetpacks.html) - 에셋팩 제공
- 모든 에셋 제작자들

## Disclaimer / 면책 조항

[EN] This tool is not an official tool of MakeHuman Community or MPFB2. All asset copyrights belong to their respective creators. This tool simply automates the download and load process.

[KR] 이 도구는 MakeHuman Community나 MPFB2의 공식 도구가 아닙니다. 에셋의 저작권은 각 제작자에게 있으며, 이 도구는 단순히 다운로드와 로드 과정을 자동화할 뿐입니다.

## Issues / 문의사항

[EN] If you encounter any issues, please create a GitHub issue.

[KR] 문제가 발생하면 GitHub 이슈를 생성해주세요. 