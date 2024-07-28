while True:
    event = relay_manager.get_event()
    if event:
        handle_nostr_event(event)