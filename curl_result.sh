curl -s http://localhost:8008/q01.arrows | duckdb -c "INSTALL arrow FROM community; LOAD arrow; FROM read_arrow('/dev/stdin')"
