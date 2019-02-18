#!/usr/bin/env bash

case $LAYER in
  cloud)

    test ! -f application/ws/app_protocols/HTTPProtocol.o || rm application/ws/app_protocols/HTTPProtocol.o
    test ! -f application/orchestrator/RemoteOrchestrator.o || rm application/orchestrator/RemoteOrchestrator.o

    echo "Running CLOUD simulation..."

    ;;
  fog)

    test ! -f application/ws/app_protocols/HTTPProtocol.o || rm application/ws/app_protocols/HTTPProtocol.o

    echo "Running FOG simulation..."

    ;;
  *) # edge

    test ! -f application/ws/app_protocols/DistributionProtocol.o || rm application/ws/app_protocols/DistributionProtocol.o

    echo "Running EDGE simulation..."

    ;;
esac

cd pal
dana -sp ../application/ EmergentSys.o &
sleep 1
dana -sp ../application/ AutonomousPerception.o
