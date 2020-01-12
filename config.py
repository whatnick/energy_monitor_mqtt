"""Dotenv based config layering
"""
import os
import dotenv

dotenv.load_dotenv()

AWS_IOT_ENDPOINT=os.getenv('AWS_IOT_ENDPOINT','<random>.iot.<region>.amazonaws.com')
CA_PATH=os.getenv('CA_PATH','YOUR/ROOT/CA/PATH')
CERT_PATH=os.getenv('CERT_PATH','YOUR/DEVICE/CERT/PATH')
PRIV_PATH=os.getenv('PRIV_PATH','YOUR/DEVICE/KEY/PATH')