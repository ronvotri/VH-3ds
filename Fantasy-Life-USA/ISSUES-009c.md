# CP009 — Những điểm cần kiểm tiếp

1. Gói 0070–0071 có 200 ID map/debug từ nguồn Nhật bị dịch thô, **HOLD** chưa duyệt.
2. Gói 0114–0123 và 0131#64–100 có Event/debug mơ hồ, không tự chế nghĩa.
3. Hai ID chỉ có tên riêng `Philosopher's Stone` và `Levitanian Sardine` được giữ English nguyên trạng, không tính vào số dịch mới.
4. Một ID cũ từ CP007, `FL-USA::F00008710@0001faca`, chứa `<color name="green"/>Orbe de especialidad<color/>`, vẫn chưa có tên item đúng; giữ nguyên trong bảng tương thích, **không coi là Việt hóa**.
5. Có 1 tiêu đề tiếng Việt dài 40 ký tự ở 0142#14, dù nguồn cũng dài; cần kiểm pixel width và xuống dòng.
6. EN_A/EN_B có tên khác nhau; cần kiểm nhánh thực sự được sử dụng trong ROM USA.
7. Chưa có font tiếng Việt/patch RomFS/CIA chạy thực tế; tiến độ 35,91% là ID đã xử lý, không phải độ phủ văn bản của game sau patch.
8. Tiếp gói 0147#33, sau đó 0148+, và quay lại HOLD khi có nguồn Nhật/screenshot.
