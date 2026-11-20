# Checkpoint 003 — Việt hóa hội thoại `kaiwa`

Ngày 20/11/2026. Đầu vào: `SuperPokemonRumble-EUR-Rev1-BoDeDich-2026-11-20.zip`.

| Chỉ tiêu | Giá trị |
|---|---:|
| EN records, 16 bảng MSBT | 6.159 |
| Mục cần dịch | 1.932 |
| Đã viết VI thực tế, giữ ID | **158** |
| Toàn bộ `kaiwa.msbt` cần dịch | **158/158** |
| Còn dịch ở bảng khác | **1.774** |
| Bảng tên/thuật ngữ giữ EN | 2.590 |
| Cảnh báo kiểm thuật ngữ | 4 (khớp giả) |
| Lỗi thứ tự/mã `{CTRL:hex}` | **0** |
| Lỗi import theo ID trong công cụ gốc | **0** |
| QA render/font/gameplay | **Chưa làm** |

**Phạm vi:** Chuỗi `EUR-REV1::/msg/EU_English/kaiwa.msbt.cx#00000` ... `#00161`. Không có bản dịch cho index rỗng `#00064`, `#00117`, `#00144`, `#00145`.

Đã đối chiếu corpus `01_CAN_DICH.jsonl` với bản nguồn `00_TOAN_BO_EN.jsonl`, import thử bằng `tools/nhan_ban_dich.py`: 158 nhập thành công, 1.774 chưa dịch, `english_preserved=2590`. Bản trên GitHub và bản JSONL bàn giao có **158 ID và nội dung VI khớp** qua kiểm tra chuỗi mã điểm Unicode.

**Bốn cảnh báo:** `Awesome` trong lời khen #00014; `Amazing` #00016; `Wrap` trong trích dẫn #00058; `Return` trong lời hướng dẫn #00078. Đều là từ ngữ thông thường bị gợi ý nhầm là tên Move; không bổ sung lại từ EN máy móc.

**Nguyên tắc ngôi xưng:** `kaiwa` có nhãn TALK cảnh nhưng không cung cấp speaker ID chuẩn. Đã cố định phong cách giọng cho các nhóm tình huống có bằng chứng (Pawniard kiêu ngạo vs dân thị trấn thân thiện), các cảnh chưa chứng minh danh tính ghi chờ ảnh/gameplay. Xem `XUNG-HO-KAIWA.md`.

**Lưu ý kỹ thuật:** Bộ ZIP có 16 MSBT giải LZH8, không có patch. Nhiều font BCFNT thiếu dấu VI. Chưa đưa file vào binary game hay đo khung chữ. Đừng dùng file này để vá USA title `0004000000066C00`.

**Ưu tiên Checkpoint 004:** `main.msbt` (726 mục cần dịch) và thông báo `NoticeDesc.msbt` (376 mục); tiếp tục test nhập dữ liệu theo từng batch.
