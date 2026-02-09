from scale_client import ScaleClient

class SnapshotManager:
    """
    Manager for IBM Storage Scale Snapshots.
    Uses ScaleClient to perform operations.
    """
    def __init__(self, client: ScaleClient):
        """
        Initialize the SnapshotManager.

        Args:
            client (ScaleClient): An authenticated ScaleClient instance.
        """
        self.client = client

    def create_snapshot(self, filesystem, snapshot_name):
        """
        Create a global snapshot for a filesystem.

        Args:
            filesystem (str): The name of the filesystem.
            snapshot_name (str): The name of the new snapshot.

        Returns:
            dict: The API response.
        """
        path = f"/scalemgmt/v3/filesystems/{filesystem}/snapshots"
        payload = {
            "snapshotName": snapshot_name
        }
        return self.client.post(path, data=payload)

    def list_snapshots(self, filesystem):
        """
        List all global snapshots for a filesystem.

        Args:
            filesystem (str): The name of the filesystem.

        Returns:
            list: A list of snapshot dictionaries.
        """
        path = f"/scalemgmt/v3/filesystems/{filesystem}/snapshots"
        response = self.client.get(path)
        # The API typically returns a list under a key like 'snapshots' or directly list
        # Based on IBM docs structure, it usually returns { "snapshots": [...] }
        return response.get('snapshots', [])

    def delete_snapshot(self, filesystem, snapshot_name):
        """
        Delete a global snapshot.

        Args:
            filesystem (str): The name of the filesystem.
            snapshot_name (str): The name of the snapshot to delete.

        Returns:
            dict: The API response.
        """
        # Ensure snapshot name is URL safe if needed, but requests usually handles basic chars
        path = f"/scalemgmt/v3/filesystems/{filesystem}/snapshots/{snapshot_name}"
        return self.client.delete(path)
