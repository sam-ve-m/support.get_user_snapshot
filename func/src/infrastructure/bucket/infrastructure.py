from contextlib import asynccontextmanager

import aioboto3
from decouple import config
from etria_logger import Gladsheim


class BucketInfrastructure:
    session = None
    client = None

    @classmethod
    def _get_session(cls):
        if cls.session is None:
            cls.session = aioboto3.Session(
                aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
                region_name=config("REGION_NAME"),
            )
        return cls.session

    @classmethod
    @asynccontextmanager
    async def get_resource(cls):
        try:
            session = cls._get_session()
            async with session.resource("s3") as s3_resource:
                yield s3_resource
        except Exception as ex:
            Gladsheim.error(error=ex)
            raise ex
