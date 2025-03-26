import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# 対象ディレクトリを指定
directory = os.getenv("PATH_TO_CSV")

# ディレクトリ内のすべてのCSVファイルを取得
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # ファイルのフルパスを取得
        file_path = os.path.join(directory, filename)
        
        # CSVファイルを読み込む
        df = pd.read_csv(file_path)
        
        # 'views'列が0でも空欄でもないものを抽出
        df_filtered = df[df['Views'].notna() & (df['Views'] != '0')]
        
        # 新しいCSVファイルとして保存（元のファイル名に '_filtered' を追加）
        filtered_file_path = os.path.join(directory, f'{os.path.splitext(filename)[0]}_filtered.csv')
        df_filtered.to_csv(filtered_file_path, index=False)
        
        # 結果を表示（オプション）
        print(f'Processed {filename}')
        print(df_filtered)
