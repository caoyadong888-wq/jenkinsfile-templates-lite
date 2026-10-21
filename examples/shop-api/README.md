# shop-api helper (lite)

`src/app.py` is the helper the full pack's Jenkinsfile tests. `quote_total` multiplies cents by quantity and rejects negatives. `health` reports `shop.example.com`.

Run it without Jenkins:

```bash
python3 -c "import sys; sys.path.insert(0, 'examples/shop-api/src'); import app; print(app.quote_total(250, 2))"
```

The filled Jenkinsfile, its pytest file, the docker agent, and the matrix stub are in the full pack.
