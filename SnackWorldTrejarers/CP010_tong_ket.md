# Snack World: Trejarers — Checkpoint 010

## Tiến độ
- Dịch từ nguồn ưu tiên **ID theo thứ tự 1140–1299**: **160 ID**, gồm **132 chuỗi mới** và **28 ID lặp** tương ứng đoạn trộm táo.
- Lũy kế: **1.300 / 23.091 ID = 5,63%**.
- QA tĩnh: **160/160 tag đúng nội dung và thứ tự**, **1.300 ID duy nhất**, dữ liệu nguồn khớp 1:1 ở các trường ID, file, hash, index và offset.
- Các đoạn: FairyPon/Belongings, vụ trộm táo, thiết kế vũ khí và Snack Shot, Master of Wood, Silver Sargent, cửa hàng P-gnocchi-0, Honeybun và màn cầu hôn.
- **Đã tạo ZIP**: `SnackWorld_Trejarers_VH_CP010.zip`, gồm `CP010_moi_160_ID.jsonl`, `CP010_luy_ke_1300_ID.jsonl`, `CP010_doi_chieu.md`, `README.md`.
- **Quan trọng:** GitHub hiện chỉ lưu nhật ký CP010, không khẳng định JSONL đã push. JSONL đầy đủ có trong ZIP cuộc trò chuyện.

## Trích bản Việt hóa
| Thứ tự | Bản dịch |
|---:|---|
| 1143 | Nhớ lưu thường xuyên, đó là bài học RPG vỡ lòng! ...Ơ, ta vừa nói RPG à? Ý ta là nhập môn phiêu lưu! |
| 1155 | Trời ơi! Sao ở đây chẳng ai chịu nghe tôi giải thích vậy!? |
| 1178 | Tôi vô tội! `<EBI>TÔI VÔ TỘI MÀÀÀ!</E>` |
| 1227 | Nó là quái vật khổng lồ, có thể hủy diệt thế giới chỉ trong bảy ngày! ...Nghe đồn thế. |
| 1247 | Đưa lịch sử duyệt web đây coi! |
| 1292 | Nói anh nghe một lý do vì sao quái vật chúng ta không thể thành vợ chồng đi? |

## QA còn thiếu
- Bản nguồn có ký tự `FairyPon<` ở ID 1142: phải kiểm tra byte/engine trước khi repack.
- Chưa xác nhận speaker mapping, cách chơi chữ và chi tiết màn hình.
- Chưa QA font dấu, line wrapping, giới hạn chuỗi, build CIA hay kiểm thử trên 3DS.

Nhánh riêng `vh/snack-world-trejarers`; không đụng `main`. CP011 bắt đầu từ thứ tự **1300**.
