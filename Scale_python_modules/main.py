import argparse
import sys
import json
import urllib3
from requests.exceptions import HTTPError

from scale_client import ScaleClient
from snapshot_manager import SnapshotManager

def main():
    parser = argparse.ArgumentParser(description="IBM Storage Scale Snapshot Workflow")
    parser.add_argument("--endpoint", required=True, help="Scale REST API Endpoint (e.g., https://192.168.1.100:443)")
    parser.add_argument("--username", required=True, help="Username for authentication")
    parser.add_argument("--password", required=True, help="Password for authentication")
    parser.add_argument("--filesystem", required=True, help="Filesystem to manage snapshots for")
    parser.add_argument("--snapshot", default="test-snap-01", help="Name of the snapshot to create")
    parser.add_argument("--verify-ssl", action="store_true", help="Verify SSL certificates")

    args = parser.parse_args()

    # Initialize Client and Manager
    print(f"Connecting to {args.endpoint} as {args.username}...")
    try:
        client = ScaleClient(args.endpoint, args.username, args.password, verify_ssl=args.verify_ssl)
        manager = SnapshotManager(client)
    except Exception as e:
        print(f"Error initializing client: {e}")
        sys.exit(1)

    # 1. Create Global Snapshot
    print(f"\n[1] Creating snapshot '{args.snapshot}' on filesystem '{args.filesystem}'...")
    try:
        response = manager.create_snapshot(args.filesystem, args.snapshot)
        print(f"Snapshot creation response: {json.dumps(response, indent=2)}")
        # Check if response contains jobs, usually means async operation
        if 'jobs' in response:
            print("Note: Snapshot creation initiated as an async job.")
    except HTTPError as e:
        print(f"Failed to create snapshot: {e}")
        # Use response text if available
        if e.response is not None:
             print(f"Server response: {e.response.text}")
        sys.exit(1)

    # 2. List Snapshots and Verify
    print(f"\n[2] Listing snapshots for filesystem '{args.filesystem}'...")
    try:
        snapshots = manager.list_snapshots(args.filesystem)
        print(f"Found {len(snapshots)} snapshots.")
        
        found = False
        for snap in snapshots:
            # Adjust key based on actual API response, usually 'snapshotName' or 'name'
            name = snap.get('snapshotName', snap.get('name'))
            print(f" - {name}")
            if name == args.snapshot:
                found = True
        
        if found:
            print(f"SUCCESS: Snapshot '{args.snapshot}' was found in the list.")
        else:
            print(f"FAILURE: Snapshot '{args.snapshot}' was NOT found in the list.")
            sys.exit(1)
            
    except HTTPError as e:
        print(f"Failed to list snapshots: {e}")
        sys.exit(1)

    # 3. Delete Snapshot
    print(f"\n[3] Deleting snapshot '{args.snapshot}'...")
    try:
        response = manager.delete_snapshot(args.filesystem, args.snapshot)
        print(f"Snapshot deletion response: {json.dumps(response, indent=2)}")
    except HTTPError as e:
        print(f"Failed to delete snapshot: {e}")
        sys.exit(1)

    # 4. Verify Deletion
    print(f"\n[4] Verifying deletion...")
    try:
        snapshots = manager.list_snapshots(args.filesystem)
        
        found = False
        for snap in snapshots:
            name = snap.get('snapshotName', snap.get('name'))
            if name == args.snapshot:
                found = True
                break
        
        if not found:
            print(f"SUCCESS: Snapshot '{args.snapshot}' is no longer in the list.")
        else:
            print(f"FAILURE: Snapshot '{args.snapshot}' still exists!")
            sys.exit(1)

    except HTTPError as e:
         print(f"Failed to verify deletion: {e}")
         sys.exit(1)

    print("\nWorkflow completed successfully.")

if __name__ == "__main__":
    main()
