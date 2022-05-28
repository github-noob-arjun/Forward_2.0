import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    #SESSION = os.environ.get("SESSION", "Forward_Session")
    SESSION = "BQA_XggfiAJKLn8Ue2tLz_C7r6jGnOboJWwEg_iiHok9WchzD4krNJmUoI2guFLBPBeacOpHnYKalItjtuHXA-j4aJ12wLArlmMkhUlmy7GnHd0s69M2n1tyg2AsgHe5LzSHNVOBpVpzQwaLQcmm0Rqi4YVCMgaTf3Re4GAoPIKeKdtOREIox-zZ3j-rG5hLYtQwFzaKiyi9wzMf44hpCvRiQ2udqBtgdFArBcBQoaXaIKEuZ5arYKmUusc2bnm1Zx_1FWn7WfdjJ3yUnnI2F4S8EBWdCuH7UfeX7hJ4Pg5N_lEgVuX_dG2BxS8XLBNHQ18WhjoHFabfNesoye5USZT9cBEteAA"
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
