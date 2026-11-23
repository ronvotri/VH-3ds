# Fantasy Life CP006 — những việc cần QA tiếp

1. **Font/glyph tiếng Việt:** chưa có bản vá glyph nào được thử thành công trên 3DS.
2. **Độ rộng/ngắt trang:** token đã bảo toàn nội dung và thứ tự, nhưng có thể tràn hoặc ngắt câu xấu theo khung thực tế.
3. **Nhánh nam/nữ:** cần kiểm trên máy bằng nhân vật cả hai giới, nhất là cách ghép đại từ quanh token.
4. **Người nói và quan hệ NPC:** còn nhiều `speaker=unknown`, sổ ngôi xưng chỉ theo từng cụm hội thoại.
5. **EN_A/EN_B:** tiếp tục giữ riêng, không tự hợp nhất tên Furlin/Fluffkin và cặp item Super/Superior.
6. **Font/ROM:** chưa build patch RomFS/CIA và chưa kiểm khả năng chạy thật.
7. **Tiếp tục dịch:** gói `0066`, bắt đầu từ ID thứ 6.501.

Bản dịch nguồn đã QA tĩnh 6.500 mục không đồng nghĩa 18,67% nội dung đã chạy được trong ROM.
