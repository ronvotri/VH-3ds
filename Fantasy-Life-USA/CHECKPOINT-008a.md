# Fantasy Life USA — Checkpoint 008a 🇻🇳

**23/11/2026 · CP008 phần 1**

- **1.610 ID mới** đã qua QA cấu trúc, bao gồm **1.412 Challenge** và **198 Quest/UI/License/Story**.
- Tổng **10.110/34.812 mục (29,04%)**, còn 24.702. Mục tiêu CP008 2.000, còn **390**; không tuyên bố CP008 đã hoàn thành.
- Phạm vi gói **0089 #7–100**, **0090–0104 đầy đủ**, **0105 #1–16**. Gói 0089 #1–6 thuộc CP007.
- **200 ID gói 0070–0071** vẫn HOLD riêng, không gộp và không tính đã dịch.
- Tiếp nối **0105 #17**. Giữ branch `vh/fantasy-life-usa`, không sửa `main`.

## Phong cách
Challenge dùng câu mệnh lệnh gọn, diễn giải bằng tiếng Việt, giữ tên vật phẩm, tên Skill, Life, Rank, Bounty, tên Challenge. Quest/UI dùng giọng hướng dẫn trung tính. Nhãn debug chỉ dịch theo ý nghĩa chức năng; không tự chế giọng NPC.

## Dữ liệu
- `translations/cp008a-1610.jsonl.bz2.b64`: bản JSONL mới bzip2 + base64 để lưu GitHub.
- `python3 unpack_batches.py`: kiểm SHA-256 và khôi phục `translations/cp008a-new-1610.jsonl`, `translations/merged-CP008a-10110.jsonl`.
- SHA-256 CP008a 1.610 ID: `083720e8654a1c53dc95d900c466133a5b4d6b3e31d1aaefd17ff61e80de750d`.
- SHA-256 bản gộp 10.110 ID: `4635ebd8b9bf7abcf3da3e251e86baa506dbe36e341fcc5bf5e317b5113cc3fd`.

**Giới hạn:** chưa có patch font tiếng Việt hay bản ROM chạy được, chưa kiểm tràn pixel/điều khiển trong game. QA 1.610 câu là QA cấu trúc, không tuyên bố QA ngữ nghĩa 100% theo scene.
