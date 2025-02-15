from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience.logging import logger
import pandas as pd 

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config    
    
    def validate_all_columns(self)->bool:
        try:
            validation_status = None 
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            validation_status = True 
            for col in all_cols:
                if col not in all_schema:
                    logger.info(f"{col} fails Data Validation stage")
                    validation_status = False 
                    break 
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e 
        