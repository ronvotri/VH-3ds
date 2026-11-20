# Sơ đồ xưng hô — chờ mapping hội thoại thật

**Cảnh báo:** Bộ ZIP chưa có câu trích, speaker ID, NPC mapping. Không được bịa tên, quan hệ hoặc xưng hô cố định cho NPC.

| Nhóm tình huống | Người nói | Người nghe | Xưng hô tạm | Điều kiện chốt |
|---|---|---|---|---|
| Hướng dẫn hệ thống | system | người chơi | “bạn” / câu mệnh lệnh không chủ ngữ | Đối chiếu hộp thoại thật |
| NPC thân thiện ngang vai | unknown | unknown | “mình/bạn” hoặc “tớ/cậu” | Xác minh tuổi/vai trò, quan hệ và giọng gốc |
| NPC lớn tuổi/có vị thế | unknown | unknown | Chưa chốt | Xác minh nhân vật và ngữ cảnh |
| Đối thủ / phản diện | unknown | unknown | Chưa chốt | Xem sắc thái gốc và diễn tiến truyện |
| NPC dịch vụ | unknown | người chơi | lịch sự, trực tiếp | Kiểm chứng màn thao tác |

## Metadata bắt buộc cho mỗi câu thoại
- `string_id`, `source_path`, `source_en`, `speaker_id`, `speaker_display`, `addressee`, `scene`, `chapter`, `tone`, `vi`, `status`, `notes`.
- Speaker không biết: `unknown`. Nếu lời thoại đổi quan hệ qua chương, ghi thêm `relationship_phase`.
- Review liên câu liền trước/sau để nhất quán “tớ/cậu”, “mình/bạn”, “ta/ngươi”.

Đây là **khung xưng hô**, chưa phải hồ sơ nhân vật đã xác minh.
