import os

from loguru import logger
from sblpy.connection import SurrealSyncConnection
from sblpy.migrations.db_processes import get_latest_version
from sblpy.migrations.migrations import Migration
from sblpy.migrations.runner import MigrationRunner


class MigrationManager:
    def __init__(self):
        self.connection = SurrealSyncConnection(
            host=os.environ["SURREAL_ADDRESS"],
            port=int(os.environ["SURREAL_PORT"]),
            user=os.environ["SURREAL_USER"],
            password=os.environ["SURREAL_PASS"],
            namespace=os.environ["SURREAL_NAMESPACE"],
            database=os.environ["SURREAL_DATABASE"],
            encrypted=False,  # Set to True if using SSL
        )
        self.up_migrations = [Migration.from_file("migrations/1.surrealql")]
        self.down_migrations = [Migration.from_file("migrations/1_down.surrealql")]
        self.runner = MigrationRunner(
            up_migrations=self.up_migrations,
            down_migrations=self.down_migrations,
            connection=self.connection,
        )

    def get_current_version(self) -> int:
        return get_latest_version(
            self.connection.host,
            self.connection.port,
            self.connection.user,
            self.connection.password,
            self.connection.namespace,
            self.connection.database,
        )

    @property
    def needs_migration(self) -> bool:
        current_version = self.get_current_version()
        return current_version < len(self.up_migrations)

    def run_migration_up(self):
        current_version = self.get_current_version()
        logger.debug(f"Current version before migration: {current_version}")

        if self.needs_migration:
            try:
                self.runner.run()
                new_version = self.get_current_version()
                logger.debug(f"Migration successful. New version: {new_version}")
            except Exception as e:
                logger.error(f"Migration failed: {str(e)}")
        else:
            logger.debug("Database is already at the latest version")
