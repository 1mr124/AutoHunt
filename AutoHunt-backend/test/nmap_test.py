import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.nmap_handler import NmapHandler

print("Successfully imported NmapHandler!")
