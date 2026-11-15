# Resident Evil 4 — Zeebo → Nintendo 3DS Việt hóa

**Dự án đang triển khai đúng:** [KiddRwxSsj/biohazard4ze-3ds](https://github.com/KiddRwxSsj/biohazard4ze-3ds). Không phải Resident Evil: The Mercenaries 3D.

## Nguồn game và cấu trúc
- Repo port 3DS: `KiddRwxSsj/biohazard4ze-3ds`.
- File tiếng Anh: `re/lang/en.txt` (~87 KB). Định dạng: `@archive:entry:offset` trên một dòng, ngay sau là câu dịch; `|` nghĩa là xuống dòng; `{1}`…`{4}`, `{H}` là ký hiệu nút bấm. Phải giữ khóa/marker.
- Chữ được thay thế khi tải từ `common.h2z`, `3d_base.h2z` bằng hook của port, **không dùng GMD**.
- Bản English hiện có vốn được dịch từ nguồn tiếng Bồ Đào Nha và tác giả lưu ý có hỗ trợ AI. Cần đối chiếu ngữ cảnh RE4, không mặc định câu nào cũng chuẩn.
- GMD `MER_MSG_eng.gmd` cùng các batch-001…005 và `merged-001-005.csv` thuộc **The Mercenaries 3D** và không được dùng làm nguồn cho bản RE4. Đã tách dự án bằng thư mục này; chưa xóa dữ liệu cũ.

## Phong cách Việt hóa
- Ngắn gọn, dễ đọc trên màn hình 3DS. Gen Z nhẹ, tự nhiên; không nhồi meme vào thoại căng thẳng.
- Leon với Ashley: anh–em khi phù hợp; Leon với Ada: tôi–cô hoặc anh–em tùy cảnh, đối chiếu thoại để không tự ý thân mật hóa; Leon với Luis: tôi–anh / anh bạn khi phù hợp. Villain dùng giọng đe dọa, không cợt nhả thiếu ngữ cảnh.
- Giữ tên nhân vật và những tên riêng quan trọng. Thuật ngữ dự kiến: Handgun = Súng ngắn, Shotgun = Shotgun hoặc Súng săn (chốt một cách theo UI), Magnum = Magnum, Green Herb = Thảo dược xanh, Pesetas = Pesetas, Merchant = Thương nhân, Ganado = Ganado, Plaga = Plaga.

## Mục tiêu kỹ thuật
1. Lập danh mục toàn bộ khóa trong `re/lang/en.txt`, kiểm tra không trùng, không mất khóa.
2. Tạo `re/lang/vi.txt` cùng cấu trúc; dịch và rà ngữ cảnh từng nhóm.
3. Kiểm tra giới hạn ô chữ với `re/lang.py check` trên bộ file game hợp lệ của người dùng.
4. Kiểm thử dấu tiếng Việt và glyph của renderer 3DS; sửa hệ thống render nếu cần.
5. Build CIA từ mã nguồn port và thử trên máy hoặc giả lập.

**Tình trạng:** Đã dịch đợt 001 gồm **100/1.170 khóa** nguồn ở `RE4-3DS/lang/vi-batch-001.txt` (8,5%). Đã giữ khóa `@archive:entry:offset` và ký hiệu ngắt dòng `|`, chỉnh gọn một số nhãn túi đồ. **Chưa build CIA, chưa kiểm tra glyph Việt và giới hạn trên tài nguyên Zeebo thực tế.** Không tính 1.039 mục Mercenaries vào tiến độ RE4.

**Chú ý công cụ:** `re/lang.py encode` hiện chỉ hỗ trợ ASCII và một số glyph tiếng Bồ Đào Nha; sẽ báo `no glyph` với dấu tiếng Việt. Không ghi đè `re/lang/en.txt` hoặc build trực tiếp trước khi mở rộng font và mã hóa glyph.
