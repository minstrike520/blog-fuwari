import os
import re
import argparse

def process_file(file_path):
    """處理單一檔案的取代邏輯"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 規則 1: 將 category 換行清單轉為單行
        p1 = r"categories:\n\s*-\s*(.*)"
        r1 = r"category: \1"
        new_content = re.sub(p1, r1, content)

        # 規則 2: date -> published
        new_content = new_content.replace("date: ", "published: ")

        # 只有在內容有變動時才寫入，減少硬碟 I/O
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False

    except Exception as e:
        print(f"處理 {file_path} 時發生錯誤: {e}")
        return False

def main():
    # 設定 argparse
    parser = argparse.ArgumentParser(description="批次修改 Markdown 檔案的 Front Matter 格式")
    parser.add_argument("dir", help="指定要處理的資料夾路徑")

    args = parser.parse_args()
    target_dir = args.dir

    if not os.path.isdir(target_dir):
        print(f"錯誤：'{target_dir}' 不是一個有效的資料夾。")
        return

    # 執行批次處理
    count = 0
    files = [f for f in os.listdir(target_dir) if f.endswith('.md')]

    print(f"開始處理資料夾：{target_dir}，共找到 {len(files)} 個 .md 檔...")

    for filename in files:
        file_path = os.path.join(target_dir, filename)
        if process_file(file_path):
            print(f" [已修改] {filename}")
            count += 1
        else:
            print(f" [無變動] {filename}")

    print(f"\n處理完成！總計修改了 {count} 個檔案。")

if __name__ == "__main__":
    main()
