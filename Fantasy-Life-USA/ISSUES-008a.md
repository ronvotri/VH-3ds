# Fantasy Life CP008a — vấn đề còn mở

1. **CP008 chưa hoàn tất:** 1.610/2.000 ID; còn **390**. Gói kế tiếp `0105` #17; từ giữa gói có thoại NPC dài cần kiểm nguyên cụm, không chuyển thành lời UI bằng suy diễn.
2. **200 ID 0070–0071 HOLD:** tên địa điểm Nhật bị phiên âm và bản Anh debug/định vị lỗi. Chưa có nguồn Nhật hoặc screenshot để xác minh; không được tự chế tên mới.
3. **QA cấu trúc không đồng nghĩa QA ngữ nghĩa:** các challenge được dịch theo mẫu và rà sửa, nhưng QA mọi câu tại scene vẫn cần người kiểm.
4. **Ngôi xưng:** `speaker=unknown`; không tự gán tuổi, quan hệ, giới tính trong NPC quests.
5. **Token & UI:** đã bảo toàn `{CTRL:hex}`; cần kiểm ngắt trang, icon nút bấm, các biến tên/nhiệm vụ động khi có bản chạy.
6. **Font/ROM:** chưa có patch glyph tiếng Việt, chưa đo độ rộng/đóng gói RomFS/CIA. Tiến độ chỉ tính **34.812 ID bộ bàn giao**.
7. **Tên item/skill:** giữ riêng EN_A và EN_B; đừng tự gộp nếu có khác biệt. Cần xác định biến thể runtime của phiên bản USA.
