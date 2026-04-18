# data/events_loader.py

from core.event import Event
import random

def load_events():
    events = []

    for i in range(50):
        features = {
            "gw_strain": random.random(),
            "ringdown_tau": random.random(),
            "xray_luminosity": random.random(),
            "redshift": random.random()
        }
        events.append(Event(i, features))

    return events