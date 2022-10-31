"""Imagine you have a call center with three levels of employees: respondent, manager, 
and director. An incoming telephone call must be first allocated to a respondent who is free. If the 
respondent cannot handle the call, he or she must escalate the call to a manager. If the manager is not 
free or not able to handle it, then the call should be escalated to a director. Design the classes and 
data structures for this problem. Implement a method dispatchCall() which assigns a call to 
the first available employee
"""

from abc import ABCMeta, abstractmethod
from collections import deque
from enum import Enum


class Rank(Enum):

    RESPONDER = 0
    MANAGER = 1
    DIRECTOR = 2


class Employee(metaclass=ABCMeta):

    def __init__(self, employee_id, name, rank, call_center):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.call = None
        self.call_center = call_center

    def take_call(self, call):
        """Assume the employee will always successfully take the call."""
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS

    def complete_call(self):
        self.call.state = CallState.COMPLETE
        self.call_center.notify_call_completed(self.call)

    @abstractmethod
    def escalate_call(self):
        pass

    def _escalate_call(self):
        self.call.state = CallState.READY
        call = self.call
        self.call = None
        self.call_center.notify_call_escalated(call)


class Responder(Employee):

    def __init__(self, employee_id, name):
        super(Responder, self).__init__(employee_id, name, Rank.RESPONDER)

    def escalate_call(self):
        self.call.level = Rank.MANAGER
        self._escalate_call()


class Manager(Employee):

    def __init__(self, employee_id, name):
        super(Responder, self).__init__(employee_id, name, Rank.MANAGER)

    def escalate_call(self):
        self.call.level = Rank.DIRECTOR
        self._escalate_call()


class Director(Employee):

    def __init__(self, employee_id, name):
        super(Responder, self).__init__(employee_id, name, Rank.DIRECTOR)

    def escalate_call(self):
        raise NotImplementedError('Directors must be able to handle any call')


class CallState(Enum):

    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class Call(object):

    def __init__(self, rank):
        self.state = CallState.READY
        self.rank = rank
        self.employee = None


class CallCenter(object):

    def __init__(self, responders, managers, directors):
        self.responders = responders
        self.managers = managers
        self.directors = directors
        self.queued_calls = deque()

    def dispatch_call(self, call):
        if call.rank not in (Rank.RESPONDER, Rank.MANAGER, Rank.DIRECTOR):
            raise ValueError('Invalid call rank: {}'.format(call.rank))
        employee = None
        if call.rank == Rank.RESPONDER:
            employee = self._dispatch_call(call, self.responders)
        if call.rank == Rank.MANAGER or employee is None:
            employee = self._dispatch_call(call, self.managers)
        if call.rank == Rank.DIRECTOR or employee is None:
            employee = self._dispatch_call(call, self.directors)
        if employee is None:
            self.queued_calls.append(call)

    def _dispatch_call(self, call, employees):
        for employee in employees:
            if employee.call is None:
                employee.take_call(call)
                return employee
        return None

    def notify_call_escalated(self, call):
        pass

    def notify_call_completed(self, call):
        pass

    def dispatch_queued_call_to_newly_freed_employee(self, call, employee):
        pass