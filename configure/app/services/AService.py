import asyncio, logging, random, string


log = logging.getLogger(__name__)

class AService:
    async def run(self, equipment_id: str, parameters: dict, timeout: int) -> str:
        await asyncio.sleep(timeout) # call service A
        log.info("A service is finished")
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))