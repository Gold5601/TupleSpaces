package pt.ulisboa.tecnico.tuplespaces.client.grpc;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import pt.ulisboa.tecnico.tuplespaces.centralized.contract.TupleSpacesGrpc;
import pt.ulisboa.tecnico.tuplespaces.centralized.contract.TupleSpacesCentralized.*;


public class ClientService {

    private final String target;

    public ClientService(String target){ this.target = target; }

    public String getTarget(){
        return this.target;
    }

    public void put(String tuple){
        try{
            final ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
            final TupleSpacesGrpc.TupleSpacesBlockingStub stub = TupleSpacesGrpc.newBlockingStub(channel);
            PutResponse response = stub.put(PutRequest.newBuilder().setNewTuple(tuple).build());

            System.out.println("OK");

            channel.shutdown();
        } catch (StatusRuntimeException e) {
            System.out.println("Caught exception with description " + e.getStatus().getDescription());
        }
    }

    public void take(String tuple){
        try{
            final ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
            final TupleSpacesGrpc.TupleSpacesBlockingStub stub = TupleSpacesGrpc.newBlockingStub(channel);
            TakeResponse response = stub.take(TakeRequest.newBuilder().setSearchPattern(tuple).build());

            System.out.println("OK");
            System.out.println(response.getResult());

            channel.shutdown();
        } catch (StatusRuntimeException e) {
            System.out.println("Caught exception with description " + e.getStatus().getDescription());
        }
    }
}
