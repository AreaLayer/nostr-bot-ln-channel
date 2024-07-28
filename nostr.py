from nostr import PrivateKey, SimpleRelayManager

# Generate a key pair
private_key = PrivateKey()
public_key = private_key.public_key.hex()

# Connect to relays
relay_manager = SimpleRelayManager()
relay_manager.add_relay('wss://relay.nostr.info')
relay_manager.add_relay('wss://nostr-pub.wellorder.net')
relay_manager.run_in_thread()