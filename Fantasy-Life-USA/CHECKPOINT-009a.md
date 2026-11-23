# Fantasy Life USA — Checkpoint 009a (24/11/2026)

**445 mục mới**: 0109#7–100 (94), 0110 (100), 0111 (100), 0112 (100), 0113#1–51 (51).

**Tích lũy 10.945/34.812 ID (31,44%)**, còn 23.867; CP009 mới hoàn thành 445/2.000 mục, cần 1.555 nữa. Đã dịch 178 EN_A và 267 EN_B, giữ nguyên tên item, Life, NPC và thuật ngữ quan trọng.

Chủ đề: Calumnus, Henrietta, Hansel, Pancake Paul; NPC, món ăn, nhiệm vụ và nghiên cứu quái trên Origin Island; tóm tắt Quest và yêu cầu trang bị/số lượng.

**Khôi phục**: `python3 unpack_batches.py` đọc `translations/cp009a-445.jsonl.bz2.b64`, xuất `translations/cp009a-new-445.jsonl` và `translations/merged-CP009a-10945.jsonl`. SHA-256 riêng CP009a: `5329d45ea3fa4122b06918697d005fbcddd9ffe83561175d39dca06350493586`; SHA-256 gộp: `7c543c059307efb3ecea0ce79246c5c2277717edd9764a798a2a737db4dd45a1`.

**Không tính** 200 ID debug/map 0070–0071 vì thiếu ngữ nghĩa xác thực. Từ 0114 xuất hiện nhiều nhãn Event/debug tiếng Anh dịch thô từ Nhật, phải phân loại rõ trước khi biên dịch.

Chưa có font/patch chạy thử trên Nintendo 3DS; chưa QA pixel width, ngắt trang, speaker/target hoặc hai nhánh nam/nữ runtime. Nhánh riêng `vh/fantasy-life-usa`, không sửa `main`.
