from typing import Callable, Dict, List
import asyncio

event_handlers: Dict[str, List[Callable]] = {}

def register_event(event_name: str):
    """
    Register an event name for event handlers.
    """
    if event_name not in event_handlers:
        event_handlers[event_name] = []

def add_event_handler(event_name: str, handler: Callable):
    """
    Add a handler function for a specific event.
    """
    if event_name in event_handlers:
        event_handlers[event_name].append(handler)

def trigger_event(event_name: str, *args, **kwargs):
    """
    Trigger all handlers associated with an event.
    """
    if event_name in event_handlers:
        for handler in event_handlers[event_name]:
            asyncio.create_task(handler(*args, **kwargs))