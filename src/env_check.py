import os
from dotenv import load_dotenv

load_dotenv()
print("Loaded DEMO_KEY:", os.getenv("DEMO_KEY"))