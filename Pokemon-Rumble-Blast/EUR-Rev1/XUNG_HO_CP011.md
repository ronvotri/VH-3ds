# Hệ thống ngôi xưng & giọng thoại — CP011 (bản hướng dẫn biên tập)

**Không suy ra speaker từ số `SPEAK000`, `SPEAK010`...** Đây là thứ tự lượt thoại trong một cảnh, không phải ID nhân vật xuyên game. Chỉ chốt từ tên nhân vật tự xưng, diễn tiến cảnh hoặc xác minh trong game.

| Nhóm | Ngôi xưng định hướng | Ngữ khí | Chứng cứ / cần xác minh |
|---|---|---|---|
| Pawniard, khi đối đầu | `ta/ngươi`, `bọn ta/ngươi` | Khịa, tự tin, hơi xấc nhưng vui | `kaiwa #00004` tự xưng tên. Đặc biệt `NoticeDesc #00123` là lời đối thủ bị hạ trước chung kết, phù hợp Pawniard, cần đối chiếu ảnh để chốt nhận diện |
| Pawniard khi công nhận người chơi | Vẫn `ta/ngươi`, nhẹ gắt hơn | Nể đối thủ nhưng giữ sĩ diện | `kaiwa #00049` |
| Cobalion lúc đối đầu | `ta/ngươi` | Kiên quyết, trịnh trọng, theo đuổi công lý | `makuai #00018–#00024`, `#00032–#00041` |
| Cobalion khi hiểu ra và cùng chiến đấu | `tôi/bạn` hoặc câu không chủ ngữ | Hối lỗi, chân thành, vẫn nghiêm túc | `makuai #00080–#00084`, `#00099–#00110` — mapping nhân vật cần đối chiếu cảnh |
| Dark Rust | `ta/ngươi`, `các ngươi` | Lạnh lùng, ác ý, không dùng meme | `makuai #00067–#00074`, `#00087–#00114` |
| Địch trong StageDesc | `ta/ngươi`, `bọn ta/ngươi` | Khiêu khích, cay cú khi thua | Nhóm `StageDesc` có văn bản thách đấu, danh tính cụ thể cần ảnh/scene |
| NPC thị trấn / trông coi cơ sở | `tôi/bạn` hoặc `mình/bạn` tùy nhân vật | Thân thiện, súc tích | Không ép thống nhất các NPC khác nhau, nhưng cùng một đoạn hội thoại phải nhất quán |
| Hướng dẫn hệ thống / menu | `bạn` / không đại từ | Rõ nghĩa, tránh pha trò khi hậu quả mất dữ liệu | `main`, `NoticeDesc` hướng dẫn |
| Mô tả Move/Special Trait | không xưng hô trực tiếp | Ngắn, chính xác, thuật ngữ ổn định | `WazaDesc`, `prefix` |

## Quy tắc hài hước

- Cà khịa được khi gốc đã có chất trêu chọc: “đống sắt vụn”, “lượn đây”, “đỉnh của cành”.
- Không dùng slang lạc giọng cho Dark Rust, Cobalion trong các cảnh nghiêm trọng.
- Giữ tiếng Anh tên Pokémon, Move/Skill, item, địa danh/chế độ, thuật ngữ chính theo yêu cầu dự án.
- Không đưa câu đùa vào xác nhận thả Pokémon, đổi chiêu, xóa save hoặc cảnh liên quan hậu quả gameplay.
- Nếu chưa xác minh ai nói thì đánh dấu `speaker=unknown`, tuyệt đối không tự tạo quan hệ/tuổi/tước vị.

## Trạng thái

Bộ nguồn không chứa speaker mapping chính thức đủ để chốt toàn bộ NPC. Đây là **hướng dẫn ngôi xưng có bằng chứng**, không phải xác nhận 100% nhân vật qua gameplay.