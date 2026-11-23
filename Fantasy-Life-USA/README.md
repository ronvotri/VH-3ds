# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 005b — 23/11/2026 · phần 2 của CP005**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, **34.812 mục**.
- **Đã dịch 4.100 / 34.812 ID (11,78%)**: CP001 100 · CP002 200 · CP003 200 · CP004 2.000 · CP005a 700 · **CP005b 900**.
- Còn **30.712 ID**.
- CP005 đặt mục tiêu 2.000 câu mới: đã hoàn thành 700 + 900 = 1.600; **còn 400 câu**, chưa khép CP005.
- Giữ thay đổi trên nhánh riêng `vh/fantasy-life-usa`, không sửa `main`.

## CP005b — các gói 0033–0041

- 0033–0036: Big Egg, Mustard, Gaites, Samantha, hội thoại nhiệm vụ với nhiều nhánh nhận/từ chối/giao/để sau.
- 0037–0039: thoại đời thường, Farley, các yêu cầu chế tạo, Tufts, mèo thích cá và chó Barker.
- 0040: khách mê Barley Juice/thịt, rau của Farley, Harmony mê nội thất u ám, lũ Radishys.
- 0041: Radishellas, người đội hòm thư thất tình, nhà phê bình ẩm thực Alfredo, bà may đồ cho cháu gái.
- Giữ riêng biến thể `EN_A`/`EN_B` theo ID, nhất là tên item `Super`/`Superior`.

## Khôi phục 4.100 bản dịch

Từ thư mục `Fantasy-Life-USA` chạy:

```bash
python3 unpack_batches.py
```

Script giải nén và kiểm SHA-256 các tệp dịch CP001–CP005b, kiểm 4.100 ID duy nhất, tạo `translations/merged-001-041.jsonl` cùng bản riêng từng đợt. Dữ liệu mỗi dòng: `{"id":"FL-USA::...", "vi":"bản dịch"}`.

Ghép theo `id` với `01_CAN_DICH.jsonl` trong ZIP nguồn; giữ nguyên `source`, `raw_hex`, `alias_ids`, `references`, `length_bindings`. Không đưa JSONL nén trực tiếp vào RomFS.

## Quy tắc và chất lượng

- Giữ tên nhân vật, tên vùng, item, skill, Life và thuật ngữ quan trọng bằng tiếng Anh.
- Việt ngữ có dấu, gần gũi, hài hước đúng cá tính NPC. Không tự suy đoán quan hệ, tuổi hoặc giới tính khi thiếu ngữ cảnh.
- Giữ nguyên mọi token `{CTRL:hex}` theo đúng số lượng và thứ tự; giữ đủ các biến thể nút lựa chọn, marker giới tính và nội dung xuống dòng.
- **QA tĩnh CP005b:** 900/900 ID đạt, 0 trùng, 0 bản dịch rỗng, 0 sai danh sách token; Unicode NFC PASS. SHA-256 dữ liệu CP005b giải nén: `d3146947fbbcfea183fb6cd095138f9a055cfb9bf84c5e5190e779d62464de7b`.
- **Chưa kiểm** font Việt, pixel width/overflow, ngôi xưng theo scene, các nhánh runtime, việc build CIA và patch.

Tài liệu chi tiết: `CHECKPOINT-005b.md`, `QA-005b.md`, `NGOI_XUNG.md`, `NGOI_XUNG_CP005b.md`.

**Tiếp theo:** gói 0042, từ mục thứ **4.101**; cần 400 mục nữa để hoàn thành đích CP005.
