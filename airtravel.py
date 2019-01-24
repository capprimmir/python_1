
class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'". format(number))
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        # list comprehnesion with a dictionary comprehension
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        # return " MM33"
        return self._number 

    def ariline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

# class to model different types of aircrafts
class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    # arrange seats in a single tuple
    def seating_plan(self):
        return (range(1, self._num_rows + 1), 
        "ABCDEFGHJK"[:self._num_seats_per_row])