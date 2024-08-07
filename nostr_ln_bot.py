# nostr_ln_bot.py
from nostr import PrivateKey, SimpleRelayManager, Event, EventKind
from lndgrpc import LNDClient
from config import NOSTR_RELAYS, PRIVATE_KEY_HEX, LND_GRPC_HOST, LND_MACAROON_PATH, LND_TLS_CERT_PATH
def main():
    # Generate keys
    private_key = PrivateKey.from_hex(PRIVATE_KEY_HEX)
    public_key = private_key.public_key.hex()

    # Connect to relays
    relay_manager = SimpleRelayManager()
    for relay in NOSTR_RELAYS:
        relay_manager.add_relay(relay)
    relay_manager.run_in_thread()

    # Connect to LND
    lnd = LNDClient(
        LND_GRPC_HOST, 
        macaroon_path=LND_MACAROON_PATH, 
        cert_path=LND_TLS_CERT_PATH
    )

    def recommend_channels():
        channels = lnd.list_channels()
        recommended = []
        for channel in channels.channels:
            if channel.remote_balance > 1000000:      
              if channel.local_balance / channel.remote_balance > 0.5:
                if channel.local_balance / channel.remote_balance < 2:
                 recommended.append(channel)
        return recommended

    def handle_nostr_event(event):
        if event.kind == EventKind.TEXT_NOTE and 'recommend channels' in event.content:
            recommendations = recommend_channels()
            recommendations_str = "Recommended Channels:\n" + "\n".join([str(ch) for ch in recommendations])
            response_event = Event(kind=EventKind.TEXT_NOTE, content=recommendations_str)
            response_event.sign(private_key.hex())
            relay_manager.publish(response_event)

    while True:
        event = relay_manager.get_event()
        if event:
            handle_nostr_event(event)

if __name__ == "__main__":
    main()
    
# Generate keys
private_key = PrivateKey.from_hex(PRIVATE_KEY_HEX)
public_key = private_key.public_key.hex()

# Connect to relays
relay_manager = SimpleRelayManager()
for relay in NOSTR_RELAYS:
    relay_manager.add_relay(relay)
relay_manager.run_in_thread()

# Connect to LND
lnd = LNDClient(
    LND_GRPC_HOST, 
    macaroon_path=LND_MACAROON_PATH, 
    cert_path=LND_TLS_CERT_PATH
)

def recommend_channels():
    channels = lnd.list_channels()
    recommended = []
    for channel in channels.channels:
        if channel.capacity > 1000000:
         if channel.local_balance > 1000000:
            if channel.remote_balance > 1000000: 
             recommended.append(channel)
    return recommended

def handle_nostr_event(event):
    if event.kind == EventKind.TEXT_NOTE and 'recommend channels' in event.content:
        recommendations = recommend_channels()
        recommendations_str = "Recommended Channels:\n" + "\n".join([str(ch) for ch in recommendations])
        response_event = Event(kind=EventKind.TEXT_NOTE, content=recommendations_str)
        response_event.sign(private_key.hex())
        relay_manager.publish(response_event)

while True:
    event = relay_manager.get_event()
    if event:
        handle_nostr_event(event)
