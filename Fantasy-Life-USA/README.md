# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 008 HOÀN TẤT — 24/11/2026**

- Nguồn bàn giao: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip` · Title ID `0004000000113200` · **34.812 ID**.
- **Đã dịch/QA cấu trúc 10.500 / 34.812 (30,16%)**; còn **24.312**.
- **CP008 đủ 2.000 ID mới**: CP008a 1.610 Challenge/Quest/UI; CP008b 390 hội thoại nhiệm vụ.
- CP008b: `0105` mục **17–100** (84), toàn bộ `0106`, `0107`, `0108` (300), `0109` mục **1–6** (6).
- 200 ID `0070–0071` thuộc nhóm bản đồ/debug tiếng Anh thiếu nghĩa vẫn **HOLD**, không gộp vào bản được duyệt; các ID trong danh sách gộp không liên tiếp vì đoạn này bị để trống.
- Là % trên **chuỗi trong bộ bàn giao**, **không phải** tỷ lệ ROM đã được vá.
- Tất cả thay đổi chỉ trên nhánh `vh/fantasy-life-usa`. Không thay `main`.

## Nội dung CP008b

- **0105:** hướng dẫn Other Requests, Hansel và Gaites, sữa/milkshake, nông dân Carrottys/Carrotys, nhiệm vụ chống quái và vật phẩm.
- **0106:** Sweet Corn/Sweetcorn, Princess Laura, Professor Hughes, Paladin chống buồn ngủ, nông sản, Tufts, Barker, bưu điện và trang trí.
- **0107:** Radishellas, người đội hòm thư thất tình, các thợ thủ công, rạp xiếc bọ chét, các loại Charm, nhà tiên tri, pie/pudding và cướp biển.
- **0108:** Dragon Meat, Cashew/Honey, Bomba, Pepperonita, Calumnus, chương trình dẹp quái Tortuga, Fluffin và các nghiên cứu carp.
- **0109 #1–6:** Woodcutter tìm Fire Log, thuốc chuẩn bị đi săn kho báu và người tiên tri nghiên cứu Dragonflies.

Giữ tiếng Anh tên NPC, Life, item, skill, Rank, Bounty và địa danh. Lời Việt gần gũi, dí dỏm theo đúng nội dung gốc; giọng hội thoại khác với menu kỹ thuật. Giữ EN_A/EN_B theo từng ID.

## Khôi phục bản dịch đã duyệt

Trong thư mục `Fantasy-Life-USA`:

```bash
python3 unpack_batches.py
```

Script (chỉ dùng thư viện chuẩn Python) giải nén các tệp `.bz2.b64`/`.gz.b64` trong `translations/`, kiểm SHA-256, số ID và ô dịch rỗng, rồi tạo:

- `translations/cp008b-new-390.jsonl` — 390 mục CP008b.
- **`translations/cp008-complete-2000.jsonl`** — trọn 2.000 mục CP008.
- **`translations/merged-CP008-10500.jsonl`** — 10.500 ID tích lũy.
- Các checkpoint CP005 và CP006 riêng cũng được khôi phục.

Mỗi dòng có dạng `{"id":"FL-USA::...","vi":"bản dịch"}`. Ghép theo ID với `01_CAN_DICH.jsonl`; không ghi đè `raw_hex`, `controls_hex`, `references`, `alias_ids`, `length_bindings` hoặc văn bản nguồn.

**SHA-256 CP008b 390 mục:** `9640411f905472d66a00225a5ac0df777802835e0555d01fcb3d6d869556dec5`.

**SHA-256 CP008 2.000 mục:** `daeac626ec53a92aba0952cb36ca7c9638e977010ca3e7afbebcf1f01ccad6e6`.

## QA và giới hạn

- **QA tĩnh CP008b:** 390/390 ID có trong nguồn, không trùng các ID cũ; **5.531 token điều khiển** đúng nội dung và thứ tự, không rỗng, Unicode NFC và các đoạn tên item tô màu nguyên vẹn.
- Toàn bộ 10.500 ID tích lũy đúng bộ 34.812 nguồn, không trùng.
- 37 cảnh báo so chữ số thô đã được rà: gồm số viết chữ, dấu phân nghìn và token chia chữ số; một chỗ ghi thiếu đơn vị (1 nhúm Super Healing Powder, 0106#17) đã sửa trước bản chính.
- **Chưa đo tràn pixel và ngắt trang trên 3DS:** các token ngắt dòng/trang giữ đúng thứ tự nhưng vị trí trong câu Việt là sơ bộ, cần test runtime trước khi vá ROM.
- **Chưa xác nhận toàn bộ speaker/target và ngôi xưng bằng gameplay.** Bảng giọng nói hiện dựa vào nhóm thoại nguồn.
- **Chưa có bản patch font/glyph tiếng Việt hoặc RomFS/CIA chơi được.**

Tài liệu chi tiết: `CHECKPOINT-008-complete.md`, `QA-008b.md`, `NGOI_XUNG_CP008b.md`, `ISSUES-008b.md`.

**Tiếp theo:** gói `0109`, bắt đầu từ **mục 7** (6 mục đầu đã dịch ở CP008b). Nhóm `0070–0071` HOLD cần đối chiếu nguồn Nhật/bản chơi riêng.
