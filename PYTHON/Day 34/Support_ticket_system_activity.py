class Ticket:
    def __init__(self, ticket_id, title, priority):
        self.ticket_id = ticket_id
        self.title = title
        self._priority = priority
    @property 
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        list1 = ["low", "medium", "high"]
        if  value  in list1:
            self._priority = value
        else:
            raise ValueError("Value is out of bound")
    def __str__(self):
        return f"Ticket {self.ticket_id}: {self.title} (Priority: {self.priority})"
class Loggable:
    def log_activity(self):
        return "Activity logged"

class BugTicket(Ticket, Loggable):
    def __init__(self, ticket_id, title, priority, severity):
        super().__init__(ticket_id, title, priority)
        self.severity = severity
    def resolve(self):
        return "Bug fixed and deployed"

class FeatureRequestTicket(Ticket):
    def __init__(self, ticket_id, title, priority, requested_by):
        super().__init__(ticket_id, title, priority)
        self.requested_by = requested_by
    def resolve(self):
        return "Feature added to roadmap"

class TicketSystem:
    def __init__(self):
        self.tickets = []
    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def show_all(self):
        for val in self.tickets:
            print(val)


t1 = BugTicket(102, "Login page crashes on submit", "high", "critical")
f1 = FeatureRequestTicket(129, "Add dark mode support", "medium", "vani")
tic = TicketSystem()
tic.add_ticket(t1)
tic.add_ticket(f1)

tic.show_all()
print(t1.resolve())
print(t1.log_activity())
            