from app.providers.sbi import SBIProvider
from app.providers.hdfc import HDFCProvider
from app.providers.icici import ICICIProvider
from app.providers.axis import AxisProvider
from app.providers.kotak import KotakProvider
from app.providers.bob import BoBProvider
from app.providers.pnb import PNBProvider
from app.providers.canara import CanaraProvider
from app.providers.union import UnionProvider
from app.providers.idfc import IDFCProvider


providers = {
    "SBI": SBIProvider(),
    "HDFC": HDFCProvider(),
    "ICICI": ICICIProvider(),
    "AXIS": AxisProvider(),
    "KOTAK": KotakProvider(),
    "BOB": BoBProvider(),
    "PNB": PNBProvider(),
    "CANARA": CanaraProvider(),
    "UNION": UnionProvider(),
    "IDFC": IDFCProvider()
}