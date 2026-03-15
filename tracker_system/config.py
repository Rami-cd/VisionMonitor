import yaml
from pathlib import Path
from pydantic import BaseModel

class MLModelConfig(BaseModel):
    name: str
    version: str


class Settings(BaseModel):
    app_name: str
    debug: bool
    tracker_system: MLModelConfig

    @classmethod
    def load(cls):
        yaml_path = Path("config/config.yaml")
        
        with open(yaml_path, "r") as f:
            yaml_data = yaml.safe_load(f)
            
        return cls(**yaml_data)

settings = Settings.load()