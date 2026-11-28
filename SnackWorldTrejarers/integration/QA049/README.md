# Snack World: Trejarers — QA049 full snapshot

QA049 is the cumulative localization integration dataset, not a playable game patch. This directory preserves the entire 6,368,493-byte integration ZIP as 17 ordered binary parts because the connector could not transmit the entire ZIP in one request. All parts have been checked against the local source by Git blob SHA. This snapshot does not overwrite the old CP001–044 checkpoints.

## Reconstruct and verify

From this directory, with Python 3:

```sh
python assemble_qa049.py
```

The tool verifies the combined ZIP size, SHA-256, ZIP CRC, embedded dataset SHA-256, and 32,067 unique IDs before writing a new archive. It refuses to overwrite an existing output. It was tested against the original ZIP, a corrupt part, and an existing destination.

- ZIP SHA-256: `f92f1d705e2251453984cdfe941c0b1c8a64f57cc5b5114c61663d1a86c521d0`
- Dataset SHA-256: `77c11605dc8e6b8b2b452892652afdc38a2b215ba7620acce44c07d98e191809`
- 18,896 Base IDs and 13,171 Update IDs; 1,868 source file/version pairs.
- Includes the source manifest, seven-file pilot, read-only preflight tool, QA reports and inventories.

Extract the rebuilt ZIP into a separate working directory. Read the included README. The data is ready for source matching, not for direct binary injection. Original Base/Update archives or extracted pilot CFG/font files are still needed. CFG reimport, font changes, ARC0 repack and runtime testing remain unverified. No new linguistic changes were made during this sync.
