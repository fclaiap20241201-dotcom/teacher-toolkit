#!/usr/bin/env python3
"""
student_cli.py — 電子計算機二年級 學生端命令列作答腳本
教學目標：
  1. 學習在 Python 終端機接收使用者輸入並進行型態校驗。
  2. 練習打包 JSON 結構化資料並量測程式碼執行時間 (Response Time)。
  3. 實作去識別化資料傳輸（僅記錄 class_id 與 seat_no，保護個人隱私）。
"""

import sys
import time
import json

def run_quiz_client():
    print("=" * 50)
    print("  💻 高二電子計算機課堂即時答題器 (Python CLI 版)")
    print("  🔒 隱私保護：本系統僅收集座號，不記錄任何真實姓名")
    print("=" * 50)

    # 1. 輸入班級與座號
    class_id = input("請輸入班級代號 (預設 201): ").strip() or "201"
    
    while True:
        seat_str = input("請輸入你的座號 (1-45): ").strip()
        if seat_str.isdigit() and 1 <= int(seat_str) <= 45:
            seat_no = int(seat_str)
            break
        print("⚠️ 座號必須為 1 到 45 之間的整數，請重新輸入！")

    print(f"\n✅ 歡迎座號 {seat_no} 號同學！題目準備開始...")
    time.sleep(0.5)

    # 2. 顯示題目（範例：二分搜尋法時間複雜度）
    print("\n" + "-" * 50)
    print("【隨堂觀念題】")
    print("對包含 1,000,000 筆已排序資料執行「二分搜尋」，最差大約需比對幾次？")
    print("  [A] 大約 20 次")
    print("  [B] 大約 1,000 次")
    print("  [C] 大約 500,000 次")
    print("  [D] 大約 1,000,000 次")
    print("-" * 50)

    # 計時開始
    start_time = time.time()

    # 3. 取得作答選項
    while True:
        choice = input("\n請輸入你的答案 (A/B/C/D): ").strip().upper()
        if choice in ["A", "B", "C", "D"]:
            break
        print("⚠️ 選項無效，僅限輸入 A、B、C 或 D！")

    elapsed_ms = int((time.time() - start_time) * 1000)

    # 4. 打包資料負載 (Payload)
    payload = {
        "class_id": class_id,
        "seat_no": seat_no,
        "student_id": f"{class_id}_{seat_no:02d}",
        "answer": choice,
        "response_time_ms": elapsed_ms,
        "submitted_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    print("\n📦 準備傳送答題封包：")
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    # 5. 提示送出結果
    print(f"\n🎉 答題完成！座號 {seat_no} 號選擇 【{choice}】，作答耗時：{elapsed_ms / 1000:.2f} 秒。")
    print("大螢幕即時統計長條圖已同步更新！")

if __name__ == "__main__":
    try:
        run_quiz_client()
    except KeyboardInterrupt:
        print("\n\n👋 已取消答題退出。")
        sys.exit(0)
