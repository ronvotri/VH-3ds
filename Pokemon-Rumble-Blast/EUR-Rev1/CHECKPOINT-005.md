# Checkpoint 005 — Super Pokémon Rumble EUR Rev 1

**Bản game:** `0004000000066D00` (EU English, EUR Rev1). Không áp dụng cho bản USA `0004000000066C00`.

## Kết quả

- Đã dịch tiếp **200 mục** từ `016_main.txt` và `017_main.txt`, thuộc `/msg/EU_English/main.msbt.cx`.
- Phạm vi: `#00202` đến `#00412`, gồm **200 ID thật thuộc diện cần dịch**, không thêm những index trống/thuộc nhóm giữ nguyên.
- [Bản dịch CP005](ban_dich/main_CP005_200.jsonl), SHA-256 `1593d5de2eebe9ec2ca20faf9cade6aed99b368a7585428aa71a9a98fa7cc7ec`.
- Nội dung: credits, thống kê chiến đấu, menu tạm dừng, xác nhận xóa save/StreetPass, local Two-Player, trạng thái Pokémon.
- Giữ nguyên tên người tham gia sản xuất, tên Pokémon và các Move/tên hệ thống chính. Những trạng thái như trúng độc, bỏng, đóng băng được Việt hóa.

## Tiến độ tích lũy

| Phần | Đã dịch |
|---|---:|
| `kaiwa.msbt` | 158 |
| `main.msbt` | 400 / 726 |
| **Tất cả các bảng** | **558 / 1.932 (28,88%)** |
| Còn cần dịch | **1.374** |
| Nhóm giữ EN theo bộ giao | 2.590 |

## QA tĩnh

- So lại 200 nguồn gốc theo ID/label; **200/200** hợp lệ.
- 30 mã `{CTRL:hex}` ở lô mới được bảo toàn chính xác thứ tự và số lượng.
- Không lỗi Unicode NFC, không trùng ID.
- Importer gốc `tools/nhan_ban_dich.py` nhận đủ 558 mục; báo còn 1.374 mục cần dịch.
- 5 cảnh báo từ bộ rà thuật ngữ tự động trong CP005 đều là va chạm từ thường với tên Move: `Assurance` xuất hiện trong QA credits, `Return` trong UI và `Fire` trong trạng thái "Sea of Fire"; không phải mất tên Move.
- Đo 40 ký tự/dòng là phép kiểm thô, **không** thay thế đo pixel thực tế. Credits quá dài cần QA riêng.

## Chưa hoàn thành

**Chưa có patch chạy được, chưa thử font tiếng Việt, chưa repack MSBT/CX, chưa test hiển thị và gameplay trên máy/giả lập.** Bản ZIP CP005 trong hội thoại bao gồm bản gộp 558 câu và 6.159 record sau importer.

**Bước tiếp:** dịch từ `018_main.txt` và tiếp tục gom QA kỹ thuật theo từng bảng, không sửa nhánh main.
