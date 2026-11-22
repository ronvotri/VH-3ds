# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 004 — 23/11/2026**

- Nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip` · Title ID `0004000000113200` · **34.812 mục nguồn**.
- **Đã dịch 2.500/34.812 (7,18%)**: CP001 100 · CP002 200 · CP003 200 · **CP004 2.000** (gói 0006–0025). **Còn 32.312**.
- CP004: trang bị, vũ khí, phụ kiện, vật liệu, cá, nấm, nội thất, mô tả hài hước, thông báo và phần đầu hướng dẫn gameplay. Mỗi gói 100 mục, 20 gói liên tục.
- Nhánh Việt hóa **`vh/fantasy-life-usa`** không sửa nhánh `main`.

## Khôi phục toàn bộ bảng dịch

Tại thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Script giải nén bốn checkpoint từ các file văn bản nén ở `translations/`, kiểm tra SHA-256, dữ liệu JSONL và 2.500 ID duy nhất rồi tạo:

- `translations/batch-001.jsonl`: CP001, 100 câu.
- `translations/cp002-new-200.jsonl`: CP002, 200 câu.
- `translations/cp003-new-200.jsonl`: CP003, 200 câu.
- `translations/cp004-new-2000.jsonl`: CP004, 2.000 câu.
- **`translations/merged-001-025.jsonl`: 2.500 câu tích lũy**.

Mỗi dòng chứa `{"id":"FL-USA::...", "vi":"bản dịch có dấu"}`. Ghép với `01_CAN_DICH.jsonl` của ZIP nguồn bằng `id`; không thay đổi `source`, `raw_hex`, `alias_ids`, `references`, `length_bindings`.

## Quy tắc dịch & QA

- Giữ **tên riêng, địa danh, Life, item, skill và thuật ngữ chính** bằng tiếng Anh.
- Tiếng Việt có dấu, tự nhiên và dí dỏm theo ngữ cảnh; hệ thống/lưu dữ liệu thì rõ nghĩa và nghiêm túc.
- Giữ toàn bộ token `{CTRL:hex}` trong đúng thứ tự và nội dung.
- Giữ riêng `EN_A` và `EN_B` theo ID; không ép chung biến thể.
- Nguồn có `speaker=unknown`; đối chiếu ngôi xưng NPC thực tế chỉ có thể QA theo cảnh. Không gán bừa tuổi, quan hệ, giới tính.
- Xem `NGOI_XUNG.md`, `CHECKPOINT-004.md` và `QA-004.md`.

**QA tĩnh CP004:** 2.000 ID mới được đối chiếu nguồn; 0 ID trùng trong 2.500 mục; 0 bản dịch rỗng; 0 sai thứ tự token; Unicode NFC PASS. Sàng lọc độ dài sơ bộ không phát hiện mục > max(120, 1.7× nguồn), nhưng kiểm tràn chữ thực tế **CHƯA LÀM**.

**CHƯA PHẢI PATCH CHƠI ĐƯỢC:** Chưa vá font tiếng Việt, chưa export RomFS/CIA/3DS, chưa kiểm tra hiển thị trên máy. Một số câu nhiều token trong gói 0025 cần kiểm context.

**Tiếp theo:** gói `0026`, từ mục thứ **2.501**. Tiếp tục nhắm 2.000 câu mỗi checkpoint nhưng không hạ tiêu chuẩn QA.
