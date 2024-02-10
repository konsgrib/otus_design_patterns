class ExceptionHandler:
    exceptions = {
        "EventA": {
            "ZeroDivisionError": "print('Handler for EventA error type ZeroDivisionError')",
            "KeyError": "print('Handler for EventA error typeKeyError')",
            "IndexError": "print('Handler for EventA error typeIndexError')",
        },
        "EventB": {
            "ZeroDivisionError": "print('Handler for EventB error type ZeroDivisionError')",
            "KeyError": "print('Handler for EventB error type KeyError')",
            "IndexError": "print('Handler for EventB error type IndexError')",
        },
        "EventC": {
            "ZeroDivisionError": "print('Handler for EventC error type ZeroDivisionError')",
            "KeyError": "print('Handler for EventC error type KeyError')",
            "IndexError": "print('Handler for EventC error type IndexError')",
        },
        "EventD": {
            "ZeroDivisionError": "print('Handler for EventD error type ZeroDivisionError')",
            "KeyError": "print('Handler for EventD error type KeyError')",
            "IndexError": "print('Handler for EventD error type IndexError')",
        },
    }

    def handle(self, event, exception):
        event_exceptions = self.exceptions.get(event.__name__)
        if not event_exceptions:
            print("Event not found in exceptions dictionary")
            return
        exception_name = str(exception.__class__.__name__)
        exception_handler = event_exceptions.get(exception_name)
        if not exception_handler:
            print(f"{exception_name}: Exception not found in dictionary for event")
            return
        exec(exception_handler)
