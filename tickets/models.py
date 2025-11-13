from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=50)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='columns')
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.board.name})"


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    column = models.ForeignKey(
        Column, on_delete=models.CASCADE, related_name='tickets')
    priority = models.CharField(
        max_length=10,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        default='medium'
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
        ],
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
