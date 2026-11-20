# Checkpoint 006 — Super Pokémon Rumble EUR Rev 1

**Ngày:** 21/11/2026 · **Title ID:** `0004000000066D00` (EUR Rev 1 / EU_English). Không dùng cho bản USA `0004000000066C00`.

## Công việc đã hoàn tất

- [200 mục mới của `main.msbt`](ban_dich/main_CP006_200.jsonl) trong hai gói nguồn `018_main.txt` và `019_main.txt`.
- ID từ `#00413` đến `#00618`, bỏ qua các ID không thuộc nhóm dịch theo nguồn: `#00485`, `#00531`, `#00533`, `#00535`, `#00549`, `#00554`.
- Trong 200 mục: 191 mục chứa nội dung có thể đọc và 9 mục là dấu phân tách `-----` giữ nguyên.
- Chủ đề: Charge Battle, Hyper Mode, Team Battle, Two-Player, Password, StreetPass, Battle Locale, Release Point và hệ thống Move (Move-a-majig / Move Vendor / Move Swapper / Move School).
- Tất cả nội dung được dịch theo corpus trích xuất thật, không tạo câu mới không tồn tại trong nguồn.

## Tiến độ tích lũy

| Thành phần | Đã xử lý | Tổng cần dịch |
|---|---:|---:|
| `kaiwa.msbt` (CP003) | 158 | 158 |
| `main.msbt` (CP004–CP006) | 600 | 726 |
| **Toàn bộ 16 bảng** | **758** | **1.932** |
| **Còn lại** | **1.174** | |

Tỷ lệ: **39,23%** số record được phân loại `translate`. 2.590 mục khóa tiếng Anh vẫn không bị chỉnh sửa.

## QA

- Công cụ gốc `tools/nhan_ban_dich.py` nhập đủ **758** bản nháp, không trùng hoặc sai ID; còn **1.174** mục cần dịch.
- Lô 006 giữ nguyên **291 mã `{CTRL:hex}`** theo đúng chuỗi thứ tự trong nguồn.
- Unicode NFC, không có ký tự thay thế lỗi, không có mã placeholder sai; **0 dòng vượt 40 ký tự** khi bỏ mã định dạng và tính dấu chuyển trang như ngắt màn.
- 0 cảnh báo thuật ngữ mới. Tổng 13 cảnh báo còn lại từ CP003–CP005 là va chạm từ thông thường với từ điển Move, cần QA cảnh trước khi chốt.
- SHA-256 bản JSONL mới: `1cd6ead049ea0a0062c565dcd6412fdd32d51aa1f81a73552f741a778ed5f023`.

## Chưa hoàn thành

**Chưa repack MSBT/CX, chưa xử lý font tiếng Việt, chưa thử độ rộng glyph thực tế, chưa có patch đã test trên 3DS.** Toàn bộ câu mới đang mang trạng thái `ban_nhap`, không được hiểu thành đã nghiệm thu game.

**CP007:** tiếp tục `020_main.txt` + `021_main.txt`, còn 126 mục để chốt toàn bộ bảng `main.msbt`. Phải đối chiếu nguồn, giữ mã biến và xưng hô trước khi commit.
