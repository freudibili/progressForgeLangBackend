import uvicorn
import sys
from pathlib import Path

# Add the src directory to the Python path
src_path = str(Path(__file__).parent / "src")
sys.path.append(src_path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 