import os
import re
from pathlib import Path

def fix_markdown_image_spaces(target_dir, md_file_path):
    # 檢查路徑是否存在
    if not os.path.exists(target_dir):
        print(f"錯誤: 找不到目錄 {target_dir}")
        return
    if not os.path.exists(md_file_path):
        print(f"錯誤: 找不到 Markdown 檔案 {md_file_path}")
        return

    # 讀取 Markdown 內容
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正則表達式解釋:
    # !\[(.*?)\] : 匹配圖片的 alt text (如 ![Description])
    # \((.*?)\)   : 匹配括號內的內容 (即檔案路徑)
    pattern = r'!\[(.*?)\]\((.*?)\)'

    count = 0

    def rename_callback(match):
        nonlocal count
        alt_text = match.group(1)
        original_link = match.group(2)
        
        # 取得純檔名 (避免路徑中包含子目錄的干擾)
        filename = os.path.basename(original_link)
        
        # 檢查檔名中是否有空格
        if ' ' in filename:
            old_file_path = os.path.join(target_dir, filename)
            
            # 如果在指定資料夾內確實存在這個含空格的檔案
            if os.path.isfile(old_file_path):
                new_filename = filename.replace(' ', '-')
                new_file_path = os.path.join(target_dir, new_filename)
                
                try:
                    # 執行實際的檔案更名
                    os.rename(old_file_path, new_file_path)
                    print(f"成功更名: '{filename}' -> '{new_filename}'")
                    
                    # 更新 Markdown 中的引用路徑 (保持原本的目錄結構，只改檔名)
                    new_link = original_link.replace(filename, new_filename)
                    count += 1
                    return f'![{alt_text}]({new_link})'
                except Exception as e:
                    print(f"更名失敗 {filename}: {e}")
        
        # 如果沒條件不符合，回傳原始字串
        return match.group(0)

    # 執行替換
    new_content = re.sub(pattern, rename_callback, content)

    # 寫回 Markdown 檔案
    if count > 0:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"\n處理完成！共修改了 {count} 處引用並更換了對應檔案。")
    else:
        print("\n未發現需要更換的檔案或引用。")

# --- 設定區域 ---
if __name__ == "__main__":
    # 請在此指定你的 D 資料夾路徑
    D_FOLDER = r'.' 
    
    # 請在此指定你的 Markdown 檔案路徑
    MD_FILE = r'index.md'

    fix_markdown_image_spaces(D_FOLDER, MD_FILE)
