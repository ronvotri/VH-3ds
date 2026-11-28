# QA049 — Chuẩn bị tích hợp (chưa phải bản vá)

Bản dữ liệu ngôn ngữ được chốt ở QA049: 32.067 ID (18.896 Base, 13.171 Update).
SHA-256 của QA049_FULL_32067.jsonl:
`77c11605dc8e6b8b2b452892652afdc38a2b215ba7620acce44c07d98e191809`.

Gói cục bộ `SnackWorld_QA049_INTEGRATION_READY.zip` chứa dataset nguyên vẹn, source_manifest.json (1.868 cặp phiên bản/đường dẫn), pilot_manifest.json (7 file, 123 chuỗi), bộ kiểm tra chỉ đọc và inventory font/ngoại lệ. Dataset và manifest chưa được đồng bộ lên GitHub; checkpoints CP001–044 được giữ nguyên. Không dùng checkpoint trên repo làm bản QA049 thay thế.

## Nguồn cần có

Ưu tiên gói SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip hoặc archive_a.fa Base/Update trích từ game hợp pháp của người dùng. Nếu đã giải nén, root từng phiên bản phải chứa data/txt/ja và fnt.

Pilot:
- Base: data/txt/ja/gamedata/ev/ev01_0010_ja.cfg.bin
- Base: data/txt/ja/gamedata/ev/ev01_0900_ja.cfg.bin
- Base: data/txt/ja/gamedata/menu/config_menu_text.cfg.bin
- Base: data/txt/ja/gamedata/menu/trade_menu_text.cfg.bin
- Base: data/txt/ja/gamedata/menu/quest_result_text.cfg.bin
- Update: data/txt/ja/gamedata/menu/quest_result_text.cfg.bin
- Base: data/txt/ja/gamedata/ev/ev90_4050_ja.cfg.bin

Cần thêm fnt/ft_nrm.xf và fnt/ft_sml.xf ở cả Base/Update để kiểm font.

```
python qa049_preflight.py --dataset /path/to/QA049_FULL_32067.jsonl --manifest /path/to/source_manifest.json --base /path/to/extracted_base --update /path/to/extracted_update --report ./preflight_result.json
```

Công cụ chỉ đọc đã đạt 8 bài kiểm thử mô phỏng. Chưa có binary nguồn để xác minh thực tế. Không tự ghi đè pool: 9.975 chuỗi đích dài hơn nguồn theo byte UTF-8, 6.933 chuỗi chưa có reference được bộ trích xuất nhận diện. Cần giải CFG, thử round-trip không đổi, vá font, repack ARC0 và kiểm thử game trước khi phát hành. Không tuyên bố đã tạo CIA/Luma hoặc hoàn tất bản vá.
