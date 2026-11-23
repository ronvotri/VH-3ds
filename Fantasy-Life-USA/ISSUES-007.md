# CP007 — vấn đề tồn đọng, cần xử lý trước phát hành

1. **200 ID gói 0070–0071** là bản đồ/debug nguồn bị dịch máy tệ, nhiều nhãn vô nghĩa như `rice impossible Dragon`. Có bản nháp riêng để kiểm nhưng **không ký duyệt**, không đưa vào bảng gộp.
2. **Nhãn UI/debug 0072–0074** có câu dịch thô từ Nhật; đã Việt hóa chức năng rõ nghĩa, nhưng phải xác nhận có được hiển thị hay chỉ là dữ liệu dev.
3. **Gói 0089** mới dịch 6/100 ID; không bỏ quên 94 câu sau ở CP008.
4. **Dynamic tokens `f6` ở 0084 câu 15–18**: đã giữ đúng thứ tự người hoàn thành và tên Challenge, cần test runtime.
5. **Giới tính, ngắt trang và màu**: token không hỏng nhưng có thể ghép đại từ/tràn chữ trên font 3DS; cần tester cả hai giới.
6. **Ngôi xưng**: dữ liệu nhiều `speaker=unknown`, chưa chốt quan hệ NPC.
7. **Chưa có patch font/glyph, RomFS/CIA, hoặc bản chạy test trên máy 3DS.**

**Nguyên tắc:** KHÔNG đưa file `HOLD-0070-0071-NOT-APPROVED.csv` vào bản patch hoặc coi là bản dịch đạt.
