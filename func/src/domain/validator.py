from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class Asset(BaseModel):
    ticker: str
    mean_price: float
    initial_quantity: int
    current_quantity: Any
    spent_value: int
    current_value: Any


Wallet = List[Asset]


class Portfolio(BaseModel):
    wallet_id_br: Optional[str]
    wallet_br: Wallet
    wallet_id_us: Optional[str]
    wallet_us: Wallet
    wallets_vnc_br: Dict[str, Wallet]


class VaiNaColaWalletReport(BaseModel):
    id: str
    influencer: str
    influencer_type: str
    report_date: str
    profitability: str
    rebalance_date: str


class BlockSummary(BaseModel):
    block_type: str
    description: str
    date: str
    lawsuit_number: str


class WarrantySummary(BaseModel):
    available: str
