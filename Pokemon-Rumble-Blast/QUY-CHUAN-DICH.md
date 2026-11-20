# Quy chuẩn dịch — Pokémon Rumble Blast

## Giữ nguyên EN
Tên loài/form Pokémon; tên item; Move/Skill; tên riêng; tên địa danh và tên chế độ/thuật ngữ chính (ví dụ: Toy Town, World Axle, Battle Royale, StreetPass, Play Coins, Wonder Key, Glowdrops, Dark Rust) **cho tới khi đối chiếu đúng source và thống nhất ngoại lệ**.

Khi cần giải thích, dùng tiếng Việt xung quanh nhưng không tự thay tên gốc: `Chọn Move muốn dùng.`, `Đã nhận Wonder Key!` (các câu chỉ minh họa phong cách, **không phải câu trích từ ROM**).

## Giao diện thông dụng (bảng nháp, chưa trích từ ROM)
| EN | VI dự kiến |
|---|---|
| New Game | Chơi mới |
| Continue | Tiếp tục |
| Save and Quit | Lưu và thoát |
| Saving | Đang lưu... |
| Settings | Cài đặt |
| Back | Trở lại |
| Cancel | Hủy |
| Confirm | Xác nhận |
| Yes / No | Có / Không |
| Retry | Thử lại |
| Victory | Chiến thắng |
| Game Over | Thất bại |
| Filter | Lọc |
| Sort | Sắp xếp |
| Favorites | Yêu thích |
| Pokémon Info | Thông tin Pokémon |
| Befriend | Kết bạn |
| Release | Thả Pokémon |
| HP | HP |
| Power | Sức mạnh |
| Type | Hệ |
| Move | Move (giữ thuật ngữ) |
| Special Trait | Special Trait (giữ thuật ngữ) |

Bảng này là từ vựng để mapping khi có corpus; không tính là đã dịch câu game.

## Ngữ khí
- Tutorial: dễ hiểu, ngắn, thân thiện, có thể dùng “bạn”.
- NPC vui tính: dí dỏm theo ngữ cảnh, không nhồi meme mọi câu.
- NPC nghiêm túc/đối địch: giữ sự nghiêm túc hoặc sức ép của cảnh.
- Thông báo xác nhận mất Pokémon, đổi Move, item: ưu tiên rõ hậu quả, không pha trò gây hiểu nhầm.

## QA
- Unicode NFC, giữ placeholder, tên riêng, số, biểu tượng, mã điều khiển.
- Không nhận giới hạn ký tự cố định khi chưa đo UI thật.
- Trạng thái `chua_dich → ban_nhap → da_bien_tap → da_kiem_tra_ky_thuat → da_test_game → da_duyet`.
