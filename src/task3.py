import logging

a = 5
b = 0

try:
    c = a / b
except Exception:
    logging.exception("Exception occurred")





