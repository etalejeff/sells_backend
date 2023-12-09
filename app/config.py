# config.py
import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgres://sell_user:Ll49YhsKgjT50RsDycL82vLxsWs5Zapl@dpg-clp1kbpoh6hc73br1020-a/sell")
    # Add more configuration variables as needed
