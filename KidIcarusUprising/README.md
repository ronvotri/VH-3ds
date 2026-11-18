# Kid Icarus: Uprising (USA) — Việt hóa

Nhánh riêng cho game 3DS này. Dữ liệu nguồn: `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` (18/11/2026).

- 4.067 mục EN (4.023 có chữ), 28 tập EN; nguồn hiện tại là text trích từ C-Stick/Gyro mod, **chưa xác nhận đủ toàn bộ game gốc**.
- `translations/batch_001.jsonl`: bản dịch overlay đầu tiên, dùng ID nguồn cố định, tuyệt đối không đánh lại index.
- `docs/STYLE_GUIDE.md`: nguyên tắc dịch, ngôi xưng nhân vật và QA.
- Nguồn đầy đủ dùng `ban_dich/tieng_anh_can_dich.jsonl` trong ZIP; overlay dịch cần ghép bằng `id` để giữ `raw_hex`, `controls_hex`, `labels`, `txt2_offset`.
- Không khẳng định đã có patch, font tiếng Việt, trình nhập lại MSBT hay test máy thật.

## Quy trình QA
1. Dịch theo ID; giữ tên nhân vật, tên riêng, Weapon/Power/item/thuật ngữ chính bằng tiếng Anh.
2. Không tự động dịch các ô rỗng, symbol hoặc ký tự điều khiển.
3. Kiểm tra vai nói của từng câu dựa vào ngữ cảnh, không đoán bằng thứ tự khi chưa xác thực.
4. Soát mã điều khiển, độ dài câu, tên thuật ngữ và ngôi xưng trước khi đóng gói.
5. Mỗi lần dịch thêm ghi đợt và số mục thực tế, không đánh dấu DONE khi chưa test trong game.
