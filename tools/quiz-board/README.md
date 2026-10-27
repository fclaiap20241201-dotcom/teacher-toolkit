# ⚡ Quiz Board — 課堂即時答題大螢幕看板

> 專案用途：高二電子計算機課程隨堂搶答、觀念診斷與即時排行榜工具  
> 適用單元：單元一（Python 演算法與資料結構）與單元二（Firebase 課堂即時連線實作）  
> 關聯雲端：Firebase 專案 `my-teaching-tools`  
> 隱私保護：學生免登入、免註冊，僅以 `班級代號 + 座號`（去識別化）參與互動

---

## 📂 模組結構

```text
tools/quiz-board/
├── index.html       # 教師端投影大螢幕看板（即時長條圖、繳交率、搶答速度排行榜）
├── student.html     # 學生端行動/網頁作答器（輸入座號、大按鈕極速作答）
├── student_cli.py   # 學生端 Python 終端機腳本（練習終端互動與 JSON 封包構建）
├── questions.json   # 預設高二演算法核心題庫（二分搜尋、泡沫排序、Stack/Queue、Big-O）
├── firestore.rules  # Firestore 安全規則（防重複、防竄改、格式約束）
└── README.md        # 本使用與課堂引導手冊
```

---

## 🚀 快速開始（三步驟課堂上手）

### 步驟 1：啟動本機預覽伺服器
在 `tools/quiz-board/` 目錄下執行極簡 Python 靜態伺服器：
```bash
cd "/Users/fengchenglai/Google Drive/我的雲端硬碟/teacher-toolkit/tools/quiz-board"
python3 -m http.server 8080
```

### 步驟 2：教師端投影大螢幕
- 瀏覽器開啟 `http://localhost:8080/index.html`。
- 投影至教室大螢幕。
- 可點擊「🎲 隨機模擬 10 人」快速演練動態長條圖與排行榜跳動效果。
- 點擊「揭曉正解」會平滑高亮正確選項並展開詳解說明。

### 步驟 3：學生端連線作答
- **網頁版**：學生手機或 Chromebook 連至 `http://<教師電腦IP>:8080/student.html`，輸入座號（例如 15）即可一鍵作答。
- **Python CLI 版**：學生在上機教室電腦執行：
  ```bash
  python3 student_cli.py
  ```
  輸入班級與座號，體驗終端機結構化資料封包傳輸！

---

## 🔒 課堂資安與學生隱私設計 (Teacher Guardrails)

1. **零真實姓名收集**：
   - 資料庫只允許記錄格式為 `{class_id}_{seat_no}` 之代號（例如 `201_05`）。
2. **防作弊與覆寫約束**：
   - 透過 `firestore.rules` 約束：活動結束（`is_active == false`）時即刻阻擋寫入；且僅允許寫入屬於該座號之 Document。
3. **無憑證洩漏風險**：
   - 學生端純提交選項，不需持有或下載 Firebase Service Account 私鑰。
