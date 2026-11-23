# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 006c, phần 1 — 23/11/2026**

- Nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, 34.812 mục được chọn để giao dịch.
- **Đã dịch 5.600 / 34.812 (16,09%)**, còn **29.212 ID**.
- CP001–004: 2.500 · CP005: 2.000 · CP006a: 500 · CP006b: 500 · **CP006c-01: 100** (gói 0056).
- Riêng CP006: **1.100/2.000 câu** hoàn thành, còn 900 câu để đóng CP006. Không khẳng định đã dịch các gói 0057–0065.
- Toàn bộ nằm trên nhánh `vh/fantasy-life-usa`; **không thay nhánh main**.

## Nội dung đợt CP006c-01

- **0056-001–023:** Bà Henrietta nhớ chồng và con, đàn gà, các nhiệm vụ Mountain/Cave Mushrooms. Chú ý nhánh `con trai/con gái` và đại từ theo ngữ cảnh.
- **0056-024–053:** Khách sành ăn, `Superior/Super Boiled Veggies`, `Juicy Burger`, `Rustic Rainbow Trout`; giữ tên item khác nhau giữa EN_A/EN_B.
- **0056-054–086:** Timmy, Royal Grasshopper, Rhino Beetle, Iron Stag Beetle; giữ tiền thưởng, menu, giọng trẻ con tinh nghịch.
- **0056-087–100:** Paladin, suối nước nóng, nhân vật dùng White Gel tưởng là đồ tráng miệng.

## Tái tạo 5.600 bản dịch

Ở thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Công cụ kiểm SHA-256 và 5.600 ID duy nhất cho tất cả checkpoint, sau đó tạo `translations/merged-001-056.jsonl`. File mới của CP006c là `translations/cp006c-new-100.jsonl`; trên GitHub, nguồn nén là `translations/cp006c-100.jsonl.bz2.b64`. Tất cả JSONL chứa `{"id":"...","vi":"..."}` và được ghép vào `01_CAN_DICH.jsonl` của bộ gốc bằng ID. Không sửa `raw_hex`, `source`, `alias_ids`, `references` hay `length_bindings`.

## Chất lượng và hạn chế

- Giữ nguyên 932 token `{CTRL:hex}` đúng nội dung và thứ tự; 100 ID gốc đều hợp lệ, không trùng 5.500 ID cũ, Unicode NFC.
- Kiểm đối chiếu toàn bộ tên item nằm trong marker màu của gói 0056: không phát hiện sai khác.
- Chưa có ánh xạ speaker theo scene chắc chắn; ngôi xưng hiện theo cụm thoại và cần thử thực tế.
- **Chưa vá font Việt, chưa kiểm ngắt trang/pixel width/nhánh giới tính runtime, chưa có patch/CIA chơi được.**
- Xem `CHECKPOINT-006c-01.md` và `QA-006c-01.md`.

**Tiếp theo:** gói 0057, câu thứ **5.601**, không đếm câu chưa dịch hoặc chưa QA.
