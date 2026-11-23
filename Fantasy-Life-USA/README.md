# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 009a — 24/11/2026 · CP009 đang thực hiện**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, 34.812 ID được bàn giao.
- **Đã dịch/QA cấu trúc 10.945/34.812 (31,44%)**; còn **23.867** ID.
- CP001–CP008 đã duyệt: 10.500 ID. **CP009a: +445 ID**, còn **1.555 ID** để đạt mục tiêu CP009 là 2.000.
- `0070–0071` gồm **200 chuỗi map/debug HOLD**, tiếp tục không tính vào số đã dịch.
- Nhánh riêng `vh/fantasy-life-usa`, **không sửa `main`**.

## Phạm vi CP009a

| Gói | Phạm vi | Số dòng | Nội dung |
|---|---|---:|---|
| `0109` | 7–100 | 94 | Calumnus, Pancake Paul, Henrietta, Hansel, nhiệm vụ các đảo |
| `0110` | 1–100 | 100 | Origin Island, các món ăn, sinh vật, Furlin/Fluffkin, chiến binh |
| `0111` | 1–100 | 100 | Lord Leo, chuyên gia cá, nghiên cứu quái, phụ kiện, nhiệm vụ đảo |
| `0112` | 1–100 | 100 | Tóm tắt quest, điều kiện item, số lượng và quái |
| `0113` | 1–51 | 51 | Tóm tắt nhiệm vụ EN_B, Rank, trang bị |
| **Tổng** | | **445** | **178 EN_A, 267 EN_B** |

## Khôi phục 10.945 câu

Chạy trong thư mục `Fantasy-Life-USA`:

```bash
python3 unpack_batches.py
```

Script giải nén các gói `.bz2.b64` và `.gz.b64` ở `translations/`, xác minh SHA-256, số dòng và ID duy nhất, sau đó tạo:

- `translations/cp009a-new-445.jsonl` — 445 bản dịch mới.
- `translations/merged-CP009a-10945.jsonl` — 10.945 bản dịch tích lũy.
- Các checkpoint CP005/CP006/CP008 riêng 2.000 câu như trước.

SHA-256 445 câu: `5329d45ea3fa4122b06918697d005fbcddd9ffe83561175d39dca06350493586`. SHA-256 bản gộp: `7c543c059307efb3ecea0ce79246c5c2277717edd9764a798a2a737db4dd45a1`.

Bản dịch chỉ chứa `id` và `vi` của từng mục, cần ghép theo `id` với `01_CAN_DICH.jsonl` trong ZIP nguồn. Không tự ý sửa trường source, raw_hex, alias_ids, references hoặc length_bindings.

## Quy tắc và chất lượng

- **Giữ tiếng Anh** tên NPC, địa danh, Life, item, skill, Rank và thuật ngữ chính; thoại tiếng Việt tự nhiên, hài đúng nhân vật; hệ thống dùng văn phong rõ ràng.
- **EN_A/EN_B tách biệt theo ID**, không ép cùng tên vật phẩm hoặc tên quái. Ngôi xưng theo mạch quest, không khẳng định speaker không có dữ liệu.
- **QA cấu trúc:** 445/445 ID có nguồn, không trùng với 10.500 ID cũ; 5.843 token `{CTRL:hex}` giữ đúng danh sách và thứ tự, 497 vùng tô màu, 21 mục có điều kiện giới tính; Unicode NFC. Toàn bộ 10.945 ID không trùng.
- **47 cảnh báo so chữ số** đã đối chiếu: phần lớn do chữ số viết thành chữ Việt; một chỗ là số quái được giải thích lặp lại trong ngoặc ở nguồn. Xem `QA-009a.md`.
- **CHƯA KIỂM TRÊN MÁY:** font tiếng Việt, tràn khung theo chiều rộng glyph, các token ngắt trang, nhánh nam/nữ thực tế, ánh xạ ngôi xưng scene. Chưa có patch RomFS/CIA chơi được.

## Tiếp theo

Từ `0114` trở đi xuất hiện nhiều nhãn Event/debug bị dịch thô từ Nhật, **không tự chế nội dung** hoặc tính điểm khi chưa xác minh. Ưu tiên string UI/skill/quest có nghĩa rõ, tiếp tục kiểm 200 HOLD trong `0070–0071` sau khi có nguồn Nhật hoặc screenshot.

Tài liệu: `CHECKPOINT-009a.md`, `QA-009a.md`, `NGOI_XUNG_CP009a.md`, `ISSUES-009a.md`.
