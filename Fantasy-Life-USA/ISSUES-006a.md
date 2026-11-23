# Fantasy Life — CP006a: Vấn đề còn mở

1. **Font Việt:** chưa có patch glyph/texture/mapping có thể xác nhận vận hành trên 3DS.
2. **Phân trang và độ rộng:** token `f0`/`ffff` được giữ nguyên nội dung và thứ tự nhưng đặt tương đối theo câu Việt; phải đo theo font thật, xem từng hộp thoại.
3. **Ngôi xưng:** nguồn `speaker=unknown` ở nhiều câu; bảng thoại theo nhân vật cần kiểm với scene gốc trước khi khóa.
4. **Biến thể EN_A/EN_B:** giữ riêng tên item và vùng khác nhau, chưa xác minh bản game USA đang kích hoạt nhánh nào ở runtime.
5. **QA số:** cảnh báo đếm số thô sau token; rà soát bổ sung không thấy mất giá trị số nào, nhưng vẫn phải kiểm ngữ nghĩa các phần thưởng và điều kiện nhiệm vụ.
6. **Tên item:** 250 đoạn bọc màu được kiểm so khớp sau chuẩn hóa khoảng trắng; tên xuất hiện ngoài marker cần đối chiếu thêm ở QA tổng.
7. **Build:** chưa có patch RomFS/CIA; CP006a chỉ là dữ liệu dịch nguồn.

**Tiếp gói 0051; còn 1.500 câu để đạt mục tiêu CP006.**
