# Fantasy Life CP010b — QA còn mở

1. **Font tiếng Việt 3DS**: chưa vá hoặc thử glyph, đo pixel width, giãn dòng trong hộp menu.
2. **Menu chọn màu** (`0182#53/54/79`): các mã lựa chọn Có/Không và 13/8/9 token nguyên vẹn; phải xem bản chạy thật để xác nhận tiêu đề màu và lựa chọn không dính nhau.
3. **Chuỗi biến động** (`0185` Warp/Follow, `0186` Learned/Obtained, `0187` Quest/Ally): bảo toàn chính xác mã f6/f0/ffff nhưng chưa kiểm đối chiếu với tên thực tế tại runtime.
4. **StreetPass, Link Mode, Ally Mode, Multiplayer**: có giao diện đã dịch, chưa thử tính năng online hoặc chia sẻ trên máy.
5. **Độ rộng, tên và mạo từ**: vài câu có thứ tự động như `Holiday Home` hoặc level craft có thể cần chỉnh sau khi xem ảnh game; chưa tuyên bố hoàn hảo về ngữ nghĩa trong mọi biến.
6. **57 ID mới giữ English**: thuật ngữ, nhãn rỗng, `SLOT`, chữ `x`, URL kỹ thuật; có trong HOLD, chưa tính dịch.
7. **200 ID map/debug từ 0070–0071**, chuỗi mơ hồ 0114–0123 và 0131#64–100 tiếp tục HOLD, không dịch đoán.
8. **Tên item tiếng Tây Ban Nha cũ `Orbe de especialidad`** vẫn cần xác minh; không tự đặt tên.
9. **CP010 còn 835 ID** để đạt chỉ tiêu 2.000. Có thể xét tiếp UI 0189, nhưng nhóm 0190+ chủ yếu tên item nên không tự tính.
10. **Chưa có patch RomFS/CIA chơi được**. 39,25% chỉ nói đến ID nguồn đã xử lý; không phải ROM.