import unittest
from unittest.mock import MagicMock, patch
import json
from scale_client import ScaleClient
from snapshot_manager import SnapshotManager

class TestScaleModules(unittest.TestCase):

    def setUp(self):
        self.endpoint = "https://mock-scale.example.com"
        self.username = "admin"
        self.password = "password"
        self.filesystem = "fs1"
        self.snapshot_name = "test-snap"

    @patch('requests.Session')
    def test_workflow(self, mock_session_cls):
        # Mock the session instance
        mock_session = mock_session_cls.return_value
        
        # Initialize client
        client = ScaleClient(self.endpoint, self.username, self.password)
        manager = SnapshotManager(client)
        
        # Test 1: Create Snapshot
        mock_response_create = MagicMock()
        mock_response_create.status_code = 200
        mock_response_create.json.return_value = {"jobs": [{"jobId": 123}]}
        mock_session.post.return_value = mock_response_create
        
        response = manager.create_snapshot(self.filesystem, self.snapshot_name)
        
        self.assertEqual(response['jobs'][0]['jobId'], 123)
        mock_session.post.assert_called_with(
            f"{self.endpoint}/scalemgmt/v3/filesystems/{self.filesystem}/snapshots",
            json={"snapshotName": self.snapshot_name}
        )
        print("Create Snapshot: PASSED")

        # Test 2: List Snapshots
        mock_response_list = MagicMock()
        mock_response_list.status_code = 200
        mock_response_list.json.return_value = {
            "snapshots": [
                {"snapshotName": "snap1"},
                {"snapshotName": self.snapshot_name}
            ]
        }
        mock_session.get.return_value = mock_response_list
        
        snapshots = manager.list_snapshots(self.filesystem)
        self.assertEqual(len(snapshots), 2)
        self.assertEqual(snapshots[1]['snapshotName'], self.snapshot_name)
        
        mock_session.get.assert_called_with(
            f"{self.endpoint}/scalemgmt/v3/filesystems/{self.filesystem}/snapshots",
            params=None
        )
        print("List Snapshots: PASSED")

        # Test 3: Delete Snapshot
        mock_response_delete = MagicMock()
        mock_response_delete.status_code = 204 # No content on success often
        mock_session.delete.return_value = mock_response_delete
        
        manager.delete_snapshot(self.filesystem, self.snapshot_name)
        
        mock_session.delete.assert_called_with(
             f"{self.endpoint}/scalemgmt/v3/filesystems/{self.filesystem}/snapshots/{self.snapshot_name}"
        )
        print("Delete Snapshot: PASSED")

if __name__ == '__main__':
    unittest.main()
