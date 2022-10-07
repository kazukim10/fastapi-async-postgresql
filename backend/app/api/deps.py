from app.db.session import async_session_generator


async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            async with session.begin():
                yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
