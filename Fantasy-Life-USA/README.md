# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 008a — 23/11/2026 · CP008 chưa hoàn thành**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip` · Title ID `0004000000113200` · **34.812 mục**.
- **10.110 / 34.812 ID đã biên dịch và QA cấu trúc (29,04%)**. Còn **24.702 ID**.
- CP001–CP007: 8.500; **CP008a +1.610**. Mục tiêu riêng CP008 là 2.000 ID; **còn 390**.
- Các gói `0070–0071` có **200 mục HOLD** vì nguồn debug/map Anh dịch thô không xác định được nghĩa: không nằm trong bảng gộp, không tính vào progress.
- Nhánh làm việc riêng `vh/fantasy-life-usa`; không sửa `main`.

## Nội dung CP008a

- **1.412 Challenge** (gói `0089` mục 7–100; `0090–0102`; `0103` mục 1–18). Các Life cần hạ quái, sử dụng skill, chế tạo, câu cá, thu vật phẩm, nhận Bounty và nâng kỹ năng. Giữ nguyên tên skill, Life, item, Rank và label Challenge.
- **198 mục Quest/UI/License/Story** (gói `0103` mục 19–100, `0104` và `0105` mục 1–16). Chỉ diễn giải các nhãn debug theo chức năng, không tự gán nhân vật hoặc cốt truyện.
- Đã sửa mẫu câu tiếng Việt máy móc trong Challenges (số lượng, chất lượng, loại món, kỹ thuật, địa điểm); rà đặc biệt nội dung bọc màu.

## Khôi phục bảng dịch trên GitHub

Ở thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Công cụ giải nén gzip/bzip2 từ các file base64 trong `translations/`, kiểm SHA-256, ID trùng, câu rỗng, sau đó xuất:
- `translations/cp008a-new-1610.jsonl` — 1.610 ID mới.
- **`translations/merged-CP008a-10110.jsonl` — 10.110 ID đã duyệt, không liên tục vì 0070–0071 chưa làm**.
- Các checkpoint trước, trong đó `cp005-complete-2000.jsonl`, `cp006-complete-2000.jsonl`.

Tệp CP008a lưu GitHub: `translations/cp008a-1610.jsonl.bz2.b64` (SHA-256 sau giải nén `083720e8654a1c53dc95d900c466133a5b4d6b3e31d1aaefd17ff61e80de750d`).

Mỗi dòng JSONL là `{"id":"FL-USA::...","vi":"..."}`, cần ghép vào `01_CAN_DICH.jsonl` gốc theo `id`. Không thay `source`, `raw_hex`, `controls_hex`, `references`, `length_bindings`, `alias_ids`.

## Chất lượng và giới hạn

- **QA cấu trúc CP008a:** 1.610 ID hợp lệ và riêng biệt, 0 ô dịch rỗng, 0 sai token; kiểm **12.735 token** đúng nội dung và thứ tự, Unicode NFC, 0 sai tên item trong marker màu, 0 sai số, 0 cảnh báo chiều dài thô.
- **Không coi QA cấu trúc là QA văn phong 100% hoặc QA máy 3DS.** Challenge theo mẫu được rà sửa, nhưng vẫn cần kiểm từng scene, font glyph, phân trang và tràn khung.
- Nguồn có nhiều `speaker=unknown`; xưng hô tạm, chưa có bảng quan hệ nhân vật đủ tin cậy.
- **Chưa có patch font, bản RomFS/CIA hoặc build chơi được**.

Tài liệu: `CHECKPOINT-008a.md`, `QA-008a.md`, `ISSUES-008a.md`, `NGOI_XUNG_CP008a.md`.

**Tiếp theo:** gói `0105` mục 17 trở đi (câu thứ 10.111 được duyệt nếu đạt); bổ sung **390 mục** để khép mục tiêu CP008. Vẫn cần quay lại xử lý riêng HOLD 0070–0071 khi có nguồn Nhật/ngữ cảnh game.
