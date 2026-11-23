# Fantasy Life — sổ ngôi xưng / văn phong CP008a

Nguồn CP008a chủ yếu là các câu Challenge/Quest/UI, không có mapping người nói chắc chắn. Vì vậy:

- **Challenge / nhiệm vụ theo nghề:** mệnh lệnh trung tính “Hạ…”, “Câu…”, “Rèn…”, “Chế tạo…”, “Nấu…”, “Thu thập…”, “Nâng skill…”. Không tự thêm NPC nói chuyện. Các Rank, Life, item, skill và label Challenge giữ nguyên Anh.
- **License, Story, Friendship, Bliss, Quest/UI:** dùng “bạn” hoặc lược đại từ. Tránh đùa trong hướng dẫn dữ liệu hoặc cảnh báo hệ thống.
- **Quest/Event debug/test:** mô tả chức năng thực, giữ ID, không tạo lời nhân vật giả.
- **EN_A/EN_B:** mỗi bản nguồn riêng theo ID, bảo toàn các cặp khác tên (vật phẩm/skill). Không sửa khác biệt chỉ vì nghĩ một tên phổ biến hơn.
- **Cần kiểm tiếp:** từ `0105` #17 trở đi có thoại NPC nhiều nhân vật. Chỉ chốt “thầy/cô – trò”, “anh – em”, “bà – cháu” sau khi biết speaker, target và hoàn cảnh scene.

Khi có gameplay tester, bổ sung `speaker → người nghe → vai vế → xưng/hô → ví dụ → độ tin cậy`.
