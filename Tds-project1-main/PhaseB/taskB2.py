import os
from fastapi import HTTPException

def is_valid_deletion(filepath, base_dir="/data"):
    """Check if a file is inside the /data directory and prevent deletion."""
    abs_filepath = os.path.abspath(filepath)
    abs_base_dir = os.path.abspath(base_dir)
    
    if not abs_filepath.startswith(abs_base_dir):
        raise HTTPException(status_code=403, detail=f"Deletion of this file: {filepath} is forbidden")
    
    # Here we prevent deletion explicitly
    raise HTTPException(status_code=403, detail=f"File deletion is not allowed: {filepath}")
    
    return True
