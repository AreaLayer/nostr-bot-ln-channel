from nostr import PrivateKey, SimpleRelayManager, Event, EventKind
from config import NOSTR_RELAYS, PRIVATE_KEY_HEX

# Generate keys
private_key = PrivateKey.from_hex(PRIVATE_KEY_HEX)
public_key = private_key.public_key.hex()

# Connect to relays
relay_manager = SimpleRelayManager()
for relay in NOSTR_RELAYS:
    relay_manager.add_relay(relay)
relay_manager.run_in_thread()

def handle_nostr_event(event):
    if event.kind == EventKind.TEXT_NOTE and 'recommend channels' in event.content:
        # Placeholder for channel recommendation logic
        recommendations = "Channel recommendations here"
        response_event = Event(kind=EventKind.TEXT_NOTE, content=recommendations)
        response_event.sign(private_key.hex())
        relay_manager.publish(response_event)

while True:
    event = relay_manager.get_event()
    if event:
        handle_nostr_event(event)