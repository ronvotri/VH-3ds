# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 009b — 24/11/2026 · CP009 đang thực hiện**

- Bộ nguồn gốc: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, **34.812 ID**.
- **11.470 / 34.812 ID được dịch/QA cấu trúc (32,95%)**; còn **23.342**.
- CP001–CP008: 10.500 ID · CP009a: 445 · **CP009b: 525** ⇒ CP009 đã làm **970/2.000**, còn 1.030.
- Hai gói `0070–0071` gồm **200 nhãn bản đồ/debug HOLD** chưa đủ nghĩa, vẫn không tính vào số ID đã dịch. Gói `0114–0123` có nhãn Event/debug cần kiểm nguồn Nhật và cảnh game.
- Nhánh riêng `vh/fantasy-life-usa`, **không đụng `main`**.
- Đây là tiến độ dịch *danh sách chuỗi nguồn*, không phải % bản ROM đã Việt hóa chơi được.

## CP009b — 525 mục mới đã duyệt

| Gói | Phạm vi được duyệt | Số ID | Nội dung |
|---|---|---:|---|
| `0131` | #1–63 | 63 | Link Mode, Multiplayer, Bag, Crafting, License/Licence, biến tên động |
| `0132` | #34–100 | 67 | Cốt truyện và thành tựu Rank/Life |
| `0133` | #1–100 | 100 | Rank, Level, Dosh, đồng đội, khách đến chơi, Story |
| `0134` | #1–100 | 100 | Creator/Legend Rank, Grace, Divinus, Origin Island |
| `0135` | #1–52, #54–100 | 99 | God Rank, thành tựu và Challenge Angler |
| `0136` | Trừ #15, #69, #86, #98 | 96 | Challenge Angler/Hunter |
| **Tổng** | | **525** | **412 EN_A / 113 EN_B** |

**Không cộng** những chuỗi chỉ là tên skill/quái giữ nguyên English (`Counter Hook!`, `Dancing Arrows`, `Stormcaller`, `Thunderflap` và `Swimming Cactus`). Gói `0131` #64–100 chứa thống kê debug dịch thô nên chưa duyệt. Gói `0132` #1–33 là tên Bliss Upgrade/Feature cần giữ nguyên English, không coi chép lại là dịch.

Giữ tiếng Anh tên NPC, địa danh, item, skill, Life, Rank, tên cá/quái, cùng các thuật ngữ giao diện chính. Dịch phần hướng dẫn/tiến trình và tiêu đề nhiệm vụ tự nhiên, gọn, có dấu. Không gộp EN_A/EN_B: giữ nguyên khác biệt `Legendary/Legend`, `Creator/God`, `Wizard/Magician`, `License/Licence`.

## Khôi phục checkpoint

Ở thư mục `Fantasy-Life-USA` chạy:

```bash
python3 unpack_batches.py
```

Script giải nén các payload JSONL gốc đã commit trong `translations/`, kiểm checksum SHA-256, các ID trùng và ô dịch rỗng, tạo:

- `translations/cp009b-new-525.jsonl` — 525 mục mới.
- `translations/cp009-work-in-progress-970.jsonl` — CP009a+b 970 mục, **chưa hoàn tất CP009**.
- `translations/merged-CP009b-11470.jsonl` — 11.470 mục tích lũy.
- Các CP005/CP006/CP008 riêng 2.000 mục như trước.

SHA-256 CP009b (525): `e38269628a64ae4fe69632ab316909e2a0082978bbe1cc0077d789eb0d86e46e`.

SHA-256 gộp 11.470: `c5e9891991ab8808c47e27924a97a4291f80f5654519a08f648d77b56cbb8255`.

Mỗi dòng dịch gồm `{"id":"FL-USA::...", "vi":"..."}`. Ghép theo ID với `01_CAN_DICH.jsonl` của bộ ZIP nguồn, không sửa `source`, `raw_hex`, `controls_hex`, `references`, `alias_ids` hay `length_bindings`.

## QA và việc còn lại

- 525/525 ID mới tồn tại trong nguồn, không trùng 10.945 ID cũ, không rỗng, Unicode NFC.
- **51 mã `{CTRL:hex}` của batch mới được giữ đúng nguyên chuỗi/thứ tự**; rà toàn bộ 11.470 ID không có mismatch.
- Đã rà **11 trường hợp chữ số** từ nguồn như `five` → `5`, vị trí `Level 15`, không đổi trị số.
- **Chưa QA runtime:** font tiếng Việt, pixel width, ngắt trang, Multiplayer/Link Mode, nhánh giới tính/speaker, bản vá RomFS/CIA.
- Sổ thuật ngữ/QA chi tiết: `CHECKPOINT-009b.md`, `QA-009b.md`, `ISSUES-009b.md`, `THUAT_NGU-009b.md`.

**Tiếp theo:** các Challenge rõ nghĩa ở gói `0137` và sau đó; **còn 1.030 ID để khép CP009**, không tính nhãn debug thiếu ngữ nghĩa hoặc tên riêng không dịch.
