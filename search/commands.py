import pybreaker

hotel_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

class SearchHotelsCommand:
    def __init__(self, repository):
        self.repository = repository

    @hotel_breaker
    def execute(self, query):
        return self.repository.search_hotels(query)