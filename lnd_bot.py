# lnd_bot.py
from lndgrpc import LNDClient
from config import LND_GRPC_HOST, LND_MACAROON_PATH, LND_TLS_CERT_PATH

# Connect to LND
lnd = LNDClient(
    LND_GRPC_HOST, 
    macaroon_path=LND_MACAROON_PATH, 
    cert_path=LND_TLS_CERT_PATH
)

def recommend_channels():
    channels = lnd.list_channels()
    # Example recommendation logic
    recommended = []
    for channel in channels.channels:
     if channel.remote_balance > 1000000:
        if channel.local_balance > 1000000:
            recommended.append(channel)
    return recommended
