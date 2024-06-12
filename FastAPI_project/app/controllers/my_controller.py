from app.models.my_model import Payload, Output
from multiprocessing import Pool
from app.utils import logger
from typing import List

class MyController:
    def add_numbers(numbers: List[int]) -> int:
        try:
            logger.debug(f"Starting addition for: {numbers}")
            result = sum(numbers)
            logger.debug(f"Result of addition for {numbers}: {result}")
            return result
        except Exception as e:
            logger.error(f"Error occurred while adding numbers {numbers}: {e}")
            return 0

    def add_list(lists_of_numbers: List[List[int]]) -> List[int]:
        try:
            with Pool() as pool:
                results = pool.map(MyController.add_numbers, lists_of_numbers)
                return results
        except Exception as e:
            logger.error(f"Error occurred during multiprocessing: {e}")
            return []