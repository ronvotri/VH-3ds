# Resident Evil: The Mercenaries 3D — Việt hóa

Nguồn bàn giao: Translation_Handover.zip / MER_MSG_eng.gmd. Bản mod có Leon và Ada.

## Tiến độ

Đợt 001: 200 mục được biên dịch trong `translations/batch-001.csv` (ID,Vietnamese). Đây là bản dịch có dấu **chưa thể đóng gói chơi trực tiếp** vì font gốc chưa có đủ glyph tiếng Việt. Không ghi đè file gốc bằng GMD có dấu trước khi vá font và kiểm thử hiển thị.

Đợt 002: 200 mục tiếp theo trong `translations/batch-002.csv` — lưu game, menu, hành động, đòn cận chiến, vật phẩm, HUD và phần đầu hướng dẫn. Tổng cộng 400/1.039 mục đã được biên dịch; chưa kiểm thử hiển thị trong game.

Đợt 003: thêm 200 mục (ID 581–780) trong `translations/batch-003.csv`: hướng dẫn chiến đấu, kỹ năng, nâng cấp cấp 3, mở khóa và chơi đôi. Tổng 600/1.039 mục đã biên dịch (57,7%); chưa kiểm thử hiển thị trong game.



Đợt 004: thêm 200 mục (ID 781–980) trong `translations/batch-004.csv` — Wi-Fi/chơi đôi, thiết lập điều khiển, âm thanh, xếp hạng và 41 huy chương. Tổng cộng 800/1.039 mục đã biên dịch (77,0%); chưa kiểm thử trên 3DS.

## Checkpoint 005 — Hoàn tất biên dịch nguồn CSV

- **1.039 / 1.039 ID** đánh dấu `Translate? = YES` đã có giá trị tương ứng, phân bổ trong 6 batch và bảng hợp nhất `translations/merged-001-005.csv`. Các tên riêng, ký hiệu điều khiển, số và tên diễn viên lồng tiếng được giữ nguyên khi phù hợp; không có nghĩa là mọi ID đều thay đổi chữ.
- Đợt 005a bổ sung 125 ID còn thiếu ở phần đầu (nhân vật, dữ liệu nhân vật, huy chương, ký hiệu).
- Đợt 005b bổ sung 114 ID ở phần cuối (điều kiện huy chương, nội dung đặc biệt, credits).
- Đã sửa 11 mục thiếu dấu `\\r\\n` của batch 002–003. Đã kiểm tra toàn bộ 1.039 ID trong sáu batch không trùng nhau.
- **Chưa thể xem là hoàn thiện bản vá**: chưa ghép CSV vào GMD và xác nhận round-trip, chưa vá font tiếng Việt, chưa kiểm tra độ rộng chữ trên máy 3DS. Bản CSV UTF-8 có dấu hiện phục vụ biên dịch và rà soát, không chép thẳng vào máy.
- Để dùng trình nhập `gmd_tool.py` trong gói bàn giao, cần đối chiếu theo ID và điền vào cột `Vietnamese` của `strings_to_translate.csv` trước khi import. Không sử dụng bảng hai cột trực tiếp thay cho CSV nguồn tám cột.

## Quy tắc biên dịch
- Giữ tên riêng: Leon, Ada, Chris Redfield, Jill Valentine, Raccoon City, S.T.A.R.S., Uroboros.
- Thuật ngữ: shotgun, Magnum, combo, boss, solo được giữ khi tự nhiên; handgun = súng ngắn, machine gun = tiểu liên, flash grenade = lựu đạn choáng, melee = cận chiến.
- Giữ nguyên token `<ICON ...>`, `<COL ...>` và các token điều khiển; giữ `\\r\\n` đúng cấu trúc gốc.
- Không lạm dụng tiếng lóng Gen Z; ưu tiên thoại ngắn, đúng tính cách và quan hệ của nhân vật.
- Leon/Ada là mod thay slot Chris/Jill: chưa tự ý thay toàn bộ hồ sơ, tên nhân vật và thông số vì cần đối chiếu chính xác slot/costume.
- Cần kiểm tra tràn dòng theo độ rộng thực tế; giới hạn ký tự tiếng Anh chỉ là chỉ báo sơ bộ.

## Ghép bản dịch
Đối chiếu cột ID của `translations/batch-001.csv` để điền vào cột `Vietnamese` của `strings_to_translate.csv` trong ZIP bàn giao. Sau khi vá font, dùng `gmd_tool.py import` để xuất GMD, kiểm tra token và chạy thử trên 3DS.
