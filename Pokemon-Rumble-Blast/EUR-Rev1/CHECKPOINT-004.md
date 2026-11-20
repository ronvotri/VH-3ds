# Checkpoint 004 — Super Pokémon Rumble EUR Rev 1

**Nguồn:** `SuperPokemonRumble-EUR-Rev1-BoDeDich-2026-11-20.zip`, Title ID `0004000000066D00`. Không nhầm bản USA `0004000000066C00`.

## Đã thực hiện

- Dịch/ghi nhận **200 mục** `main.msbt` trong hai gói `014_main.txt` và `015_main.txt`, lưu tại [`ban_dich/main_CP004_200.jsonl`](ban_dich/main_CP004_200.jsonl).
- Phạm vi ID `#00000–#00201`; `#00162` và `#00185` là hai mục rỗng trong nguồn nên không thêm bản dịch.
- Bao gồm Toy Shop, StreetPass, Player Cards, Mii/Play Coins, danh sách Pokémon, bộ lọc, và thống kê trận.
- Đã bảo toàn token `{CTRL:hex}`, tên Pokémon, item, Move/Skill, các thuật ngữ và tên riêng cần giữ tiếng Anh.
- 200 mục theo phân loại nguồn gồm **184 mục có văn bản/ký tự cần xử lý** và **16 mục chỉ gồm token hoặc ký hiệu**. Mỗi mục vẫn ở trạng thái `ban_nhap`.

## Tiến độ corpus

| Bảng | Đã xử lý | Tổng cần dịch |
|---|---:|---:|
| `kaiwa.msbt` (CP003) | 158 | 158 |
| `main.msbt` (CP004) | 200 | 726 |
| **Toàn dự án** | **358** | **1.932** |

**Còn 1.574 mục.** Phần giữ nguyên tiếng Anh có 2.590 mục, không bị sửa.

## QA kỹ thuật

Chạy importer `tools/nhan_ban_dich.py` đi kèm ZIP: **358/358 ID hợp lệ**, 151 mã `{CTRL:hex}` mới đúng thứ tự, 0 ID trùng, 0 lỗi Unicode, số mục cần dịch còn lại 1.574.

Có 4 cảnh báo thuật ngữ mới: `Return`, `Awesome`, `Amazing`, `Protect`, vốn là các từ tiếng Anh thông dụng trong ngữ cảnh tương ứng, không phải Move cần giữ ở đây. Tổng cảnh báo của 2 checkpoint là 8.

Kiểm sơ bộ độ dài dòng sau khi xử lý token chuyển trang: 0 dòng quá 40 ký tự. Đây **không** thay cho thử độ rộng glyph và màn hình 3DS.

## Giới hạn

Chưa nhập/repack MSBT/CX, chưa sửa font, **chưa build patch hoặc test trên máy/giả lập**. Bản gộp 6.159 record, báo cáo QA và CSV so sánh EN/VI có trong ZIP bàn giao CP004.

**Đợt kế tiếp:** `016_main.txt` (100 mục) rồi tiếp đến `017_main.txt`. Kiểm lại ngôi xưng bằng cảnh thật nếu xuất hiện hội thoại có người nói.
