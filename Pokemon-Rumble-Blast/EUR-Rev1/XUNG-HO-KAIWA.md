# Khung xưng hô `kaiwa` — dựa trên nội dung nguồn, chưa test NPC

`TALK_*_SPEAK*` trong bộ giao chỉ là nhãn thoại/cảnh, không phải tên người nói. Mọi mapping nhân vật đều cần ảnh cảnh tương ứng để nâng mức chắc chắn.

| Nhóm ngữ cảnh / ID điển hình | Giọng VI đã dùng | Mức xác nhận |
|---|---|---|
| Chào mừng ở Toy Town, hướng dẫn Meadow/Forest (`#00000–#00003`, `#00008–#00026`) | `mình/bạn`, `tôi/bạn`, `bọn mình` tùy lời nói | Đã nhận diện chức năng thoại; chưa xác minh NPC |
| Pawniard xưng tên trực tiếp `#00004`; nhóm khiêu khích `#00007`, `#00027–#00028`, `#00036–#00037`, `#00047–#00049` | `ta/ngươi`, giọng ngông nghênh, châm chọc vừa phải | `#00004` xác nhận Pawniard tự giới thiệu; nhóm còn lại suy theo cảnh, chờ test |
| Hội thoại hỏi Pawniard về Glowdrops `#00053–#00060` | Người chất vấn `cậu`, bên phản bác `bọn ta` | Quan hệ chưa xác minh |
| Người hướng dẫn Team Battle và Great Glowing Fountain `#00069–#00085` | `tôi/bạn`, lịch sự, có khí chất hiệp sĩ ở lời xuất quân | Chưa xác minh NPC |
| Thị trấn Westerly, lời trinh sát và quân Cobalion `#00086–#00114` | `tôi/bạn`, hơi lúng túng khi che giấu `ngài Cobalion` | Chưa xác minh danh tính người nói |
| Northerly Town, Temple of Keys và Path of Heroes `#00115–#00130` | `tôi/bạn`, riêng lời thách thức mang sắc thái gắt | Chưa xác minh NPC |
| Kể về Dark Rust và công lý `#00131–#00151` | `tôi/bạn`, nghiêm túc, hối lỗi khi phù hợp | Speaker ID chưa xác minh |
| Hậu truyện World Axle và Glowdrop Vial `#00152–#00161` | `tôi/bạn`, thông báo trực tiếp, thân thiện | Chưa xác minh NPC |

**Quy tắc rà sau:** khi có ảnh UI hoặc scene dump có speaker, kiểm cặp đối thoại liền trước/sau, tuyệt đối không ép đại từ theo loài hoặc tuổi tưởng tượng. Nếu quan hệ thay đổi theo cốt truyện thì ghi một giai đoạn quan hệ riêng thay vì sửa đồng loạt các câu cũ.
