# Resident Evil: The Mercenaries 3D — Việt hóa

Nguồn bàn giao: Translation_Handover.zip / MER_MSG_eng.gmd. Bản mod có Leon và Ada.

## Tiến độ

Đợt 001: 200 mục được biên dịch trong `translations/batch-001.csv` (ID,Vietnamese). Đây là bản dịch có dấu **chưa thể đóng gói chơi trực tiếp** vì font gốc chưa có đủ glyph tiếng Việt. Không ghi đè file gốc bằng GMD có dấu trước khi vá font và kiểm thử hiển thị.

Đợt 002: 200 mục tiếp theo trong `translations/batch-002.csv` — lưu game, menu, hành động, đòn cận chiến, vật phẩm, HUD và phần đầu hướng dẫn. Tổng cộng 400/1.039 mục đã được biên dịch; chưa kiểm thử hiển thị trong game.

## Quy tắc biên dịch
- Giữ tên riêng: Leon, Ada, Chris Redfield, Jill Valentine, Raccoon City, S.T.A.R.S., Uroboros.
- Thuật ngữ: shotgun, Magnum, combo, boss, solo được giữ khi tự nhiên; handgun = súng ngắn, machine gun = tiểu liên, flash grenade = lựu đạn choáng, melee = cận chiến.
- Giữ nguyên token `<ICON ...>`, `<COL ...>` và các token điều khiển; giữ `\\r\\n` đúng cấu trúc gốc.
- Không lạm dụng tiếng lóng Gen Z; ưu tiên thoại ngắn, đúng tính cách và quan hệ của nhân vật.
- Leon/Ada là mod thay slot Chris/Jill: chưa tự ý thay toàn bộ hồ sơ, tên nhân vật và thông số vì cần đối chiếu chính xác slot/costume.
- Cần kiểm tra tràn dòng theo độ rộng thực tế; giới hạn ký tự tiếng Anh chỉ là chỉ báo sơ bộ.

## Ghép bản dịch
Đối chiếu cột ID của `translations/batch-001.csv` để điền vào cột `Vietnamese` của `strings_to_translate.csv` trong ZIP bàn giao. Sau khi vá font, dùng `gmd_tool.py import` để xuất GMD, kiểm tra token và chạy thử trên 3DS.
