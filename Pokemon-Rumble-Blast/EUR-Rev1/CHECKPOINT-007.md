# Super Pokémon Rumble — Bàn giao Checkpoint 007 🇻🇳

**Nguồn:** Super Pokémon Rumble EUR Rev 1, Title ID `0004000000066D00` (`EU_English`). **Không dùng cho ROM USA** `0004000000066C00`.

## Tiến độ

- Dịch mới: **200 mục phân loại translate** (126 `main.msbt` + 74 `NoticeDesc.msbt`).
- Tích lũy: **958/1.932 (49,59%)**, còn **974**.
- `kaiwa.msbt`: 158/158.
- `main.msbt`: **726/726 mục cần dịch (hoàn tất nội dung bảng)**.
- `NoticeDesc.msbt`: **74/376 mục cần dịch**, còn 302.
- 2.590 mục được phân loại giữ EN không bị đổi.

## Nội dung

- `ban_tra_ve/main_CP007_126.jsonl`: trọn các mục còn lại của main, ID `#00619–#00748` (bỏ các index không thuộc nhóm dịch).
- `ban_tra_ve/NoticeDesc_CP007_74.jsonl`: 74 mục đầu NoticeDesc, ID `#00000–#00093` (bỏ index không thuộc nhóm dịch).
- `ban_tra_ve/CP007_200.jsonl`: 200 mục mới của đợt này.
- `ban_tra_ve/CP003_CP007_958.jsonl`: bản gộp tất cả đợt từ CP003 đến CP007.
- `ban_dich_da_nhap.jsonl`: **6.159 record gốc** sau khi nhập 958 bản nháp; giữ nguyên ID, metadata và nhóm protected.
- `doi_chieu_CP007.csv`: đối chiếu nguồn tiếng Anh / bản nháp Việt.
- `bao_cao/CP007_QA.json`, `bao_cao/bao_cao_nhan_ban_dich.json`: thống kê.
- `tools/nhan_ban_dich.py`: tool nhập bản dịch gốc đi kèm bộ nguồn.

## Quy tắc

Giữ tên Pokémon, item, Move/Skill, tên riêng, thuật ngữ chính (Battle Royale, Hyper Mode, World Rank, Glowing Fountain, Glowdrops...). Lời thoại thân thiện, Gen Z có tiết chế. Không gán bừa danh tính NPC khi chưa có cảnh/portrait. Các dòng `-----`, nhãn quá ngắn và ký hiệu vẫn tính theo **record** được nguồn đánh dấu dịch, nhưng không phải toàn bộ là lời thoại mới.

## QA đã làm

- **200/200 ID** mới hợp lệ; **87/87 token** `{CTRL:hex}` mới được bảo toàn đúng thứ tự.
- Công cụ nhập bản dịch nguồn: **958 mục nhập thành công**, không trùng ID, 974 mục còn thiếu, 2590 mục giữ EN.
- **1 cảnh báo từ điển mới**: chữ `Move` ở câu hướng dẫn `Move using the Circle Pad` mang nghĩa động từ; dịch thành “Di chuyển”, không phải tên Move.
- Đo ký tự thô: không có dòng Việt mới vượt 40 ký tự, **ngoại trừ 1 dòng credits bản quyền giữ nguyên**. Phép đo này không thay thế render 3DS.

## Chưa hoàn thành

**Chưa vá font glyph tiếng Việt, chưa repack MSBT/CX, chưa test trên 3DS/giả lập, chưa có patch chơi được.** Mọi câu thuộc trạng thái `ban_nhap`. Cần test đồng bộ ngôi xưng và khung chữ trong gameplay trước khi duyệt.

**Đợt 008:** tiếp tục `NoticeDesc.msbt` từ mục còn dịch tiếp sau `#00093`; kiểm tra từng nguồn và xuất đầy đủ bàn giao.