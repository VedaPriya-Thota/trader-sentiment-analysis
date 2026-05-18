import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_csv(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded dataset from {path}")
        logger.info(f"Dataset shape: {df.shape}")
        return df

    except Exception as e:
        logger.error(f"Error loading {path}: {e}")
        raise