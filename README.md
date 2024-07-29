# Nostr bot LN Channel ⚡🟣

>A bot Nostr for Node Runners 

⚠️**Experimental product**

⚠️**WIP & Beta**

⚠️**Only support LND**

### How works 

- Nostr Protocol: The bot connects to Nostr relays to listen for specific events/messages. When it detects a relevant message (e.g., a request for LN channel recommendations), it processes this request.
- Lightning Network: The bot interacts with an LN node (like LND) to gather data about channels. It applies some logic to recommend channels based on certain criteria (e.g., channel capacity, reliability).
- Integration: The bot then sends the recommendations back through the Nostr network to the user who requested them.

### Securtiy considerations

- Run your Lightning Node stable (LND)
- Choose Relays stable
- Self-custody keys
- The project doesn't hold private keys from external users
  
### Roadmap 

- [x] Docs
- [x] Py project
- [ ] Open source 
