# Fantasy Life CP009a — những việc chưa giải quyết

1. **Gói 0114+** có nhiều tên Event/debug nguồn Anh dịch thô, có thể sai từ Nhật, phải xác minh nguồn Nhật/màn hình trước khi Việt hóa; không chế tên địa danh.
2. **200 ID 0070–0071 HOLD** do map/debug không rõ nghĩa, chưa nằm trong 10.945 ID được duyệt.
3. **Font/glyph Việt** chưa có patch chạy thử trên máy 3DS.
4. **Phân trang/độ rộng**: token đủ và đúng thứ tự nhưng vị trí ngắt câu Việt là sơ bộ, chưa đo pixel width.
5. **21 nhánh giới tính mới**: giữ token và dịch hai nhánh, chưa thử cả hai giới trong game.
6. **EN_A/EN_B**: giữ khác biệt gốc; chưa xác nhận bản nào được dùng tại runtime của ROM USA.
7. **CP009 còn 1.555/2.000 ID** theo mục tiêu, cần tiếp các phần rõ nghĩa thay vì lấp bằng debug.
8. **QA ngữ nghĩa độc lập** cần tester xác minh scene và speaker/target.
9. **0113#14** có token kết thúc màu kép trong nguồn quanh số 3, đã giữ nguyên để bảo đảm cấu trúc; cần test màu trên máy.

**Chưa có patch RomFS/CIA chơi được.**
