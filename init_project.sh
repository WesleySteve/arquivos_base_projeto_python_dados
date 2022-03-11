python3 -m venv .venv && sleep 2 && \
. .venv/bin/activate && sleep 1 && \
make install && \
pre-commit install
