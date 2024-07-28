from nostr.event import Event, EventKind

def handle_nostr_event(event):
    if event.kind == EventKind.TEXT_NOTE and 'recommend channels' in event.content:
        recommendations = recommend_channels(lnd.list_channels())
        response_content = "Recommended Channels:\n" + "\n".join([str(ch) for ch in recommendations])
        response_event = Event(kind=EventKind.TEXT_NOTE, content=response_content)
        response_event.sign(private_key.hex())
        relay_manager.publish(response_event)