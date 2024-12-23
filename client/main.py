import grpc
import interface_pb2_grpc
import interface_pb2

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = interface_pb2_grpc.PoseServiceStub(channel)
        
        # Create a request with sample data
        request = interface_pb2.CoordinatesRequest(
            position_x=1.0,
            position_y=2.0,
            position_z=3.0,
            orientation_roll=0.5,
            orientation_pitch=1.5,
            orientation_yaw=2.5
        )
        
        # Make the RPC call
        try:
            response = stub.SendCoordinates(request)
            print(f"Server response: {response.message}")
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()} - {e.details()}")

if __name__ == "__main__":
    run()
