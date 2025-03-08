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

## Detailed Usage Guide / 상세 사용 가이드

### Step 1: Initial Setup / 초기 설정

[EN]
1. Make sure you have installed:
   - Blender 4.0 or higher
   - MPFB2 addon (installed and activated in Blender)
   - Python 3.7 or higher
   - requests library (open terminal/command prompt and run: `pip install requests`)

2. Create a directory structure:
   ```
   any_folder/
   ├── mpfb_data/
   │   └── assetpacks/    # This will store downloaded assets
   └── download_temp/     # Temporary directory for downloads
   ```

3. Copy `config.py.example` to `config.py` and edit it:
   - Set `ASSET_DIR` to your assetpacks directory path
   - Set `DOWNLOAD_DIR` to your temporary download directory path
   Example:
   ```python
   ASSET_DIR = "C:/Users/YourName/Documents/mpfb_data/assetpacks"  # Use forward slashes
   DOWNLOAD_DIR = "C:/Users/YourName/Documents/download_temp"
   ```

[KR]
1. 다음 프로그램들이 설치되어 있는지 확인하세요:
   - Blender 4.0 이상
   - MPFB2 애드온 (Blender에 설치 및 활성화)
   - Python 3.7 이상
   - requests 라이브러리 (터미널/명령 프롬프트를 열고 실행: `pip install requests`)

2. 다음과 같은 폴더 구조를 만드세요:
   ```
   아무_폴더/
   ├── mpfb_data/
   │   └── assetpacks/    # 다운로드된 에셋이 저장될 폴더
   └── download_temp/     # 임시 다운로드 폴더
   ```

3. `config.py.example`을 `config.py`로 복사하고 수정하세요:
   - `ASSET_DIR`을 assetpacks 폴더 경로로 설정
   - `DOWNLOAD_DIR`을 임시 다운로드 폴더 경로로 설정
   예시:
   ```python
   ASSET_DIR = "C:/Users/사용자이름/Documents/mpfb_data/assetpacks"  # 슬래시(/) 사용
   DOWNLOAD_DIR = "C:/Users/사용자이름/Documents/download_temp"
   ```

### Step 2: Downloading Assets / 에셋 다운로드

[EN]
1. Open terminal/command prompt
2. Navigate to the scripts directory:
   ```bash
   cd path/to/your/scripts/folder
   ```
3. Run the download script:
   ```bash
   python download_assets.py
   ```
4. Wait for the download to complete:
   - You'll see progress for each file
   - Total download size is about 3GB
   - Downloads are saved automatically in your configured asset directory

[KR]
1. 터미널/명령 프롬프트를 엽니다
2. scripts 폴더로 이동합니다:
   ```bash
   cd scripts폴더의/경로
   ```
3. 다운로드 스크립트를 실행합니다:
   ```bash
   python download_assets.py
   ```
4. 다운로드가 완료될 때까지 기다립니다:
   - 각 파일별 진행상황이 표시됩니다
   - 전체 다운로드 크기는 약 3GB입니다
   - 다운로드된 파일은 설정한 에셋 디렉토리에 자동으로 저장됩니다

### Step 3: Loading Assets in Blender / Blender에서 에셋 로드

[EN]
1. Open Blender
2. Make sure MPFB2 addon is activated:
   - Go to `Edit > Preferences > Add-ons`
   - Search for "MPFB"
   - Check the box next to "MakeHuman Plugin For Blender 2"

3. Open Text Editor in Blender:
   - Click on the top bar of any panel
   - Select `Text Editor` from the dropdown menu
   - Or split your view and change one panel to Text Editor

4. Load the script:
   - Click `Text > Open`
   - Navigate to where you saved `bulk_load_assets.py`
   - Select and open the file

5. Run the script:
   - Click the "Run Script" button (▶️) in the Text Editor
   - Or press `Alt + P`

6. Monitor progress:
   - Press `Window + Alt + C` to open the System Console
   - Watch the loading progress
   - Wait for the "Processing complete!" message

7. After loading completes:
   - Save your Blender file
   - Close Blender completely
   - Restart Blender to see all loaded assets

[KR]
1. Blender를 실행합니다
2. MPFB2 애드온이 활성화되어 있는지 확인:
   - `Edit > Preferences > Add-ons` 메뉴로 이동
   - "MPFB" 검색
   - "MakeHuman Plugin For Blender 2" 옆의 체크박스 활성화

3. Blender의 텍스트 에디터 열기:
   - 아무 패널의 상단 바를 클릭
   - 드롭다운 메뉴에서 `Text Editor` 선택
   - 또는 화면을 분할하고 한 패널을 Text Editor로 변경

4. 스크립트 불러오기:
   - `Text > Open` 클릭
   - `bulk_load_assets.py` 파일이 있는 위치로 이동
   - 파일 선택 후 열기

5. 스크립트 실행:
   - 텍스트 에디터의 "Run Script" 버튼(▶️) 클릭
   - 또는 `Alt + P` 키 누르기

6. 진행상황 모니터링:
   - `Window + Alt + C`를 눌러 시스템 콘솔 열기
   - 로딩 진행상황 확인
   - "Processing complete!" 메시지가 나올 때까지 대기

7. 로딩 완료 후:
   - Blender 파일 저장
   - Blender 완전히 종료
   - Blender 재시작하여 로드된 에셋 확인

### Troubleshooting / 문제 해결

[EN]
Common download issues:
- "Permission denied": Run terminal as administrator
- "Directory not found": Check if your paths in config.py exist
- "ModuleNotFoundError: No module named 'requests'": Run `pip install requests`

Common loading issues:
- "MPFB operator not found": Check if MPFB2 addon is activated
- "File not found": Check if your asset directory path is correct
- Blender becomes unresponsive: Try loading fewer assets at once

[KR]
자주 발생하는 다운로드 문제:
- "Permission denied": 터미널을 관리자 권한으로 실행
- "Directory not found": config.py의 경로가 실제로 존재하는지 확인
- "ModuleNotFoundError: No module named 'requests'": `pip install requests` 실행

자주 발생하는 로드 문제:
- "MPFB operator not found": MPFB2 애드온이 활성화되어 있는지 확인
- "File not found": 에셋 디렉토리 경로가 올바른지 확인
- Blender가 응답하지 않음: 한 번에 더 적은 수의 에셋을 로드해보기

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