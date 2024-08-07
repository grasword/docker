FROM python:alpine

WORKDIR /app

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000"]
# The -q flag makes wget operate in quiet mode, and -O- outputs the response to standard output.
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD wget -qO- http://localhost:8000 || exit 1