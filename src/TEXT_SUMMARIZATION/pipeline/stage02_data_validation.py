from TEXT_SUMMARIZATION.config.configuration import ConfigurationManager
from TEXT_SUMMARIZATION.conponents.data_validation import DataValiadtion
from TEXT_SUMMARIZATION.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
