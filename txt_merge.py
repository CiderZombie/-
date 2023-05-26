import os

def merge_text_files(folder_path, output_file):
    merged_text = ''

    # 폴더 내의 모든 메모장 파일을 순회
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                merged_text += file.read()

    # 병합된 텍스트를 새로운 파일에 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(merged_text)

# 병합할 메모장 파일이 있는 폴더 경로
folder_path = r'C:\Users\ldh1020\OneDrive - KccGlass\바탕 화면\kccfc\1.업무\★회계★\1. 마감및 결산\3. 고정자산\PC 확인\8. PC QR 관리\.venv\텍스트 파일 모음'

# 병합된 메모장 파일의 저장 경로와 이름
output_file = r'C:\Users\ldh1020\OneDrive - KccGlass\바탕 화면\kccfc\1.업무\★회계★\1. 마감및 결산\3. 고정자산\PC 확인\8. PC QR 관리\.venv\텍스트 파일 모음\병합본\병합.txt'

# 메모장 파일 병합 실행
merge_text_files(folder_path, output_file)
