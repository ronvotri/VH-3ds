# Fantasy Life (USA) — Việt hóa Votri Valley — CP010 hoàn tất

**24/11/2026 — 14.500 / 34.812 ID đã xử lý (41.65%)**. Còn 20.312 ID chưa xử lý; 1 ID cũ tiếng Tây Ban Nha giữ nguyên chờ xác minh, nên 14.499 ID có nội dung Việt hóa khác nguồn.

CP010a 522 + CP010b 643 + CP010c 835 = **2.000 ID**. Nhánh `vh/fantasy-life-usa`, không sửa `main`.

## CP010c: phạm vi

| Gói | ID mới | Nội dung |
|---|---:|---|
| 0189#1–12 | 12 | Đổi thưởng Goddess Statue, chọn loại xu |
| 0217 | 100 | Mô tả nội thất, nguyên liệu, thuốc |
| 0218 | 100 | Mô tả nguyên liệu, đá quý, gỗ, vật phẩm |
| 0219 | 93 | Mô tả nguyên liệu, biến thể EN_B |
| 0220 | 95 | Nguyên liệu và tiêu đề hướng dẫn |
| 0221 | 95 | Hướng dẫn các Life, câu cá, chế tạo |
| 0222 | 95 | Hướng dẫn chiến đấu, Creator Mode, License |
| 0223 | 49 | God Mode, mô tả Special Skill |
| 0340 | 100 | Giáp, Charm, thuốc, món ăn |
| 0341#1–96 | 96 | Mô tả món ăn và chỉ số |
| **Tổng** | **835** | **701 EN_A / 134 EN_B** |

73 ID đã xem xét nhưng chỉ là tên riêng/skill/nhãn được bảo vệ được giữ riêng trong `HOLD-NOT-COUNTED.csv`, không cộng vào tiến độ. Các gói chưa khảo sát hoặc được nhảy qua vẫn chưa duyệt; tiếp theo ưu tiên 0341#97–100, 0342–0347 và các hội thoại rõ nghĩa 0330–0336, 0351. Không quên 0070–0071 và các mục debug cũ đang HOLD.

## Quy tắc
Giữ English cho tên riêng, NPC, item, skill, Life, Rank, License, Creator/God Mode, HP/SP, Strength, Vitality, Dexterity, Focus, Luck, Intelligence. Mô tả nguyên liệu dùng danh từ Việt khi nguồn dùng danh từ thường, không đổi định danh item chính thức. Tiêu đề hướng dẫn dịch gọn, không tự thêm thao tác. Thông báo hồi HP/SP và cải tiến công thức giữ nguyên mức độ, chỉ số, mục tiêu, thời gian tác dụng. Không gán lời NPC cho văn bản hướng dẫn.

## QA tĩnh
- 835 ID mới đúng nguồn, không trùng, không rỗng; 943 token mới bảo toàn nội dung và thứ tự. Bản gộp giữ 64.580 token.
- Kiểm chữ số và tên chỉ số HP/SP/Strength/Vitality/Dexterity/Focus/Luck/Intelligence: 0 sai khác sau tách token.
- Các nguồn giống hệt trong batch mới có bản Việt nhất quán; Unicode NFC đạt. Giữ nguyên tiền tố 13.665 ID CP010b.
- Chưa kiểm tra độc lập từng câu trong cảnh game, font glyph, độ rộng pixel, ngắt trang, icon và các tên gọi trong runtime. Chưa có patch RomFS/CIA chơi được.

## Tệp khôi phục
`cp010c-new.jsonl` — 835 ID; `cp010-complete-2000.jsonl` — 2.000 ID CP010; `merged-CP010c.jsonl` — 14.500 ID. Chạy `python3 unpack_batches.py` ở repo khi script đã được cập nhật. Ghép theo ID vào `01_CAN_DICH.jsonl` trong ZIP nguồn, không ghi đè source/raw_hex/references/alias_ids/length_bindings.

SHA-256 CP010c: `bfd755404c2556b97267ca1de9414fae7f20f59c364a67f42a540aed485d0f0c`

SHA-256 CP010: `cbbf89fd83d26cb8ebc7ca4755fabe65cd56462a2debd7a3c95d86d8a8ab8585`

SHA-256 bản gộp: `0da060b95836903301b85ca3b961351e260b295eed8125462035b294f6204b66`