import grpc
import interface_pb2
import interface_pb2_grpc
from concurrent import futures

# Define the service implementation
class PoseService(interface_pb2_grpc.PoseServiceServicer):
    def SendCoordinates(self, request, context):
        # Log received coordinates
        print(f"Received Position: ({request.position_x}, {request.position_y}, {request.position_z})")
        print(f"Received Orientation: (Roll: {request.orientation_roll}, Pitch: {request.orientation_pitch}, Yaw: {request.orientation_yaw})")
        
        # Generate a response
        response_message = (
            f"Coordinates received. "
            f"Position: ({request.position_x}, {request.position_y}, {request.position_z}), "
            f"Orientation: (Roll: {request.orientation_roll}, Pitch: {request.orientation_pitch}, Yaw: {request.orientation_yaw})"
        )
        
        return interface_pb2.CoordinatesResponse(message=response_message)

# Main function to start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    interface_pb2_grpc.add_PoseServiceServicer_to_server(PoseService(), server)
    
    server.add_insecure_port("[::]:50051")
    print("Server is running on port 50051...")
    server.start()
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down server...")

if __name__ == "__main__":
    serve()
