# Contributing

Keep parsers conservative: report malformed input rather than silently repair it. Do not mix code licensing with source dataset licensing. For data changes, preserve exact API record, file URL, retrieval timestamp and checksum; review source attribution/terms. Add unit tests for deterministic computations and test with `python -m pytest`. No generated secrets, credentials, or unrelated large datasets.
