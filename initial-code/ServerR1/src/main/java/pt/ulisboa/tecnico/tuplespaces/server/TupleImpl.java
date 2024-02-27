package pt.ulisboa.tecnico.tuplespaces.server;

import static io.grpc.Status.*;
import io.grpc.stub.StreamObserver;
import pt.ulisboa.tecnico.tuplespaces.server.domain.ServerState;
import pt.ulisboa.tecnico.tuplespaces.centralized.contract.TupleSpacesGrpc;
import pt.ulisboa.tecnico.tuplespaces.centralized.contract.TupleSpacesCentralized.*;


public class TupleImpl extends TupleSpacesGrpc.TupleSpacesImplBase {

    private final ServerState serverState = new ServerState();

    @Override
    public void put(PutRequest request, StreamObserver<PutResponse> responseObserver){

            String newTuple = request.getNewTuple();
            this.serverState.put(newTuple);
            PutResponse.Builder response = PutResponse.newBuilder();
            responseObserver.onNext(response.build());
            responseObserver.onCompleted();
    }

    @Override
    public void take(TakeRequest request, StreamObserver<TakeResponse> responseObserver){

        String searchPattern = request.getSearchPattern();
        this.serverState.take(searchPattern);
        TakeResponse.Builder response = TakeResponse.newBuilder();
        responseObserver.onNext(response.build());
        responseObserver.onCompleted();
    }
}
