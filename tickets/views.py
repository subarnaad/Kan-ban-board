from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Board, Column, Ticket
from .serializers import BoardSerializer, ColumnSerializer, TicketSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('-created_at')
    serializer_class = BoardSerializer


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all().order_by('position')
    serializer_class = ColumnSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        # Optional: handle offline data syncing (if you add is_synced)
        serializer.save()
