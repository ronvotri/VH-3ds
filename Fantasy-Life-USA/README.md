# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 010a — 24/11/2026 · CP010 chưa hoàn tất**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, **34.812 chuỗi ID**.
- **13.022 / 34.812 ID đã xử lý, qua QA cấu trúc (37,41%)**; còn **21.790**.
- CP001–CP009: 12.500 ID; **CP010a: +522 ID**, mục tiêu CP010 2.000 ID → **còn 1.478**.
- Trong phạm vi 563 mục vừa kiểm, **41 ID HOLD** không được tính vào số câu dịch: tên skill/item thuần Anh và nhãn debug mơ hồ.
- 200 mục bản đồ/debug **0070–0071** vẫn HOLD từ CP007, không nằm trong 13.022.
- Một nhãn tiếng Tây Ban Nha cũ `Orbe de especialidad` còn cần xác minh; không tuyên bố tất cả 13.022 ID đều đã Việt hóa hoàn hảo.
- Chỉ làm việc trên nhánh **`vh/fantasy-life-usa`**, không sửa `main`.

## Phạm vi CP010a

| Gói | ID duyệt | Nội dung |
|---|---:|---|
| 0147#33–100 | 68 | Challenge Tailor, Paladin, đánh quái |
| 0148#1–100 | 93 | Challenge Alchemist, giữ 7 tên skill/item thuần Anh |
| 0149#1–100 | 100 | Challenge Cook, Woodcutter, Carpenter |
| 0150#1–100 | 91 | Challenge Carpenter, Magician, giữ 9 tên nghi là skill/item |
| 0151#1–22 | 20 | Challenge cuối nhóm, 2 tên riêng HOLD |
| 0151#23–62 | 40 | Tên màu giao diện tùy biến |
| 0153#1–100 | 80 | Tên nhóm chất liệu, vật phẩm, nội thất; nhãn debug không rõ nghĩa HOLD |
| 0154#1–33 | 30 | Loại trang bị, 3 mã mơ hồ HOLD |
| **Tổng** | **522** | **41 mục mới HOLD, không tính tiến độ** |

Tên item, skill, NPC, Life, Rank và địa danh được giữ nguyên tiếng Anh. Câu chơi chữ ở tên Challenge được chuyển ngữ tự nhiên, dễ đọc. Các nhóm vật liệu chung (như Ore, Crystal) được dịch khi là **loại vật phẩm**, không phải tên riêng của item.

## Khôi phục toàn bộ dữ liệu

Trong thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Chương trình đọc các file bzip2/gzip + base64 trong `translations/`, kiểm SHA-256 và ID trùng, áp **một sửa lỗi Blacksmith từ CP009**, tạo:
- `translations/cp010a-new-522.jsonl` — 522 ID mới.
- `translations/merged-CP010a-13022.jsonl` — 13.022 ID đã duyệt, bao gồm bản sửa CP009.
- Các checkpoint CP005/CP006/CP008/CP009 riêng đã có từ trước.

Nguồn GitHub: `translations/cp010a-522.jsonl.bz2.b64`. SHA-256 dữ liệu mới (giải nén): `e70f143f443d6890bd47113106effc320779be8f06205509b2c068a54fd86083`. SHA-256 gộp: `637113202084ac176043917ce18d5913c6712aece71e94b4b642a5f591fbd78b`.

**Danh sách HOLD của đợt:** `HOLD-CP010a-NOT-COUNTED.csv.bz2.b64` — chỉ để rà soát, không ghép vào bảng dịch. Giải base64, sau đó giải bzip2 để lấy CSV.

Mỗi dòng dịch có dạng `{"id":"FL-USA::...","vi":"..."}`. Ghép với `01_CAN_DICH.jsonl` trong bộ gốc theo ID. Không tự sửa `source`, `raw_hex`, `references`, `alias_ids` hoặc các mã điều khiển `{CTRL:hex}`.

## QA và hạn chế

**QA cấu trúc:** 522/522 ID thuộc nguồn gốc, không trùng 12.500 ID cũ, không có câu rỗng, Unicode NFC đạt; bản gộp 13.022 giữ đúng **63.414 token điều khiển** (gói mới là nhãn ngắn nên có 0 token mới). Không phát hiện bất nhất khi cùng một tiêu đề English đã được dịch ở các CP trước. Đã giữ lại số `10` của `10 Wishes Come True`.

**Chưa QA:** font tiếng Việt, độ rộng pixel, ngắt trang, menu màu theo RGB và nhánh game trên 3DS; chưa có patch RomFS/CIA chơi được. Đây là % ID nguồn đã xử lý, **không phải % ROM đã Việt hóa chơi được**.

Xem `CHECKPOINT-010a.md`, `QA-010a.md`, `ISSUES-010a.md`, `THUAT_NGU-010a.md`.

**Tiếp theo:** những thông báo/UI người chơi thực sự nhìn thấy ở gói `0182–0188` (một phần có token cần rà theo câu), tiếp tục không tính chỉ tên NPC/skill ở `0155–0181`.
