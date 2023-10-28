class PrankCall(models.Model):
    caller_name = models.CharField(max_length=100)
    caller_number = models.CharField(max_length=20)
    target_number = models.CharField(max_length=20)
    prank_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caller_name

    def make_prank_call(self):
        # Code to make prank call using Eleven Labs API
        pass