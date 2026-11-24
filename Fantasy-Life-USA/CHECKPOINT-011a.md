# Fantasy Life (USA) — CP011a — Votri Valley

**14,973 / 34.812 ID đã xử lý (43.01%)**, thêm **473** mục mới; còn **19,839**. CP011: 473/2.000. Một nhãn Tây Ban Nha cũ vẫn giữ nguyên; không coi toàn bộ số ID là đã Việt hóa.

## Phạm vi
| Gói | Phạm vi | Số ID mới |
|---|---|---:|
| 0341 | #97–100 | 4 |
| 0342–0345 | Toàn bộ, mỗi gói 100 | 400 |
| 0348 | #1–66, #90–99; trừ 17 nhãn bảo vệ | 59 |
| 0351 | #1–10 | 10 |
| Tổng | | **473** |

Mô tả món ăn, thuốc, giáp, gỗ, nguyên liệu chế tạo; hướng dẫn trang bị, câu cá, bắn cung, skill và các nhiệm vụ Napollon/Daphne, Jem, Mallow. Giữ tên riêng, item, skill, Life, HP/SP và các chỉ số. Mô tả các loại nguyên liệu chung được dịch theo nghĩa gốc; EN_A và EN_B không bị gộp.

## QA cấu trúc
- Đối chiếu 34.812 ID nguồn; 473 ID mới duy nhất, không rỗng, không trùng 14.500 ID cũ, Unicode NFC.
- 937 token mới và 65517 token tích lũy đúng nguyên chuỗi/thứ tự. Các vùng màu chứa tên item/skill (mã f7 03) giữ nguyên nội dung ở batch mới. Biến định dạng printf giữ nguyên.
- Kiểm chữ số và các chỉ số: 2 cảnh báo do `magic defence`/`defence` viết thường ở nguồn, đã giữ `Magic Defence`/`Defence`. Không phát hiện sai giá trị số trong audit.
- 17 nhãn English-only hoặc dòng chỉ chứa tên và chỉ số giữ nguyên, ghi riêng trong HOLD-NOT-COUNTED.csv.
- Chưa QA nghĩa theo mọi scene, độ rộng chữ, font, phân trang, runtime 3DS. Chưa có patch RomFS/CIA.

## Khôi phục
`cp011a-new.jsonl`: 473 mục. `merged-CP011a.jsonl`: 14.973 mục, giữ nguyên 14.500 dòng CP010. Ghép theo ID với 01_CAN_DICH.jsonl; không sửa trường nguồn. Nhánh `vh/fantasy-life-usa`.

SHA-256 gói mới: `4b0298b92a4a05dcaf9fab34bfc3cf00f78c9609cac1f0928e2d4d06144c8cc7`

SHA-256 bản gộp: `e407b947b136411745a4e253c868d3d2bd0208ab29d38277e4bb9b2691ba6987`

## Tiếp theo
0346–0347 (hướng dẫn), 0348#67–89 và #100 (phân loại tên skill/debug), 0349–0350 (phân loại, thoại cuối). Các gói đã bỏ qua và 0070–0071 HOLD vẫn chưa xử lý. Sổ ngôi xưng theo scene chưa xác minh; Gladstone dùng ta–ngươi, Napollon dùng tôi–bạn, người nói không rõ danh tính ưu tiên trung tính. Không tính các tên thuần English là bản dịch mới.