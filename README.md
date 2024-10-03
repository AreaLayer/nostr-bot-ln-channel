# Nostr bot LN Channel ⚡🟣

>A bot Nostr for Node Runners 

[![Bitcoin-only](https://img.shields.io/badge/bitcoin-only-FF9900?logo=bitcoin)](https://twentyone.world)
[![LN](https://img.shields.io/badge/lightning-792EE5?logo=lightning)](https://mempool.space/lightning)
[![Nostr](https://img.shields.io/badge/nostr-only-FF9900?)]((https://user-images.githubusercontent.com/99301796/223592277-34058d0e-af30-411d-8dfe-87c42dacdcf2.png))

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
- Self-custody keys (Nostr and Lightning Node)
  
### Roadmap 

- [x] Docs
- [x] Py project
- [x] Open source 
- [x] Local tests compiling, running and debugging
- [x] Add more info to the Bot
- [ ] APIs
- [ ] LDK & CLN support
- [x] DVMs [WIP]
- [x] CLN plugin 