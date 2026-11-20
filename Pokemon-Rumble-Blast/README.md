# Pokémon Rumble Blast (USA) — Việt hóa

Nguồn khảo sát: bộ tài liệu ngày 19/11/2026 do người dùng cung cấp. Product code: `CTR-P-ACCE`; Title ID: `0004000000066C00`.

## Tình trạng
- Đã tạo nhánh dự án riêng, không sửa nhánh `main` hoặc dự án Kid Icarus.
- ZIP bàn giao chỉ chứa tài liệu, mẫu và kiểm kê CIA: `bieu_mau/chuoi_dich.jsonl` có **0 bản ghi**.
- Chưa có RomFS/ExeFS đã giải mã, chưa trích câu gốc, chưa xác định parser/font, chưa có bản dịch trong game và chưa build patch.
- Không đưa nguyên CIA, keys hay ROM vào repo.

## Quy tắc khóa theo yêu cầu
1. Giữ nguyên tên Pokémon, item, skill/move, tên riêng và thuật ngữ chính bằng tiếng Anh. Chỉ dịch văn bản giải thích hoặc hướng dẫn xung quanh.
2. Việt hóa giao diện, thông báo, lời thoại bằng tiếng Việt có dấu NFC; hài hước Gen Z vừa đủ, trung thành tình huống.
3. Xưng hô dựa trên danh tính, vai trò, quan hệ và cảnh; chưa biết người nói thì để `unknown`, tuyệt đối không tự gán.
4. Giữ nguyên ID, placeholder, control code, ký hiệu nút, giá trị và biến động trạng thái.
5. Chỉ đánh dấu dịch/QA sau khi có chuỗi gốc có nguồn và kiểm tra kỹ thuật.

## Bước thực hiện tiếp theo
1. Nhận bản xuất RomFS/ExeFS hợp lệ, ghi hash và revision.
2. Kiểm kê định dạng, trích corpus JSONL giữ ID và ngữ cảnh.
3. Thử round-trip/import và font tiếng Việt trước khi dịch đại trà.
4. Dịch theo batch, đối chiếu glossary, QA tràn chữ/ngôi xưng và test game.

Xem `QUY-CHUAN-DICH.md` và `SO-DO-NHAN-VAT.md`.
