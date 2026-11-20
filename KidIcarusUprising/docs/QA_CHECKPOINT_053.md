# Kid Icarus: Uprising — QA Checkpoint 053

## Phạm vi

Rà chọn mẫu hội thoại `a1500.zrc`–`a1700.zrc` (Chương 15–17), đặc biệt các đoạn Pyrrhon / Palutena / Pit và các phép ví von. Đối chiếu tiếng Anh đúng ID trực tiếp từ ZIP bàn giao `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`. Các batch gốc `031` và `032` chỉ chứa `vi`, nên cần lấy `source` từ ZIP khi QA.

## Hai điều chỉnh

| Nguồn ID | Tiếng Anh gốc | Trước QA | Sau QA | Giải thích |
| --- | --- | --- | --- | --- |
| `a1600.zrc#00018` | And if their smaller troops are drones, their ships are killer bees. | Nếu lính nhỏ là ong thợ, thì chiến hạm là ong sát thủ. | Nếu lính nhỏ là ong đực, thì chiến hạm là ong sát thủ. | Trong phép ví quân Aurum với đàn ong, `drone` là ong đực, không phải ong thợ. |
| `a1700.zrc#00024` | Do your thing, Pit. You know, your... shooting thing. | Triển đi Pit! Cái trò... bắn bắn của cậu ấy. | Trổ tài đi, Pit! Ấy, cái trò... bắn bắn của cậu đó! | Câu gốc đang trực tiếp gọi Pit; `cậu ấy` khiến câu Việt như đang nói về người thứ ba. |

## QA sau commit

- Cập nhật trực tiếp `translations/batch_031.jsonl` và `translations/batch_032.jsonl`, không phát sinh ID.
- Đã tải lại hai file từ nhánh `vh/kid-icarus-uprising`; **2/2 câu có nội dung đã sửa**.
- Giữ đúng số bản ghi: `batch_031` **76 ID duy nhất**, `batch_032` **82 ID duy nhất**.
- Số ID đã xử lý theo kiểm kê trước giữ nguyên **3.235 / 4.023 (80,4%)**.

## Chưa xác nhận

Chưa có QA đầy đủ tất cả người nói trong game, chưa kiểm thử font, độ dài dòng, mã điều khiển khi patch ROM, hoặc thử trên Nintendo 3DS. Giữ trạng thái `draft`.
