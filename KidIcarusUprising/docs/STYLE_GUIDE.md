# Quy chuẩn dịch & bảng ngôi xưng — Kid Icarus: Uprising

## Luật chung
- Giữ nguyên: Pit, Palutena, Viridi, Hades, Dark Pit; tên địa điểm, chủng loài, vũ khí, item, Power/skill và thuật ngữ chính thức của game (ví dụ Circle Pad, Touch Screen, L Button, Play Coin, hearts như đơn vị tiền, Weapon Gem, Solo, Idol, Intensity, Ranged, Melee).
- Việt hóa: hướng dẫn, lời thoại, cảnh báo, menu phổ thông. Văn nói Gen Z hài hước nhưng không nhét meme làm sai cá tính hoặc phá sắc thái nghiêm túc.
- Ngắn gọn vừa màn hình 3DS; giữ xuống dòng có ý nghĩa, không tự ý bỏ placeholder hay mã điều khiển.
- Chỉ dịch từ EN nguyên bản; FR/ES tham khảo khi cần.

## Ngôi xưng (khung khởi tạo, rà theo từng cảnh)
| Nhân vật | Xưng | Gọi đối phương | Tính cách và ngoại lệ |
|---|---|---|---|
| Pit | mình / tôi | Lady Palutena: nữ thần / ngài; Viridi: cô; Hades: ngươi hoặc ông tùy cảnh | Nhiệt tình, ngây thơ đáng yêu, thỉnh thoảng đáp trả lém lỉnh; hạn chế 'tao/mày' |
| Palutena | ta | Pit: em hoặc Pit; Viridi: cô | Thần thái điềm tĩnh, trêu Pit nhẹ; khi chỉ dẫn dùng ngữ khí rõ ràng, gần gũi |
| Viridi | ta | Pit: cậu / nhóc; Palutena: Palutena | Đanh đá, tự tin, hay cà khịa; không biến thành chửi tục |
| Hades | ta | Pit: nhóc / cậu bé / ngươi theo cảnh | Kịch tính, thích chơi chữ và chế giễu |
| Dark Pit | tôi / ta tùy cảnh | Pit: cậu / ngươi tùy quan hệ | Bất cần, sắc cạnh, không đồng hóa với Pit |

**Lưu ý:** Đây là bảng gợi ý chuẩn bị dịch, chưa được kiểm chứng toàn bộ hội thoại. Mỗi câu không có trường speaker trong JSONL phải kiểm tra diễn biến hoặc media gốc trước khi chốt xưng hô.

## Quy tắc dữ liệu
- Một dòng JSONL gồm `id`, `source`, `vi`, `status`; overlay không được thay metadata gốc.
- `status=draft`: dịch bước đầu, chờ QA ngữ cảnh; `reviewed`: đã kiểm tra ngữ cảnh; `verified_ingame`: đã kiểm chứng trực tiếp game.
- Đối chiếu trên tập đủ 4.067 mục EN, gồm 44 mục rỗng; không tự động đếm dòng rỗng là câu dịch.
- Không ghi ROM/CIA vào repo.
