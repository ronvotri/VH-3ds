# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Dành riêng cho EUR Rev 1**, Title ID `0004000000066D00`, product `CTR-P-ACCP`, bảng tiếng Anh `EU_English`. **Không nhập vào game USA** `0004000000066C00`.

## Tiến độ đến Checkpoint 006

- Nguồn gốc **6.159 record / 16 MSBT**; gồm **1.932 mục cần dịch**, 2.590 mục giữ tiếng Anh, 443 debug, 1.194 rỗng.
- **758 / 1.932 mục đã xử lý (39,23%)**; còn **1.174 mục**.
- `kaiwa.msbt`: **158/158** mục.
- `main.msbt`: **600/726** mục.

| Checkpoint | Nguồn | Bản dịch | QA / ghi chú |
|---|---|---|---|
| CP003 | `kaiwa.msbt`, 158 mục | [JSONL](ban_dich/kaiwa_CP003_158.jsonl) | [CP003](CHECKPOINT-003.md) |
| CP004 | `014_main.txt` + `015_main.txt`, 200 mục | [JSONL](ban_dich/main_CP004_200.jsonl) | [CP004](CHECKPOINT-004.md) |
| CP005 | `016_main.txt` + `017_main.txt`, 200 mục | [JSONL](ban_dich/main_CP005_200.jsonl) | [CP005](CHECKPOINT-005.md) |
| CP006 | `018_main.txt` + `019_main.txt`, 200 mục | [JSONL](ban_dich/main_CP006_200.jsonl) | [CP006](CHECKPOINT-006.md) |

[Quy tắc xưng hô hội thoại](XUNG-HO-KAIWA.md).

## Quy tắc dịch

Giữ nguyên EN tên Pokémon, item, Move/Skill, tên riêng và thuật ngữ hệ thống/chế độ. Việt hóa lời thoại, menu, hướng dẫn, thông báo và trạng thái thông thường bằng tiếng Việt NFC; giọng thân thiện, tự nhiên, Gen Z có tiết chế. Không tự gán người nói từ tên nhãn. Bắt buộc giữ nguyên ID và mã `{CTRL:hex}`.

## QA / trạng thái bản vá

Đã QA bằng importer gốc: **758 mục nhập thành công**, nhóm giữ EN bất biến. CP006: **291 mã điều khiển đúng thứ tự, 0 cảnh báo thuật ngữ mới**. Các bản dịch ở trạng thái `ban_nhap`; chưa QA đầy đủ trên màn hình game.

**Chưa repack MSBT/CX, chưa vá font, chưa test gameplay 3DS, chưa tạo patch chơi được.**

CP007 dự kiến dịch tiếp `020_main.txt` và `021_main.txt`, còn 126 mục để hoàn tất `main.msbt`.
